"""
14 — Agentic AI demo: multi-step goal + internet tools (Ollama + requests).

The LLM has NO internet by itself. Tools in this file use requests to fetch live data.

Prerequisites:
  ollama pull llama3.2
  pip install requests

Usage:
  python 14_agentic_demo.py
  python 14_agentic_demo.py --goal "Your multi-part goal here"
"""

import argparse
import re

import requests

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3.2"
MAX_STEPS = 8

# Allowlisted hosts for fetch_url (demo safety — expand carefully in production)
ALLOWED_HOSTS = (
    "wttr.in",
    "api.github.com",
    "httpbin.org",
    "example.com",
)

DEFAULT_GOAL = (
    "I am planning time off. Check the current weather in London, "
    "look up XYZ ORG vacation policy from company data, "
    "and give me a short summary I can use to decide on a 5-day trip."
)

# ---------------------------------------------------------------------------
# Internet + local tools (Python runs these — not Ollama)
# ---------------------------------------------------------------------------

COMPANY_KB = {
    "xyz org": "XYZ ORG is a fictional company used for AI training demos.",
    "vacation policy": "XYZ ORG offers 20 days paid leave per year.",
    "support email": "support@xyz-org.example",
}


def tool_get_weather(city: str) -> str:
    """Live weather via wttr.in — no API key required."""
    city = city.strip().replace(" ", "+")
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=15,
            headers={"User-Agent": "agentic-demo/1.0"},
        )
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as exc:
        return f"Weather fetch failed: {exc}"


def tool_fetch_url(url: str) -> str:
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
            headers={"User-Agent": "agentic-demo/1.0"},
        )
        response.raise_for_status()
        text = response.text[:2000]
        return text + ("\n...[truncated]" if len(response.text) > 2000 else "")
    except requests.RequestException as exc:
        return f"URL fetch failed: {exc}"


def tool_company_lookup(query: str) -> str:
    key = query.lower().strip()
    for topic, answer in COMPANY_KB.items():
        if topic in key or key in topic:
            return answer
    return "No company info found for that topic."


def tool_calculator(expression: str) -> str:
    expression = expression.strip()
    if not re.fullmatch(r"[\d\s+\-*/().]+", expression):
        return "Error: only numbers and + - * / ( ) allowed"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))  # noqa: S307 — demo only
    except Exception as exc:
        return f"Error: {exc}"


TOOLS = {
    "get_weather": tool_get_weather,
    "fetch_url": tool_fetch_url,
    "company_lookup": tool_company_lookup,
    "calculator": tool_calculator,
}

TOOL_HELP = """
- get_weather — city name, e.g. London (uses internet)
- fetch_url — full URL, e.g. https://api.github.com/zen (uses internet)
- company_lookup — XYZ ORG facts (local data)
- calculator — math expression (local)
""".strip()


# ---------------------------------------------------------------------------
# Ollama + agentic loop
# ---------------------------------------------------------------------------


def ollama_chat(messages: list[dict]) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"].strip()


AGENTIC_SYSTEM = f"""You are an autonomous assistant working toward a GOAL.
You may take multiple steps and use tools until the goal is complete.

{TOOL_HELP}

Rules:
- Work step by step toward the GOAL.
- Use tools when you need live or company-specific facts. Do not invent weather or policy data.
- When the goal is fully handled, reply with ONE line:
  DONE: your final summary for the user

When you need a tool, reply with ONE line only:
TOOL: tool_name | INPUT: input here

Examples:
TOOL: get_weather | INPUT: London
TOOL: company_lookup | INPUT: vacation policy
DONE: Here is my summary..."""


def parse_line(text: str) -> tuple[str, str, str]:
    first = text.strip().split("\n")[0].strip()

    if first.upper().startswith("DONE:"):
        return "done", "", first.split(":", 1)[1].strip()

    match = re.match(r"TOOL:\s*(\w+)\s*\|\s*INPUT:\s*(.+)", first, re.I)
    if match:
        return "tool", match.group(1).lower(), match.group(2).strip()

    return "unknown", "", text


def run_agentic(goal: str) -> None:
    print("=" * 60)
    print("Agentic AI demo — goal + loop + tools + internet")
    print("=" * 60)
    print(f"Goal: {goal}\n")
    print("Note: Ollama has no internet. Python tools fetch live data.\n")

    messages = [
        {"role": "system", "content": AGENTIC_SYSTEM},
        {"role": "user", "content": f"GOAL: {goal}"},
    ]

    for step in range(1, MAX_STEPS + 1):
        print(f"--- Step {step} ---")
        raw = ollama_chat(messages)
        print(f"Model: {raw}\n")

        kind, name, payload = parse_line(raw)

        if kind == "done":
            print("=" * 60)
            print("FINAL REPORT")
            print("=" * 60)
            print(payload)
            return

        if kind == "tool":
            if name not in TOOLS:
                result = f"Unknown tool '{name}'. Available: {', '.join(TOOLS)}"
            else:
                result = TOOLS[name](payload)
            print(f"Tool [{name}] → {result[:300]}{'...' if len(result) > 300 else ''}\n")

            messages.append({"role": "assistant", "content": raw})
            messages.append(
                {"role": "user", "content": f"Tool result ({name}): {result}\nContinue toward the GOAL."}
            )
            continue

        messages.append({"role": "assistant", "content": raw})
        messages.append(
            {
                "role": "user",
                "content": "Reply with TOOL: name | INPUT: ... or DONE: summary (one line).",
            }
        )

    print("Stopped: max steps reached without DONE.")


def main():
    parser = argparse.ArgumentParser(description="Agentic AI demo with internet tools")
    parser.add_argument("--goal", default=DEFAULT_GOAL, help="Multi-step goal for the agent")
    args = parser.parse_args()
    run_agentic(args.goal)


if __name__ == "__main__":
    main()
