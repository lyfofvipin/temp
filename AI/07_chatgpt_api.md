# OpenAI API Basics

The OpenAI API lets you add AI capabilities (text, images, audio, agents, and more) to your applications through HTTP requests or official SDKs.

## Setup

1. Sign up and create an API key in the dashboard.
2. Store it securely as an environment variable.
3. Never expose API keys in frontend code or public repositories.

Docs: https://developers.openai.com/api/docs/quickstart

## Chat completion API

The model is given a conversation and asked to "complete" it by generating the next assistant message.

```mermaid
flowchart LR
    APP[Your application] --> API[OpenAI API]
    API --> LLM[Language model]
    LLM --> API
    API --> APP
```

### Message roles

| Role | Purpose |
|------|---------|
| `system` | Instructions for model behavior |
| `user` | Messages from the end user |
| `assistant` | Previous AI responses |
| `tool` / `function` | Outputs from external tools |

### Typical use cases

- Customer support chatbots
- Virtual assistants
- Content generation
- Coding assistants
- Data extraction and summarization
- AI agents that call tools and APIs

## Conversation memory

A chatbot remembers by **storing previous messages and sending them again with every new request**.

### Without memory

```mermaid
sequenceDiagram
    participant U as User
    participant B as Bot

    U->>B: My name is Ravi.
    B-->>U: Nice to meet you.
    U->>B: What's my name?
    B-->>U: I don't know.
```

### With memory

```mermaid
sequenceDiagram
    participant U as User
    participant A as App
    participant API as OpenAI API

    U->>A: My name is Ravi.
    A->>API: [user: Ravi]
    API-->>A: Nice to meet you.
    A-->>U: reply

    U->>A: What's my name?
    A->>API: [user: Ravi, assistant: ..., user: name?]
    Note over A,API: Full history sent each request
    API-->>A: Your name is Ravi.
    A-->>U: reply
```

### Minimal Python pattern

```python
chat_history = []

while True:
    user = input("You: ")
    chat_history.append({"role": "user", "content": user})

    # Send chat_history to API
    bot_reply = "AI response here"

    chat_history.append({"role": "assistant", "content": bot_reply})
    print("Bot:", bot_reply)
```

## Local equivalent

Ollama's `/api/chat` works the same way — see `06_using_api.md`.
