"""
PDF / text RAG demo — load documents → chunk → Chroma → ask with Ollama.

Prerequisites:
  ollama pull llama3.2
  ollama pull nomic-embed-text
  pip install -r 23_pdf_rag_requirements.txt

Usage:
  python 23_pdf_rag_demo.py                          # index sample handbook + ask demo questions
  python 23_pdf_rag_demo.py path/to/your/file.pdf    # index your PDF first, then ask
  python 23_pdf_rag_demo.py --reindex path/to/doc.txt
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

import chromadb
import requests
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from pypdf import PdfReader

OLLAMA_URL = "http://localhost:11434"
CHAT_MODEL = "llama3.2"
EMBED_MODEL = "nomic-embed-text"
DB_PATH = Path(__file__).resolve().parent / "chroma_pdf_rag_db"
COLLECTION = "pdf_rag"
SAMPLE_DOC = Path(__file__).resolve().parent / "23_sample_docs" / "xyz_handbook.txt"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 80

class OllamaEmbedding(EmbeddingFunction[Documents]):
    def __call__(self, input: Documents) -> Embeddings:
        vectors: Embeddings = []
        for text in input:
            response = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={"model": EMBED_MODEL, "prompt": text},
                timeout=120,
            )
            response.raise_for_status()
            vectors.append(response.json()["embedding"])
        return vectors


def load_document(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages).strip()
    if suffix in {".txt", ".md"}:
        return path.read_text(encoding="utf-8").strip()
    raise ValueError(f"Unsupported file type: {suffix} (use .pdf, .txt, or .md)")


def chunk_text(text: str, source: str) -> list[dict]:
    sections = re.split(r"(?=^Section \d+)", text, flags=re.MULTILINE)
    sections = [s.strip() for s in sections if s.strip()]
    if len(sections) <= 1:
        sections = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks: list[dict] = []
    index = 0

    for section in sections:
        if len(section) <= CHUNK_SIZE:
            chunks.append(
                {
                    "id": f"{source}-{index}",
                    "text": section,
                    "metadata": {"source": source, "chunk": index},
                }
            )
            index += 1
            continue

        start = 0
        while start < len(section):
            end = min(start + CHUNK_SIZE, len(section))
            chunks.append(
                {
                    "id": f"{source}-{index}",
                    "text": section[start:end].strip(),
                    "metadata": {"source": source, "chunk": index},
                }
            )
            index += 1
            if end >= len(section):
                break
            start = max(end - CHUNK_OVERLAP, start + 1)

    return chunks


def collection_name_for(source: str) -> str:
    digest = hashlib.md5(source.encode()).hexdigest()[:8]
    return f"{COLLECTION}_{digest}"


def get_collection(source: str):
    client = chromadb.PersistentClient(path=str(DB_PATH))
    return client.get_or_create_collection(
        name=collection_name_for(source),
        embedding_function=OllamaEmbedding(),
    )


def index_document(path: Path, reindex: bool = False) -> chromadb.Collection:
    source = path.name
    collection = get_collection(source)

    if collection.count() > 0 and not reindex:
        print(f"Using existing index for {source} ({collection.count()} chunks)")
        return collection

    if reindex and collection.count() > 0:
        client = chromadb.PersistentClient(path=str(DB_PATH))
        client.delete_collection(collection_name_for(source))

    print(f"Loading {path}...")
    text = load_document(path)
    if not text:
        raise ValueError(f"No text extracted from {path}")

    chunks = chunk_text(text, source)
    print(f"Indexing {len(chunks)} chunks into Chroma...")
    collection.add(
        ids=[c["id"] for c in chunks],
        documents=[c["text"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks],
    )
    return collection


def retrieve(collection, question: str, top_k: int = 3) -> list[str]:
    results = collection.query(query_texts=[question], n_results=top_k)
    return results["documents"][0]


def ask_llm(question: str, context_chunks: list[str]) -> str:
    context = "\n\n---\n\n".join(context_chunks)
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": CHAT_MODEL,
            "stream": False,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Answer using only the context below. "
                        "If the answer is not in the context, say you do not know.\n\n"
                        f"Context:\n{context}"
                    ),
                },
                {"role": "user", "content": question},
            ],
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


def run_qa(collection, questions: list[str], with_llm: bool = True) -> None:
    print("\n--- PDF / document RAG ---\n")
    for question in questions:
        chunks = retrieve(collection, question)
        print(f"Q: {question}")
        print("Retrieved:")
        for chunk in chunks:
            preview = chunk[:120] + ("..." if len(chunk) > 120 else "")
            print(f"  - {preview}")
        if with_llm:
            answer = ask_llm(question, chunks)
            print(f"A: {answer}\n")
        else:
            print()


DEFAULT_QUESTIONS = [
    "Where does vipin work?",
    "what's his skills?"
]


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF/text RAG with Chroma + Ollama")
    parser.add_argument(
        "document",
        nargs="?",
        type=Path,
        help="PDF, .txt, or .md to index (default: sample handbook)",
    )
    parser.add_argument("--reindex", action="store_true", help="Force rebuild of the index")
    parser.add_argument("--retrieve-only", action="store_true", help="Skip LLM answer step")
    args = parser.parse_args()

    doc_path = args.document or SAMPLE_DOC
    if not doc_path.exists():
        print(f"File not found: {doc_path}", file=sys.stderr)
        sys.exit(1)

    collection = index_document(doc_path, reindex=args.reindex)
    run_qa(collection, DEFAULT_QUESTIONS, with_llm=not args.retrieve_only)


if __name__ == "__main__":
    main()
