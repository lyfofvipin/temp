"""
15 — Real MCP server (FastMCP).

Exposes the same tools as 15_mcp_demo.py on the Model Context Protocol.
Plug this into Cursor, Claude Desktop, or any MCP host.

Prerequisites:
  pip install mcp requests

Run:
  python 15_mcp_server.py

Cursor MCP config (~/.cursor/mcp.json) example:
  {
    "mcpServers": {
      "xyz-org-tools": {
        "command": "python",
        "args": ["/full/path/to/AI/15_mcp_server.py"]
      }
    }
  }
"""

import re

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("xyz-org-tools")

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
