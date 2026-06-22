"""
OpenAI API — SDK vs raw requests (same call, two ways).
Requires: pip install openai requests
Set OPENAI_API_KEY in your environment before running.
"""

import os

# gpt-4o-mini: lowest-cost general-purpose model (good for demos)
MODEL = "gpt-4o-mini"
PROMPT = "write a flask app that uses Open API keys to be used in another UI."

# --- Option 1: Official SDK (active) ---
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from env

response = client.responses.create(
    model=MODEL,
    input=PROMPT,
)

print(response.output_text)


# --- Option 2: Same call with requests (uncomment to compare) ---
# import requests
#
# api_key = os.environ["OPENAI_API_KEY"]
#
# response = requests.post(
#     "https://api.openai.com/v1/responses",
#     headers={
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#     },
#     json={
#         "model": MODEL,
#         "input": PROMPT,
#     },
#     timeout=120,
# )
# response.raise_for_status()
# data = response.json()
#
# # Same result — SDK's output_text is a shortcut for this path in the JSON:
# print(data["output"][0]["content"][0]["text"])
