"""
15 — MCP-style agent demo (simulated Host → Client → Server).

Shows the same agent loop as 14, but tools live on an MCP Server instead of
a hardcoded TOOLS dict. Proves MCP is a wiring change, not a new kind of AI.

Prerequisites:
  ollama pull llama3.2
  pip install requests

Usage:
  python 15_mcp_demo.py
  python 15_mcp_demo.py --compare
  python 15_mcp_demo.py --question "What is 19 times 21?"
"""

import argparse
import re

import requests

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3.2"
MAX_STEPS = 6

ALLOWED_HOSTS = ("wttr.in", "api.github.com", "httpbin.org", "example.com")

COMPANY_KB = {
    "xyz org": "XYZ ORG is a fictional company used for AI training demos.",
    "vacation policy": "XYZ ORG offers 20 days paid leave per year.",
    "support email": "support@xyz-org.example",
}


# ---------------------------------------------------------------------------
# MCP Server — exposes tools (like 15_mcp_server.py / GitLab MCP / Slack MCP)
# ---------------------------------------------------------------------------


class MCPServer:
    """Standalone tool provider. In production this runs as its own process."""

    def list_tools(self) -> list[dict]:
        return [
            {
                "name": "get_weather",
                "description": "Current weather for a city (uses internet via wttr.in)",
            },
            {
                "name": "company_lookup",
                "description": "Facts about XYZ ORG from local knowledge base",
            },
            {
                "name": "calculator",
                "description": "Math expressions, e.g. 19 * 21",
            },
            {
                "name": "fetch_url",
                "description": "Fetch allowlisted public URL (uses internet)",
            },
        ]

    def call_tool(self, name: str, arguments: str) -> str:
        name = name.lower().strip()
        if name == "get_weather":
            return self._get_weather(arguments)
        if name == "company_lookup":
            return self._company_lookup(arguments)
        if name == "calculator":
            return self._calculator(arguments)
        if name == "fetch_url":
            return self._fetch_url(arguments)
        return f"Unknown tool '{name}'. Available: get_weather, company_lookup, calculator, fetch_url"

    def _get_weather(self, city: str) -> str:
        city = city.strip().replace(" ", "+")
        try:
            r = requests.get(
                f"https://wttr.in/{city}?format=3",
                timeout=15,
                headers={"User-Agent": "mcp-demo/1.0"},
            )
            r.raise_for_status()
            return r.text.strip()
        except requests.RequestException as exc:
            return f"Weather fetch failed: {exc}"

    def _company_lookup(self, query: str) -> str:
        key = query.lower().strip()
        for topic, answer in COMPANY_KB.items():
            if topic in key or key in topic:
                return answer
        return "No company info found."

    def _calculator(self, expression: str) -> str:
        expression = expression.strip()
        if not re.fullmatch(r"[\d\s+\-*/().]+", expression):
            return "Error: only numbers and + - * / ( ) allowed"
        try:
            return str(eval(expression, {"__builtins__": {}}, {}))  # noqa: S307
        except Exception as exc:
            return f"Error: {exc}"

    def _fetch_url(self, url: str) -> str:
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            return "Error: URL must start with http:// or https://"
        host = url.split("/")[2].lower()
        if not any(host == a or host.endswith(f".{a}") for a in ALLOWED_HOSTS):
            return f"Error: host not allowlisted. Allowed: {', '.join(ALLOWED_HOSTS)}"
        try:
            r = requests.get(url, timeout=15, headers={"User-Agent": "mcp-demo/1.0"})
            r.raise_for_status()
            text = r.text[:1500]
            return text + ("\n...[truncated]" if len(r.text) > 1500 else "")
        except requests.RequestException as exc:
            return f"URL fetch failed: {exc}"


# ---------------------------------------------------------------------------
# MCP Client — host uses this to talk to the server (standard protocol in real MCP)
# ---------------------------------------------------------------------------


class MCPClient:
    def __init__(self, server: MCPServer):
        self.server = server

    def list_tools(self) -> list[dict]:
        return self.server.list_tools()

    def call_tool(self, name: str, arguments: str) -> str:
        print(f"  [MCP Client] → calling server tool: {name}")
        return self.server.call_tool(name, arguments)


# ---------------------------------------------------------------------------
# Agent Host — LLM loop (same idea as 13/14, tools via MCP Client)
# ---------------------------------------------------------------------------


def ollama_chat(messages: list[dict]) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"].strip()


def build_system_prompt(tools: list[dict]) -> str:
    lines = [f"- {t['name']} — {t['description']}" for t in tools]
    tool_block = "\n".join(lines)
    return f"""You are an agent. Tools are provided by an MCP server (not built into the model).

Available tools:
{tool_block}

When you need a tool, reply ONE line:
TOOL: tool_name | INPUT: input here

When done, reply ONE line:
ANSWER: your final answer

Do not invent weather, URLs, or company facts — use tools."""


def parse_line(text: str) -> tuple[str, str, str]:
    first = text.strip().split("\n")[0].strip()
    if first.upper().startswith("ANSWER:"):
        return "answer", "", first.split(":", 1)[1].strip()
    match = re.match(r"TOOL:\s*(\w+)\s*\|\s*INPUT:\s*(.+)", first, re.I)
    if match:
        return "tool", match.group(1).lower(), match.group(2).strip()
    return "unknown", "", text


def run_mcp_agent(question: str, client: MCPClient) -> None:
    tools = client.list_tools()
    print("MCP tools registered:")
    for t in tools:
        print(f"  • {t['name']}: {t['description']}")
    print()

    messages = [
        {"role": "system", "content": build_system_prompt(tools)},
        {"role": "user", "content": question},
    ]

    for step in range(1, MAX_STEPS + 1):
        print(f"--- Step {step} ---")
        raw = ollama_chat(messages)
        print(f"Model: {raw}\n")

        kind, name, payload = parse_line(raw)

        if kind == "answer":
            print(f"Final: {payload}")
            return

        if kind == "tool":
            result = client.call_tool(name, payload)
            print(f"  [MCP Server] result → {result[:200]}{'...' if len(result) > 200 else ''}\n")
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content": f"Tool result: {result}"})
            continue

        messages.append({"role": "assistant", "content": raw})
        messages.append(
            {"role": "user", "content": "Use TOOL: name | INPUT: ... or ANSWER: ... (one line)."}
        )

    print("Stopped: max steps reached.")


# ---------------------------------------------------------------------------
# Compare: file-14 style (direct TOOLS) vs MCP style
# ---------------------------------------------------------------------------


def run_direct_tools(question: str) -> None:
    """Same as 13/14 — tools hardcoded in the host script."""
    print("=" * 60)
    print("A) DIRECT TOOLS (like 14_agentic_demo.py)")
    print("=" * 60)
    print("Host calls TOOLS[name]() directly — no MCP layer.\n")

    direct = {
        "calculator": lambda x: MCPServer()._calculator(x),
        "company_lookup": lambda x: MCPServer()._company_lookup(x),
    }

    # Simple one-shot for demo: if math question, call calculator directly
    if "times" in question.lower() or "*" in question:
        expr = re.sub(r"what is (.+)\?", r"\1", question.lower())
        expr = expr.replace("times", "*").strip()
        result = direct["calculator"](expr)
        print(f"Host hardcoded logic → calculator({expr}) → {result}\n")
    else:
        result = direct["company_lookup"](question)
        print(f"Host hardcoded logic → company_lookup → {result}\n")


def run_compare(question: str) -> None:
    run_direct_tools(question)
    print("=" * 60)
    print("B) MCP TOOLS (like 15_mcp_demo.py)")
    print("=" * 60)
    print("Host → MCP Client → MCP Server → tool.\n")
    server = MCPServer()
    client = MCPClient(server)
    run_mcp_agent(question, client)


def main():
    parser = argparse.ArgumentParser(description="MCP-style agent demo")
    parser.add_argument(
        "--question",
        default="What is 19 times 21?",
        help="Question for the agent",
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="Show direct TOOLS vs MCP wiring",
    )
    args = parser.parse_args()

    if args.compare:
        run_compare(args.question)
        return

    print("=" * 60)
    print("MCP Agent Demo — Host → MCP Client → MCP Server → Ollama")
    print("=" * 60)
    print(f"Question: {args.question}\n")
    print("The LLM has no tools built in. MCP Server provides them.\n")

    server = MCPServer()
    client = MCPClient(server)
    run_mcp_agent(args.question, client)


if __name__ == "__main__":
    main()
