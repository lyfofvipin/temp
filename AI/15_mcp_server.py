"""
15 — MCP server (tools only — does NOT connect to Ollama).

This file exposes TOOLS (weather, calculator, fetch_url, company_lookup).
It is NOT an LLM. It does not talk to Ollama.

How it fits together:
  You → Cursor (MCP Host)
          ├── LLM  ← Ollama / Claude / GPT (configured in Cursor, separate)
          └── MCP Client → this file (tools via stdio)

DO NOT run `python 15_mcp_server.py` in a terminal for a chat.
MCP uses JSON-RPC over stdin/stdout — only an MCP host (Cursor) should start it.
Running it alone causes: "Invalid JSON: EOF while parsing"

Setup:
  pip install -r 15_mcp_requirements.txt
  ollama serve                    # if you want Ollama as Cursor's LLM (optional)

Cursor MCP config (~/.cursor/mcp.json):
  {
    "mcpServers": {
      "xyz-org-tools": {
        "command": "/home/vipikuma/my_data/temp/AI/ollama/.venv/bin/python",
        "args": ["/home/vipikuma/my_data/temp/AI/15_mcp_server.py"]
      }
    }
  }

Use the same Python venv where `mcp` and `requests` are installed.
Restart Cursor after editing mcp.json. Then ask in Cursor chat:
  "What is the weather in London?"
Cursor's LLM decides to call get_weather on this MCP server.

For Ollama + tools in one Python script (no Cursor), use 13_agent_demo.py or 14_agentic_demo.py.
"""

import re

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("xyz-org-tools")

ALLOWED_HOSTS = (
    "wttr.in",
    "api.github.com",
    "httpbin.org",
    "example.com",
)

COMPANY_KB = {
    "xyz org": "XYZ ORG is a fictional company used for AI training demos.",
    "vacation policy": "XYZ ORG offers 20 days paid leave per year.",
    "support email": "support@xyz-org.example",
}


@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city (live data from wttr.in)."""
    city = city.strip().replace(" ", "+")
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=15,
            headers={"User-Agent": "xyz-org-mcp/1.0"},
        )
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as exc:
        return f"Weather fetch failed: {exc}"


@mcp.tool()
def company_lookup(query: str) -> str:
    """Look up XYZ ORG company facts (local knowledge base)."""
    key = query.lower().strip()
    for topic, answer in COMPANY_KB.items():
        if topic in key or key in topic:
            return answer
    return "No company info found for that topic."


@mcp.tool()
def fetch_url(url: str) -> str:
    """Fetch a public URL (allowlisted domains only)."""
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        return "Error: URL must start with http:// or https://"

    host = url.split("/")[2].lower()
    if not any(host == allowed or host.endswith(f".{allowed}") for allowed in ALLOWED_HOSTS):
        return f"Error: host not allowlisted. Allowed: {', '.join(ALLOWED_HOSTS)}"

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "xyz-org-mcp/1.0"},
        )
        response.raise_for_status()
        text = response.text[:2000]
        return text + ("\n...[truncated]" if len(response.text) > 2000 else "")
    except requests.RequestException as exc:
        return f"URL fetch failed: {exc}"


@mcp.tool()
def calculator(expression: str) -> str:
    """Evaluate a math expression, e.g. 19 * 21 or 840 * 0.15."""
    expression = expression.strip()
    if not re.fullmatch(r"[\d\s+\-*/().]+", expression):
        return "Error: only numbers and + - * / ( ) allowed"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))  # noqa: S307 — demo only
    except Exception as exc:
        return f"Error: {exc}"


if __name__ == "__main__":
    mcp.run()
