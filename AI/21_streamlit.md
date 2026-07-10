# Streamlit — AI web apps (theory)

**Streamlit** turns Python scripts into **web apps** with minimal HTML/CSS/JS. Popular for **ML and GenAI demos**, internal tools, and prototypes.

Compare with your **`flask-app/`** — same job (Ollama chat UI), different style.

## Flask vs Streamlit

| | **Flask** (`flask-app/`) | **Streamlit** (`streamlit-app/`) |
|---|--------------------------|----------------------------------|
| Style | Routes + templates + JS | Pure Python UI calls |
| HTML/CSS | You write (or templates) | Streamlit renders for you |
| API + UI | Easy to split (REST + dashboard) | UI-first; API is optional |
| Best for | Production APIs, custom frontends | Fast AI demos, data apps |
| Learning curve | Web basics helpful | Python only — very fast |

```mermaid
flowchart LR
    subgraph flask [Flask app]
        R[Routes] --> T[templates/index.html]
        T --> JS[app.js]
        JS --> API[/v1/chat]
        API --> O[Ollama]
    end

    subgraph st [Streamlit app]
        PY[app.py UI code] --> O2[Ollama]
    end
```

Both call the same Ollama API — see `06_using_api.md`.

## Core Streamlit ideas

| Concept | Code | Purpose |
|---------|------|---------|
| Run app | `streamlit run app.py` | Starts local web server |
| Widgets | `st.text_input`, `st.selectbox` | User input |
| Buttons | `st.button` | Actions |
| Chat | `st.chat_message`, `st.chat_input` | ChatGPT-style UI |
| Session state | `st.session_state` | Remember chat history |
| Layout | `st.columns`, `st.sidebar` | Page structure |

### Minimal hello

```python
import streamlit as st

st.title("My AI App")
name = st.text_input("Your name")
if st.button("Greet"):
    st.write(f"Hello, {name}!")
```

Run: `streamlit run app.py` → opens browser at `http://localhost:8501`

## Mapping to your GenAI repo

| Pattern | Flask | Streamlit |
|---------|-------|-----------|
| Chatbot | `/v1/chat` + `index.html` | `st.chat_input` + Ollama POST |
| Model picker | `<select>` in HTML | `st.selectbox` |
| Show response | `div` + JS | `st.markdown` / `st.write` |
| History | JS `chatHistory` | `st.session_state.messages` |

Your **`streamlit-app/app.py`** mirrors the Flask gateway as a single Python file.

## When companies use Streamlit

| Use case | Why Streamlit |
|----------|---------------|
| Internal RAG demo | Ship in hours |
| QA / PM test UI for agents | No frontend team needed |
| Data + LLM dashboards | Charts + chat in one file |
| Hackathons & PoCs | Fastest Python UI |

Production customer-facing apps often move to **Flask/FastAPI + React** later — Streamlit wins for **speed of learning and demos**.

## Learning path

1. Read this file  
2. Run the demo:

```bash
pip install -r streamlit-app/requirements.txt
ollama pull llama3.2
cd streamlit-app
streamlit run app.py
```

3. Compare with `flask-app/` side by side  
4. Try adding: sidebar model info, clear chat button, file upload for RAG (stretch goal)

## Common widgets for AI apps

```python
st.selectbox("Model", models)          # model list
st.text_area("Prompt", height=150)     # long prompt
st.chat_input("Ask…")                  # chat bar
st.spinner("Thinking…")                # loading state
st.expander("Debug")                   # hide JSON
st.sidebar.header("Settings")          # settings panel
```

## Streamlit vs Gradio

| | Streamlit | Gradio |
|---|-----------|--------|
| Focus | General data + AI apps | ML model demos |
| HF integration | Good | Excellent (HF Spaces) |
| This repo | ✅ `streamlit-app/` | Not included |

## Related files

| File | Topic |
|------|-------|
| `streamlit-app/app.py` | Ollama chat demo |
| `flask-app/app.py` | Same idea with Flask |
| `06_using_api.md` | Ollama API reference |
| `20_ollama_in_ide.md` | Ollama in your editor |

## One-line summary

**Streamlit = Python-only web UI for AI apps — fastest way to demo what you built with Ollama, RAG, and agents.**
