"""
Vector DB demo — Chroma + Ollama embeddings.

Compare with ollama/rag.py (manual list + cosine similarity).
This does the same retrieval using a persistent vector database.

Prerequisites:
  ollama pull nomic-embed-text
  pip install -r 22_vector_db_requirements.txt
"""

from __future__ import annotations

from pathlib import Path

import chromadb
import requests
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
DB_PATH = Path(__file__).resolve().parent / "chroma_demo_db"
COLLECTION = "xyz_org_kb"


class OllamaEmbedding(EmbeddingFunction[Documents]):
    """Embed text via Ollama /api/embeddings."""

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


DOCS = [
    {
        "id": "leave",
        "text": "XYZ ORG offers 20 days paid leave per year.",
        "metadata": {"topic": "hr"},
    },
    {
        "id": "rag",
        "text": "RAG retrieves relevant documents before the LLM generates an answer.",
        "metadata": {"topic": "ai"},
    },
    {
        "id": "embeddings",
        "text": "Embeddings turn text into vectors so systems can search by meaning.",
        "metadata": {"topic": "ai"},
    },
]

QUERIES = [
    "What is the leave policy?",
    "How many days off do employees get?",  # semantic — no word "leave"
    "What is RAG?",
]


def main() -> None:
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_or_create_collection(
        name=COLLECTION,
        embedding_function=OllamaEmbedding(),
    )

    if collection.count() == 0:
        print("Indexing documents into Chroma...")
        collection.add(
            ids=[d["id"] for d in DOCS],
            documents=[d["text"] for d in DOCS],
            metadatas=[d["metadata"] for d in DOCS],
        )
    else:
        print(f"Using existing index ({collection.count()} docs in {DB_PATH})")

    print("\n--- Semantic search (vector DB) ---\n")
    for question in QUERIES:
        results = collection.query(query_texts=[question], n_results=1)
        top_doc = results["documents"][0][0]
        distance = results["distances"][0][0]
        meta = results["metadatas"][0][0]
        print(f"Q: {question}")
        print(f"  → {top_doc}")
        print(f"    (distance={distance:.4f}, topic={meta['topic']})\n")

    print("--- Filtered search: HR docs only ---\n")
    hr_results = collection.query(
        query_texts=["time off benefits"],
        n_results=1,
        where={"topic": "hr"},
    )
    print(f"Q: time off benefits (hr filter only)")
    print(f"  → {hr_results['documents'][0][0]}\n")


if __name__ == "__main__":
    main()
