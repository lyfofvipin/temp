"""
16 — LangChain basics (maps to your manual agents in 13/14).

Prerequisites:
  ollama pull llama3.2
  pip install -r 16_langchain_requirements.txt

Usage:
  python 16_langchain_demo.py basic
  python 16_langchain_demo.py chain
  python 16_langchain_demo.py tools
"""

import re
import sys

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

MODEL = "llama3.2"
MAX_TOOL_STEPS = 5


# ---------------------------------------------------------------------------
# Tools (same idea as 13_agent_demo.py — LangChain adds schema automatically)
# ---------------------------------------------------------------------------


@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression, e.g. 17 * 23 or 840 * 0.15."""
    expression = expression.strip()
    if not re.fullmatch(r"[\d\s+\-*/().]+", expression):
        return "Error: only numbers and + - * / ( ) allowed"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))  # noqa: S307 — demo only
    except Exception as exc:
        return f"Error: {exc}"


@tool
def company_lookup(query: str) -> str:
    """Look up XYZ ORG company facts."""
    kb = {
        "xyz org": "XYZ ORG is a fictional company used for AI training demos.",
        "vacation policy": "XYZ ORG offers 20 days paid leave per year.",
    }
    key = query.lower().strip()
    for topic, answer in kb.items():
        if topic in key or key in topic:
            return answer
    return "No company info found."


TOOLS = [calculator, company_lookup]
TOOLS_BY_NAME = {t.name: t for t in TOOLS}


def get_llm() -> ChatOllama:
    return ChatOllama(model=MODEL, temperature=0)


# ---------------------------------------------------------------------------
# 1. Basic — chatbot (one call, like flask-app)
# ---------------------------------------------------------------------------


def demo_basic() -> None:
    print("=" * 60)
    print("LangChain BASIC — one LLM call (chatbot)")
    print("=" * 60)

    llm = get_llm()
    response = llm.invoke([HumanMessage(content="Explain RAG in one sentence.")])
    print(response.content)
    print("\nSame idea as: flask-app /v1/chat (one shot, no tools)")


# ---------------------------------------------------------------------------
# 2. Chain — prompt template | llm
# ---------------------------------------------------------------------------


def demo_chain() -> None:
    print("=" * 60)
    print("LangChain CHAIN — prompt template | llm")
    print("=" * 60)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful teacher. Answer in 2 short sentences."),
            ("human", "Explain {topic} to a QA engineer."),
        ]
    )
    chain = prompt | get_llm()

    result = chain.invoke({"topic": "the difference between a chatbot and an agent"})
    print(result.content)
    print("\nLangChain wires: variables → prompt → model (LCEL pipe syntax)")


# ---------------------------------------------------------------------------
# 3. Tools — agent loop (like 13_agent_demo.py, LangChain parses tool_calls)
# ---------------------------------------------------------------------------


def demo_tools() -> None:
    print("=" * 60)
    print("LangChain TOOLS — bind_tools + loop (agent)")
    print("=" * 60)

    question = "What is 17 times 23?"
    print(f"Question: {question}\n")

    llm = get_llm().bind_tools(TOOLS)
    messages = [
        SystemMessage(
            content="You are a helpful assistant. Use tools for math and company facts."
        ),
        HumanMessage(content=question),
    ]

    for step in range(1, MAX_TOOL_STEPS + 1):
        print(f"--- Step {step} ---")
        response = llm.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            print(f"Final: {response.content}")
            print("\nSame idea as: 13_agent_demo.py (loop until answer)")
            return

        for call in response.tool_calls:
            name = call["name"]
            args = call["args"]
            print(f"Tool call: {name}({args})")
            tool_fn = TOOLS_BY_NAME.get(name)
            if tool_fn:
                result = tool_fn.invoke(args)
            else:
                result = f"Unknown tool: {name}"
            print(f"Result: {result}\n")
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))

    print("Stopped: max tool steps reached.")


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "basic"

    if mode == "basic":
        demo_basic()
    elif mode == "chain":
        demo_chain()
    elif mode == "tools":
        demo_tools()
    else:
        print("Usage: python 16_langchain_demo.py [basic|chain|tools]")
        sys.exit(1)


if __name__ == "__main__":
    main()
