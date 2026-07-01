"""
Fine-tune a small language model with LoRA on CPU.

Uses Qwen/Qwen2.5-0.5B-Instruct (~82M params). Typical run time: under a minute on a modern laptop.
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

MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"
# LORA_TARGETS = ["c_attn", "c_proj", "c_fc"] # Model internal attention layers
LORA_TARGETS = LORA_TARGETS = [
    "q_proj", 
    "k_proj", 
    "v_proj", 
    "o_proj", 
    "gate_proj", 
    "up_proj", 
    "down_proj"
]

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
    # model.to("cuda")
    # model.to("mps")

    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=LORA_TARGETS,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    # What it does: It freezes 99%+ of Qwen's weights. It inserts pairs of small matrices 
    # (Rank 8) into the attention layers (LORA_TARGETS).
    # Why it matters for CPU: When model.print_trainable_parameters() runs, 
    # you'll see that you are training less than 1% of the model.
    # Because the CPU only has to calculate gradients for this tiny fraction
    # memory usage stays low and training finishes incredibly fast.
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    # PEFT (Parameter-Efficient Fine-Tuning)
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

    # batch_size=1: Feeds only 1 text example into the CPU at a time to keep RAM consumption minimal.
    # gradient_accumulation_steps=4: Instead of updating the weights after every single example,
    # the script calculates gradients for 1 example, saves it, repeats for 4 examples, and then does a single weight update. This simulates a larger batch size of 4 without the massive RAM spike.
    # max_steps=60: Caps the total training steps to 60. On a 0.5B model, this takes less than a minute but is just enough to force the model to memorize small, specific custom datasets (like company FAQs).

    # The SFTTrainer (Supervised Fine-Tuning Trainer) handles the heavy lifting of the training loop. Once trainer.train() finishes, look closely at what is being saved:
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
