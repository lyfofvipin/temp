# Ollama in Cursor, VS Code, and Antigravity

How to use **local Ollama models** inside your editor — for chat, coding help, and alongside MCP tools like `15_mcp_server.py`.

## Prerequisites (all editors)

```bash
# Install Ollama: https://ollama.com
ollama serve
ollama pull llama3.2
curl http://localhost:11434/api/tags   # verify running
```

Default API: `http://localhost:11434`  
OpenAI-compatible endpoint: `http://localhost:11434/v1`

---

## Cursor

Cursor can use Ollama in **two separate ways** — do not confuse them:

| Use | What it is | Config |
|-----|------------|--------|
| **A. Chat / Composer LLM** | Which model **thinks** | Cursor Settings → Models |
| **B. MCP tools** | Weather, calculator, etc. | `~/.cursor/mcp.json` → `15_mcp_server.py` |

MCP gives **tools only** — see `15_mcp.md`. For Ollama as the **brain**:

### Option 1 — Cursor Models settings (recommended)

1. Open **Cursor Settings** → **Models**
2. Look for **Ollama** or **Local / OpenAI-compatible**
3. Base URL: `http://localhost:11434/v1`
4. Model name: `llama3.2` (must match `ollama list`)
5. Select that model in the chat **model picker**

UI labels change between Cursor versions — search settings for “Ollama” or “override OpenAI base URL”.

### Option 2 — OpenAI-compatible override

Some setups route through OpenAI-compatible mode:

| Field | Value |
|-------|--------|
| Base URL | `http://localhost:11434/v1` |
| API key | `ollama` (any placeholder — Ollama ignores it) |
| Model | `llama3.2` |

### MCP tools + Ollama brain together

```json
// ~/.cursor/mcp.json — tools only
{
  "mcpServers": {
    "xyz-org-tools": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/AI/15_mcp_server.py"]
    }
  }
}
```

- **LLM:** Ollama via Settings → Models  
- **Tools:** MCP server  
- **Host (Cursor)** connects them — same loop as `14_agentic_demo.py`

Restart Cursor after changing MCP config.

---

## VS Code

VS Code does not ship with a built-in LLM. Use an **extension**.

### Continue (recommended)

1. Install **Continue** from the marketplace  
2. Open Continue config (`~/.continue/config.yaml` or via extension UI)  
3. Add Ollama:

```yaml
models:
  - name: Llama 3.2 local
    provider: ollama
    model: llama3.2

# Or OpenAI-compatible style:
  - name: Ollama via OpenAI API
    provider: openai
    model: llama3.2
    apiBase: http://localhost:11434/v1
    apiKey: ollama
```

4. Open Continue panel → chat or inline edit with local model

Docs: https://docs.continue.dev/

### Other VS Code options

| Extension | Role |
|-----------|------|
| **Continue** | Chat + autocomplete with Ollama |
| **Cline** | Agentic coding, supports Ollama endpoint |
| **Ollama** (community) | Quick run/pull models from sidebar |

### VS Code + your repo

| Task | How |
|------|-----|
| Run Flask gateway | Terminal: `cd flask-app && python app.py` |
| Run Streamlit app | Terminal: `cd streamlit-app && streamlit run app.py` |
| Run agent demos | `python 13_agent_demo.py agent` |
| MCP server | Configured in Cursor; VS Code uses Continue instead |

---

## Google Antigravity

Antigravity is a **VS Code–based IDE** with a built-in **cloud agent** (Gemini, Claude, etc.). The **native model picker** is usually a **fixed cloud list** — you often **cannot** point it directly at `localhost:11434` like a custom dropdown entry.

You still have **practical ways** to use Ollama:

### Option 1 — Continue or Cline extension (best for local LLM chat)

Antigravity supports extensions via **OpenVSX** (VS Code fork):

1. Install **Continue** or **Cline** from OpenVSX  
2. Point at Ollama:

```yaml
# Continue — apiBase example
apiBase: http://localhost:11434/v1
model: llama3.2
```

Use **Antigravity’s cloud agent** for heavy multi-file tasks; use **Continue/Cline + Ollama** for free local chat/completion.

### Option 2 — Terminal + your Python scripts

Antigravity’s integrated terminal runs your repo like any IDE:

```bash
ollama serve
python 13_agent_demo.py agent
python 14_agentic_demo.py
streamlit run streamlit-app/app.py
```

The IDE runs code; **Python + Ollama** do the AI work.

### Option 3 — MCP for tools

MCP config location may differ from Cursor — often under Gemini/Antigravity config paths (e.g. `~/.gemini/antigravity/mcp_config.json` on some setups). Same idea as `15_mcp_server.py`:

```json
{
  "mcpServers": {
    "xyz-org-tools": {
      "command": "python",
      "args": ["/full/path/to/AI/15_mcp_server.py"]
    }
  }
}
```

Check Antigravity docs for the exact MCP file path for your version.

### Option 4 — MCP bridge to Ollama (advanced)

Community **ollama-mcp-server** packages expose Ollama itself as an MCP tool for hosts that support MCP — separate from your custom `15_mcp_server.py` tools.

---

## Comparison table

| Editor | Local Ollama as chat LLM | MCP tools | Easiest path |
|--------|--------------------------|-----------|--------------|
| **Cursor** | Settings → Models / Ollama | `~/.cursor/mcp.json` | Models + MCP |
| **VS Code** | Continue / Cline extension | Usually via agent extensions | Continue |
| **Antigravity** | Continue / Cline (not native picker) | MCP config (path varies) | Extension + terminal |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Connection refused | Run `ollama serve` |
| Model not found | `ollama pull llama3.2` |
| Slow responses | Use smaller model (`llama3.2:1b`) or GPU |
| MCP JSON error in terminal | Do not run `15_mcp_server.py` manually — let the IDE start it |
| Cursor uses cloud model | Check model **picker** in chat — select Ollama |
| Antigravity no local option | Use Continue extension or terminal scripts |

---

## Related files

| File | Topic |
|------|-------|
| `15_mcp.md` | MCP vs LLM — tools vs brain |
| `06_using_api.md` | Ollama HTTP API |
| `flask-app/` | Web UI gateway (Flask) |
| `streamlit-app/` | Web UI gateway (Streamlit) |
| `13_agent_demo.py` | Ollama + tools in one script (no IDE needed) |

## One-line summary

**Ollama runs as a local server; your editor connects via Models settings (Cursor), Continue/Cline (VS Code / Antigravity), or your own Python scripts — MCP adds tools on top, not the LLM itself.**
