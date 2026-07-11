# GenAI Learning Lab — personal notes & runnable demos

A numbered learning path from **LLM basics** → **APIs** → **RAG** → **agents** → **MCP** → **LangChain** → **multimodal** — with local **Ollama**, **Hugging Face**, and small web apps (**Flask** + **Streamlit**).

Built while transitioning from **QA** to **applied GenAI development**. Every file is meant to be read, run, and blogged about.

---

## What is GenAI?

**Generative AI (GenAI)** = AI that **creates** new content (text, images, code, video) instead of only classifying data.

| Traditional ML | GenAI |
|----------------|-------|
| “Is this spam?” | “Write a reply to this email” |
| Fixed labels | Open-ended language / media |
| Often tabular data | Text, images, multimodal |

**NLP** (Natural Language Processing) is the broader field; this repo focuses on the **LLM / GenAI** branch — see `19_nlp.md`.

### The one rule (everything in this repo)

**The model only reads and writes text.** Tools, APIs, browsers, and MCP servers **act in the world** — the host app connects brain + hands. See `15_mcp.md`.

---

## Quick start

```bash
# Local LLM
ollama serve
ollama pull llama3.2

# Flask chat UI
cd flask-app && pip install flask requests && python app.py
# → http://localhost:8000

# Streamlit chat UI
cd streamlit-app && pip install -r requirements.txt && streamlit run app.py
# → http://localhost:8501

# Agent demo
python 13_agent_demo.py agent
```

---

## Learning path (numbered files)

### Foundations

| # | File | Topic |
|---|------|-------|
| 01 | `01_trainning_inference.md` | Training vs inference |
| 02 | `02_Tokens_embeddings.md` | Tokens, embeddings |
| 03 | `03_prompts.md` | Prompt design |
| 04 | `04_llm.md` | How LLMs work |
| 05 | `05_index.html` | Ollama lecture (HTML) |
| 19 | `19_nlp.md` | NLP theory — names what you learned |

### APIs & local models

| # | File | Topic |
|---|------|-------|
| 06 | `06_using_api.md` | Ollama HTTP API |
| 07 | `07_chatgpt_api.md` | OpenAI API basics |
| 08 | `08_chatgpt_api_uses.py` | OpenAI SDK vs requests |
| 09 | `09_using_gemini_api.py` | Gemini SDK vs requests |
| 20 | `20_ollama_in_ide.md` | Ollama in Cursor / VS Code / Antigravity |

### Apps & gateways

| Folder / file | Topic |
|---------------|-------|
| `flask-app/` | Chatbot gateway (Flask + HTML/JS) |
| `streamlit-app/` | Chatbot gateway (Streamlit) — see `21_streamlit.md` |
| `12_hg_model_bot.py` | Hugging Face text API (FastAPI) |

### RAG, training, PyTorch

| # | File / folder | Topic |
|---|---------------|-------|
| 10 | `10_rag.md` + `ollama/rag.py` | RAG |
| 11 | `11_pytorch_basics/` | PyTorch/HF for `train_model.py` |
| 12 | `12_lora.html` | LoRA lecture |
| `ollama/train_model.py` | LoRA fine-tuning (CPU) |

### Agents & orchestration

| # | File | Topic |
|---|------|-------|
| 13 | `13_ai_agents.md` + `13_agent_demo.py` | Chatbot vs agent |
| 14 | `14_agentic_ai.md` + `14_agentic_demo.py` | Agentic AI + internet tools |
| 15 | `15_mcp.md` + `15_mcp_server.py` | MCP tools for Cursor |
| 16 | `16_langchain.md` + `16_langchain_demo.py` | LangChain glue layer |

### Multimodal (HF)

| # | File | Topic |
|---|------|-------|
| 17 | `17_hf_image_demo.py` | Text → image |
| 18 | `18_hf_multimodal.md` | Theory |
| 18 | `18_hf_image_to_text_demo.py` | Image → text (caption / OCR) |
| 18 | `18_hf_video_demo.py` | Text → video (GPU recommended) |

### UI frameworks

| # | File | Topic |
|---|------|-------|
| 21 | `21_streamlit.md` | Streamlit for AI web apps |
| 22 | `22_vector_db.md` + `22_vector_db_demo.py` | Vector databases (Chroma) |
| 23 | `23_pdf_rag.md` + `23_pdf_rag_demo.py` | PDF / document RAG |
| 24 | `24_n8n_automation.md` | AI automation with n8n (free, self-hosted) |

---

## Concept ladder (what you learned)

```
Chatbot        → one LLM call                    (flask-app, streamlit-app)
RAG            → retrieve docs, then answer      (10, ollama/rag.py)
Agent          → loop + tools                    (13)
Agentic AI     → big goal + many steps + web     (14)
MCP            → standard tool plug-ins          (15)
LangChain      → framework for the same patterns (16)
NLP            → the field name for all of it    (19)
```

---

## What companies want in a GenAI developer (2025–2026)

Typical **applied GenAI / LLM engineer** role — not research PhD:

| Skill area | What employers ask for | Your repo evidence |
|------------|------------------------|-------------------|
| **LLM basics** | Tokens, context, inference | 01–04, 19 |
| **Prompting** | System prompts, few-shot | 03, RAG system prompts |
| **API integration** | OpenAI, Gemini, Ollama | 06–09, flask-app |
| **RAG** | Embeddings, retrieval, chunking | 10, rag.py |
| **Agents** | Tool loops, guardrails | 13, 14 |
| **Python** | FastAPI/Flask, scripts | 12, flask-app, streamlit-app |
| **Vector / search** | pgvector, Pinecone, Chroma | Concept in 10 (manual cosine) |
| **Evaluation / QA mindset** | Hallucination tests, edge cases | 13 QA checklist, RAG tests |
| **MCP / tool standards** | Cursor, enterprise integrations | 15 |
| **Frameworks** | LangChain, LangGraph | 16 |
| **Local + cloud** | Ollama dev, cloud prod | Whole repo |

### Job titles you can realistically target

- Applied GenAI Developer  
- LLM Application Engineer  
- AI Integration Engineer  
- GenAI QA / AI Quality Engineer (strong fit from QA background)  
- RAG Engineer (with more vector-DB practice)

---

## What you can say you are capable of

After working through this repo, you can honestly claim:

- Explain **training vs inference**, **RAG vs fine-tuning vs prompting**
- Build a **local chatbot** with Ollama (Flask or Streamlit)
- Call **OpenAI and Gemini** APIs (SDK and raw HTTP)
- Implement a **manual agent loop** with tools and optional internet
- Explain **MCP** (host, LLM, server) and run `15_mcp_server.py` in Cursor
- Run **RAG** over a JSON knowledge base
- Read **train_model.py** at a high level (LoRA, HF, PyTorch basics)
- Use **LangChain** for prompts, chains, and tool binding
- Know when to use **image / OCR / video** HF pipelines (17–18)
- Connect **Ollama to Cursor / VS Code** (20)
- **Test** LLM apps like a QA — edge cases, hallucinations, tool failures

You are an **applied GenAI builder**, not an ML research scientist — and that is what most teams hire.

---

## Repo layout

```
AI/
├── 01–24 numbered theory + demos
├── flask-app/          # Flask Ollama gateway + dashboard
├── streamlit-app/      # Streamlit Ollama chat
├── ollama/             # RAG, LoRA training, data.json
├── 11_pytorch_basics/  # PyTorch/HF mini lessons
└── README.md           # this file
```

---

## Suggested blog posts from this repo

1. “I built the same Ollama gateway in Flask vs Streamlit”  
2. “Chatbot vs agent vs agentic — explained with Python”  
3. “MCP is USB for AI tools (no model inside the server)”  
4. “RAG from scratch without a vector database”  
5. “From QA to GenAI — what transferred and what I had to learn”  

---

## What to learn next

- [ ] PDF RAG Streamlit UI — wrap `23_pdf_rag_demo.py`
- [ ] Complete n8n workflows (`24_n8n_automation.md` checklist)
- [ ] Streaming responses (SSE) in Flask/Streamlit
- [ ] LangGraph for multi-step agentic workflows
- [ ] Evals — golden questions + expected answers
- [ ] Dockerize flask-app or streamlit-app
- [ ] One portfolio project end-to-end (RAG + agent + UI + tests)

---

## License & notes

- Learning material — add a LICENSE before publishing publicly  
- Never commit API keys; use environment variables  
- `train_model.py` and video gen demos are CPU/GPU sensitive — see file headers  

**Author path:** QA engineer → GenAI practitioner via hands-on labs, not theory-only courses.
