"""
Gemini API — SDK vs raw requests (same call, two ways).

Setup:
  pip install google-genai requests
  export GEMINI_API_KEY="your-key"   # or GOOGLE_API_KEY

Get a key: https://aistudio.google.com/apikey
"""

import os

# Use the same model as your working curl call.
# gemini-2.0-flash-lite may show limit: 0 on free tier for some accounts.
MODEL = "gemini-flash-latest"
PROMPT = "Explain what an API gateway does in two sentences."

# --- Option 1: Official SDK (active) ---
from google import genai

client = genai.Client()  # reads GEMINI_API_KEY or GOOGLE_API_KEY from env

response = client.models.generate_content(
    model=MODEL,
    contents=PROMPT,
)

print(response.text)


# --- Option 2: Same call with requests (uncomment to compare) ---
# import requests
#
# api_key = os.environ.get("GEMINI_API_KEY") or os.environ["GOOGLE_API_KEY"]
# url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
#
# response = requests.post(
#     url,
#     headers={
#         "Content-Type": "application/json",
#         "X-goog-api-key": api_key,
#     },
#     json={
#         "contents": [
#             {
#                 "parts": [{"text": PROMPT}]
#             }
#         ]
#     },
#     timeout=120,
# )
# response.raise_for_status()
# data = response.json()
#
# print(data["candidates"][0]["content"]["parts"][0]["text"])


# --- Option 3: Same call with curl (for terminal demo) ---
# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
#   -H "Content-Type: application/json" \
#   -H "X-goog-api-key: $GEMINI_API_KEY" \
#   -X POST \
#   -d '{
#     "contents": [
#       {
#         "parts": [
#           {"text": "Explain what an API gateway does in two sentences."}
#         ]
#       }
#     ]
#   }'
