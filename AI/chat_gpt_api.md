OpenAI API Basics:
The OpenAI API lets you add AI capabilities (text, images, audio, agents, and more) to your applications through HTTP requests or official SDKs.

Create an API key
* Sign up and create an API key in the dashboard.
* Store it securely as an environment variable.
* Never expose API keys in frontend code or public repositories.

For More:
https://developers.openai.com/api/docs/quickstart


Chat completion APIs:
The model is given a conversation and asked to "complete" it by generating the next assistant message.

Conversation structure commonly includes:
* system – instructions for the model's behavior.
* user – messages from the end user.
* assistant – previous AI responses.
* tool/function – outputs from external tools (depending on the API).

Typical use cases:
* Customer support chatbots
* Virtual assistants
* Content generation
* Coding assistants
* Data extraction and summarization
* AI agents that call tools and APIs


This is usually the most important concept.
How does ChatGPT remember what you said earlier?

A chatbot remembers by storing previous messages and sending them again with every new request.

Without memory:
```
User: My name is Ravi.
Bot: Nice to meet you.
```

```
User: What's my name?
Bot: I don't know.
```

With memory:

```
User: My name is Ravi.
Bot: Nice to meet you.

User: What's my name?
Bot: Your name is Ravi.
```

Visual explanation:

```
Conversation History

User: My name is Ravi
Bot: Nice to meet you

User: What's my name?
```

How they are sent:
```
[
  User: My name is Ravi
  Bot: Nice to meet you
  User: What's my name?
]
```


Sample:

```
chat_history = []

while True:
    user = input("You: ")

    chat_history.append(
        {"role": "user", "content": user}
    )

    # Send chat_history to AI

    bot_reply = "AI response here"

    chat_history.append(
        {"role": "assistant", "content": bot_reply}
    )

    print("Bot:", bot_reply)
```

