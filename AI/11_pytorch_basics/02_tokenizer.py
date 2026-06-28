"""
02 — Tokenizer: text ↔ numbers the model understands.

Maps to train_model.py:
  - AutoTokenizer.from_pretrained (line 40)
  - pad_token setup (lines 41-42)
  - tokenizer(prompt, return_tensors="pt") (line 85)
  - tokenizer.decode (line 98)
"""

from transformers import AutoTokenizer

MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# GPT-2 has no pad token by default — train_model.py fixes this:
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# To fix this without messing up the model's vocabulary matrix, developers borrow the EOS (End of Sequence) token and tell the tokenizer: "Whenever you need to pad a sentence, just use the EOS token as a placeholder."

text = "Hello, XYZ ORG team!"
encoded = tokenizer(text)
print("Encoded (dict):", encoded)
print("Token IDs:", encoded["input_ids"])
print("Tokens:", tokenizer.convert_ids_to_tokens(encoded["input_ids"]))

# Models need tensors, not plain lists — return_tensors="pt" means PyTorch
inputs = tokenizer(text, return_tensors="pt")
print("\nAs PyTorch tensors:")
print("  input_ids shape:", inputs["input_ids"].shape)

decoded = tokenizer.decode(encoded["input_ids"], skip_special_tokens=True)
print("\nDecoded back:", decoded)

print("\nIn train_model.py:")
print("  Training text is formatted as ### Instruction / ### Response")
print("  Tokenizer turns that string into input_ids for the model")
