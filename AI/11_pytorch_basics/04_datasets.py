"""
04 — Hugging Face datasets: load JSON and transform rows.

Maps to train_model.py:
  - load_dataset("json", data_files=...) (line 36)
  - dataset.map(to_training_text) (line 37)
"""

from pathlib import Path

from datasets import load_dataset

# When you run load_dataset("json", ...) from Hugging Face’s datasets library, it doesn't just read the JSON file into a standard Python list. It converts it into an Apache Arrow memory table.
# Why Arrow? Hugging Face datasets are designed to handle gigabytes of data without crashing your computer's RAM. They stream data from your hard drive instantly, making them incredibly fast compared to a traditional Pandas DataFrame.

# Reuse the same data file as train_model.py
DATA_FILE = Path(__file__).resolve().parent.parent / "ollama" / "data.json"


def to_training_text(example):
    """Same function shape as train_model.py — adds a 'text' column."""
    example["text"] = (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )
    return example


def main():
    dataset = load_dataset("json", data_files=str(DATA_FILE), split="train")
    print(f"Raw rows: {len(dataset)}")
    print("Columns:", dataset.column_names)
    print("First row:", dataset[0])

    dataset = dataset.map(to_training_text)
    print("\nAfter .map() — new 'text' column:")
    print(dataset[0]["text"][:200], "...")

    ### Instruction:
    # What is XYZ ORG?
    # ### Response:
    # XYZ ORG is an AI and software training organization based in Jaipur.

    print("\nIn train_model.py:")
    print("  SFTTrainer reads dataset['text'] for supervised fine-tuning")


if __name__ == "__main__":
    main()
