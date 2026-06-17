Start Ollama Server

Usually Ollama starts automatically.

Verify:

ollama serve

Default API URL:

http://localhost:11434

Understanding Ollama APIs

Common endpoints:

Endpoint	    Purpose
/api/generate	Generate text
/api/chat	    Chat conversations
/api/tags   	List models
/api/show	    Model details


List Available Models
Request

Method:
GET
URL:
http://localhost:11434/api/tags




Example 2: Text Generation API
Endpoint
POST http://localhost:11434/api/generate
Headers
Content-Type: application/json
Request Body

Select:

Body → Raw → JSON
{
  "model": "llama3.2",
  "prompt": "Explain machine learning in simple terms.",
  "stream": false
}


Chat API

The Chat API maintains conversation structure.

Endpoint
POST http://localhost:11434/api/chat
Request Body
{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "What is Artificial Intelligence?"
    }
  ],
  "stream": false
}



Multi-Turn Conversation
{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "My name is John."
    },
    {
      "role": "assistant",
      "content": "Nice to meet you, John! How can I help you today?"
    },
    {
      "role": "user",
      "content": "What is my name?"
    }
  ],
  "stream": false
}


Model Information
Endpoint
POST http://localhost:11434/api/show
Request Body
{
  "name": "llama3.2"
}

