"""Preview the training dataset and formatted text used by train_model.py."""

from pathlib import Path

from datasets import load_dataset

DATA_FILE = Path(__file__).resolve().parent / "data.json"


def format_example(example: dict) -> str:
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )


def main():
    dataset = load_dataset("json", data_files=str(DATA_FILE), split="train")
    print(f"Examples: {len(dataset)}\n")
    print("First record (raw):")
    print(dataset[0])
    print("\nFirst record (training format):")
    print(format_example(dataset[0]))


if __name__ == "__main__":
    main()
