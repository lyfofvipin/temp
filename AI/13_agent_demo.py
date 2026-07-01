"""
Chatbot vs AI Agent — side-by-side demo (Ollama + requests).

Prerequisites:
  ollama pull llama3.2
  pip install requests

Usage:
  python 13_agent_demo.py chatbot
  python 13_agent_demo.py agent
"""

import re
import sys

import requests

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3.2"
MAX_AGENT_STEPS = 5

# ---------------------------------------------------------------------------
# Shared: one Ollama chat call
# ---------------------------------------------------------------------------


def ollama_chat(messages: list[dict]) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"].strip()


# ---------------------------------------------------------------------------
# Tools (only the agent can use these — your Python code runs them)
# ---------------------------------------------------------------------------

COMPANY_KB = {
    "xyz org": "XYZ ORG is a fictional company used for AI training demos.",
    "vacation policy": "XYZ ORG offers 20 days paid leave per year.",
    "support email": "support@xyz-org.example",
}


def tool_calculator(expression: str) -> str:
    expression = expression.strip()
    if not re.fullmatch(r"[\d\s+\-*/().]+", expression):
        return "Error: only numbers and + - * / ( ) allowed"
    try:
        result = eval(expression, {"__builtins__": {}}, {})  # noqa: S307 — demo only
        return str(result)
    except Exception as exc:
        return f"Error: {exc}"


def tool_company_lookup(query: str) -> str:
    key = query.lower().strip()
    for topic, answer in COMPANY_KB.items():
        if topic in key or key in topic:
            return answer
    return "No company info found for that topic."


TOOLS = {
    "calculator": tool_calculator,
    "company_lookup": tool_company_lookup,
}


# ---------------------------------------------------------------------------
# Mode 1: Normal chatbot — single LLM call, no tools
# ---------------------------------------------------------------------------

CHATBOT_SYSTEM = (
    "You are a helpful assistant. Answer briefly. "
    "You cannot run code or call external APIs."
)


def run_chatbot(question: str) -> None:
    print("=" * 60)
    print("MODE: Normal chatbot (1 LLM call, no tools)")
    print("=" * 60)
    print(f"Question: {question}\n")

    messages = [
        {"role": "system", "content": CHATBOT_SYSTEM},
        {"role": "user", "content": question},
    ]

    answer = ollama_chat(messages)
    print(f"Reply:\n{answer}\n")
    print("Note: On math or company-specific facts, the model may guess wrong.")


# ---------------------------------------------------------------------------
# Mode 2: AI agent — LLM + tools + loop
# ---------------------------------------------------------------------------

AGENT_SYSTEM = """You are an agent with tools. Follow these rules strictly.

Available tools:
- calculator — math expressions only, e.g. 17 * 23 or 840 * 0.15
- company_lookup — facts about XYZ ORG (policies, contact, what it is)

When you need a tool, reply with ONE line only:
TOOL: tool_name | INPUT: input here

When you have the final answer, reply with ONE line only:
ANSWER: your final answer here

Do not make up company facts or math — use tools when needed."""


def parse_agent_line(text: str) -> tuple[str, str, str]:
    """Return (kind, name_or_empty, payload). kind is 'tool', 'answer', or 'unknown'."""
    first_line = text.strip().split("\n")[0].strip()

    if first_line.upper().startswith("ANSWER:"):
        return "answer", "", first_line.split(":", 1)[1].strip()

    match = re.match(r"TOOL:\s*(\w+)\s*\|\s*INPUT:\s*(.+)", first_line, re.I)
    if match:
        return "tool", match.group(1).lower(), match.group(2).strip()

    return "unknown", "", text


def run_agent(question: str) -> None:
    print("=" * 60)
    print("MODE: AI agent (LLM + tools + loop)")
    print("=" * 60)
    print(f"Question: {question}\n")

    messages = [
        {"role": "system", "content": AGENT_SYSTEM},
        {"role": "user", "content": question},
    ]

    for step in range(1, MAX_AGENT_STEPS + 1):
        print(f"--- Step {step} ---")
        raw = ollama_chat(messages)
        print(f"Model: {raw}\n")

        kind, name, payload = parse_agent_line(raw)

        if kind == "answer":
            print(f"Final answer: {payload}")
            return

        if kind == "tool":
            if name not in TOOLS:
                tool_result = f"Unknown tool '{name}'. Use: {', '.join(TOOLS)}"
            else:
                tool_result = TOOLS[name](payload)
            print(f"Tool [{name}] → {tool_result}\n")

            messages.append({"role": "assistant", "content": raw})
            messages.append(
                {
                    "role": "user",
                    "content": f"Tool result for {name}: {tool_result}",
                }
            )
            continue

        # Model did not follow format — nudge once
        messages.append({"role": "assistant", "content": raw})
        messages.append(
            {
                "role": "user",
                "content": (
                    "Use format TOOL: name | INPUT: ... or ANSWER: ... on one line."
                ),
            }
        )

    print("Stopped: max agent steps reached.")


# ---------------------------------------------------------------------------
# Demo questions
# ---------------------------------------------------------------------------

DEMO_QUESTIONS = [
    "What is 17 times 23?",
    "What is XYZ ORG and what is their vacation policy?",
]


def main():
    mode = (sys.argv[1] if len(sys.argv) > 1 else "both").lower()

    if mode == "chatbot":
        for q in DEMO_QUESTIONS:
            run_chatbot(q)
            print()
    elif mode == "agent":
        for q in DEMO_QUESTIONS:
            run_agent(q)
            print()
    elif mode == "both":
        q = DEMO_QUESTIONS[0]
        run_chatbot(q)
        print()
        run_agent(q)
    else:
        print("Usage: python 13_agent_demo.py [chatbot|agent|both]")
        sys.exit(1)

if __name__ == "__main__":
    main()
