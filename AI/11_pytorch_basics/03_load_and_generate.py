"""
03 — Load a Hugging Face model and generate text (inference only).

Maps to train_model.py:
  - AutoModelForCausalLM.from_pretrained (line 44)
  - model.eval() (line 87)
  - model.generate() (lines 89-95)
  - tokenizer.decode (line 98)

This is the same as the bottom of train_model.py, but WITHOUT training.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype=torch.float32)

# Why using float32
# standard debugging, absolute stability
# Older NVIDIA GPUs (Inference)
# Modern GPUs (A100, H100, M1/M2/M3 Mac) for training large LLMs

# Same prompt format as train_model.py uses after fine-tuning
prompt = "### Instruction:\nWhat is XYZ ORG?\n\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt")

model.eval()
with torch.no_grad():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=40,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id,
    )

# max_new_tokens=40 (The Word Limit)
# This tells the model the maximum number of loops it is allowed to execute.
# It will stop generating text as soon as it creates 40 new tokens, or if it naturally generates an End-of-Sequence (<|endoftext|>) token early.

# do_sample=True (Turning on the Wheel of Fortune)
# By default, an LLM acts like a boring robot: it looks at its vocabulary list and always picks the single highest-probability word (e.g., if "the" has a 35% chance and "apple" has a 30% chance, it always picks "the"). This is called Greedy Search.
# Setting do_sample=True changes the rule. It tells the model to treat the probabilities like a wheel of fortune:
# "The" gets a 35% slice of the wheel, and "apple" gets a 30% slice. Every time a new token is generated, PyTorch spins the wheel. The highest-probability word is still more likely to win, but other creative options have a chance too. This stops the model from repeating itself endlessly.

# temperature=0.7 (The Creativity Control)
# Temperature mathematically scales the probabilities before the wheel of fortune is spun.
    # Low Temperature (e.g., 0.2): It sharpens the differences. A 35% chance shoots up to 90%, and lower options drop to near 0%. The model becomes highly predictable, logical, and factual.
    # High Temperature (e.g., 1.5): It flattens the differences out. Every word gets an almost equal slice of the wheel. The model becomes wildly creative, chaotic, and will start writing gibberish or hallucinating.
    # 0.7 is the industry "gold standard" for a balanced, natural human conversation.

# pad_token_id=tokenizer.eos_token_id (The Emergency Stop)
# Remember how we discussed that DistilGPT-2 doesn't have an official padding token out of the box?
# This line explicitly tells the generation function: "If you need to align batches, or if you hit a wall and don't know what to do, use the End-of-Sequence (EOS) token ID as your fallback marker." It keeps the internal looping mechanics from throwing shape or padding mismatch errors.

print(tokenizer.decode(output_ids[0], skip_special_tokens=True))

print("\n--- What each generate() arg does ---")
print("  max_new_tokens  → how many tokens to add after the prompt")
print("  do_sample       → random sampling (vs always picking top token)")
print("  temperature     → higher = more creative, lower = more focused")
print("  pad_token_id    → tells model when to stop padding")
