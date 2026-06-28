from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import torch

app = FastAPI()

# 1. Initialize the Hugging Face model ONCE when the server starts
# Using HF "pipeline" abstracts away manual tokenization + forward pass steps
device = "cuda" if torch.cuda.is_available() else "cpu"
generator = pipeline("text-generation", model="distilgpt2", device=device)

# "text-generation": This is the Task Identifier. It tells Hugging Face exactly what kind of job you want to do. Hugging Face supports dozens of different AI pipelines (e.g., "sentiment-analysis", "translation", "audio-classification"). By passing "text-generation", it automatically knows it needs an auto-regressive language model that predicts the next word.

# 2. Define what the incoming request data should look like
class AIRequest(BaseModel):
    prompt: str

# 3. Create an API endpoint
@app.post("/generate")
def generate_text(request: AIRequest):
    # Run the local HF model
    result = generator(request.prompt, max_new_tokens=20)
    return {"response": result[0]["generated_text"]}