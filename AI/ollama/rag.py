"""
Minimal RAG demo using Ollama (no GPU training required).

Prerequisites:
  ollama pull llama3.2
  ollama pull nomic-embed-text
  pip install requests
"""

import json
import math
from pathlib import Path

import requests

OLLAMA_URL = "http://localhost:11434"
CHAT_MODEL = "llama3.2"
EMBED_MODEL = "nomic-embed-text"
DATA_FILE = Path(__file__).resolve().parent / "data.json"


def embed(text: str) -> list[float]:
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["embedding"]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    return dot / (norm_a * norm_b + 1e-9)


def load_knowledge_base() -> list[dict]:
    records = json.loads(DATA_FILE.read_text())
    chunks = []
    for row in records:
        text = f"Q: {row['instruction']}\nA: {row['output']}"
        chunks.append({"text": text, "embedding": embed(text)})
    return chunks


def retrieve(question: str, chunks: list[dict], top_k: int = 2) -> list[str]:
    query_vec = embed(question)
    scored = [
        (cosine_similarity(query_vec, chunk["embedding"]), chunk["text"])
        for chunk in chunks
    ]
    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]


def ask(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
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


def main():
    print("Loading knowledge base and building embeddings...")
    chunks = load_knowledge_base()

    questions = [
        "What is XYZ ORG?",
        "What is RAG?",
        "What is the capital of France?",
    ]

    for question in questions:
        print(f"\nQuestion: {question}")
        retrieved = retrieve(question, chunks)
        print("Retrieved:")
        for item in retrieved:
            print(f"  - {item[:80]}...")
        answer = ask(question, retrieved)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
