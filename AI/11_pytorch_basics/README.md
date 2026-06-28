# PyTorch & Hugging Face basics (for `train_model.py`)

Small scripts that explain the libraries used in `ollama/train_model.py`.

**`train_model.py` uses PyTorch**, not TensorFlow. Hugging Face `transformers` supports both backends, but LoRA training in this repo is PyTorch-only. TensorFlow/Keras is noted at the end for comparison.

## Setup

```bash
cd 11_pytorch_basics
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run scripts in order:

```bash
python 01_tensors.py
python 02_tokenizer.py
python 03_load_and_generate.py
python 04_datasets.py
# 05 is read-only — maps train_model.py line by line
```

## How each script maps to `train_model.py`

| Script | Concepts | Used in `train_model.py` |
|--------|----------|--------------------------|
| `01_tensors.py` | Tensors, shapes, `torch.no_grad()` | lines 44, 87–88 |
| `02_tokenizer.py` | `AutoTokenizer`, encode/decode | lines 40–42, 85, 98 |
| `03_load_and_generate.py` | `AutoModelForCausalLM`, `.generate()` | lines 44, 87–95 |
| `04_datasets.py` | `load_dataset`, `.map()` | lines 36–37 |
| `05_train_model_walkthrough.md` | LoRA, PEFT, SFTTrainer | lines 46–77 |

## Stack cheat sheet

| Package | Role |
|---------|------|
| **torch** | Tensors, GPU/CPU, training math |
| **transformers** | Load models & tokenizers from Hugging Face Hub |
| **datasets** | Load JSON/CSV as training data |
| **peft** | LoRA — train small adapters, not full model |
| **trl** | `SFTTrainer` — supervised fine-tuning helper |
| **accelerate** | Device placement (used internally by trainers) |

## Tools like Ollama for Hugging Face models

| Tool | What it does | Like Ollama? |
|------|--------------|--------------|
| **[Ollama](https://ollama.com)** | Run GGUF models locally with `ollama run` | Yes — simplest local runner |
| **[LM Studio](https://lmstudio.ai)** | Desktop app, download & chat with HF/GGUF models | Yes — GUI-first |
| **[llama.cpp](https://github.com/ggerganov/llama.cpp)** | C++ inference engine (Ollama uses similar ideas) | Engine, not a full app |
| **[LocalAI](https://localai.io)** | Open-source API server for many model formats | Yes — API gateway |
| **[text-generation-inference](https://github.com/huggingface/text-generation-inference)** | HF's production inference server | Server — needs GPU for big models |
| **[vLLM](https://github.com/vllm-project/vllm)** | Fast GPU inference server | Server — GPU-focused |
| **transformers (Python)** | `pipeline()` or `model.generate()` in a script | Library — you write the app |

**Practical answer:** For “pull a model and chat locally” like Ollama, use **Ollama**, **LM Studio**, or **LocalAI**. Many Ollama models originally come from Hugging Face (converted to GGUF). To run a **specific HF model as-is** (e.g. `distilgpt2`), use **transformers in Python** (`03_load_and_generate.py`) or LM Studio.

Ollama does **not** run arbitrary `transformers` checkpoints directly — models are usually converted to GGUF first.

## PyTorch vs TensorFlow (one paragraph)

| | PyTorch | TensorFlow |
|---|---------|------------|
| Style | Pythonic, dynamic graphs | Keras API + static graphs (TF 2.x is eager too) |
| In this repo | ✅ `train_model.py` | ❌ not used |
| Hugging Face | Primary backend for training | Supported for inference on some models |

For understanding `train_model.py`, learn **PyTorch basics + Hugging Face** — skip TensorFlow unless a job specifically requires it.
