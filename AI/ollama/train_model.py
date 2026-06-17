"""
Fine-tune a small language model with LoRA on CPU.

Uses distilgpt2 (~82M params). Typical run time: under a minute on a modern laptop.
"""

from pathlib import Path

import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from trl import SFTTrainer

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / "data.json"
OUTPUT_DIR = SCRIPT_DIR / "outputs"
ADAPTER_DIR = SCRIPT_DIR / "lora_adapter"

MODEL_ID = "distilgpt2"
LORA_TARGETS = ["c_attn", "c_proj", "c_fc"]


def to_training_text(example):
    example["text"] = (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )
    return example


def main():
    print("Device: CPU")
    print(f"Model:  {MODEL_ID}")

    dataset = load_dataset("json", data_files=str(DATA_FILE), split="train")
    dataset = dataset.map(to_training_text)
    print(f"Training examples: {len(dataset)}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype=torch.float32)

    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=LORA_TARGETS,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    training_args = TrainingArguments(
        output_dir=str(OUTPUT_DIR),
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        warmup_steps=2,
        max_steps=60,
        learning_rate=5e-4,
        logging_steps=5,
        save_steps=30,
        report_to="none",
    )

    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,
        train_dataset=dataset,
        args=training_args,
    )

    print("Starting training...")
    trainer.train()

    ADAPTER_DIR.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(ADAPTER_DIR)
    tokenizer.save_pretrained(ADAPTER_DIR)
    print(f"LoRA adapter saved to: {ADAPTER_DIR}")

    prompt = "### Instruction:\nWhat is XYZ ORG?\n\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt")

    model.eval()
    with torch.no_grad():
        generated = model.generate(
            **inputs,
            max_new_tokens=60,
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
        )

    print("\n--- Sample generation after training ---")
    print(tokenizer.decode(generated[0], skip_special_tokens=True))


if __name__ == "__main__":
    main()
