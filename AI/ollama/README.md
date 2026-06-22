# Ollama Lab (CPU only)

Scripts for learning training and RAG on a CPU laptop.

## Quick start

```bash
cd ollama
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python load_data.py      # preview training data
python train_model.py    # LoRA training on CPU
python rag.py            # RAG with Ollama (needs ollama pull nomic-embed-text)
```

## Files

| File | Purpose |
|------|---------|
| `data.json` | Training + RAG knowledge base |
| `train_model.py` | LoRA fine-tuning on distilgpt2 (CPU) |
| `rag.py` | Retrieval-augmented generation with Ollama |
| `load_data.py` | Preview formatted training text |
| `../06_using_api.md` | Ollama HTTP API reference |

Training writes to `outputs/` and `lora_adapter/` (both gitignored — delete anytime to start fresh).

## Training vs RAG

| Approach | Script | Changes weights? |
|----------|--------|------------------|
| LoRA training | `train_model.py` | Yes (small adapter) |
| RAG | `rag.py` | No |
| System prompt | `../Modelfile.txt` | No |

For company facts without retraining, use **RAG** (`rag.py`).
