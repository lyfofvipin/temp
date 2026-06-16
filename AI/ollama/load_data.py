from datasets import load_dataset

dataset = load_dataset(
    "json",
    data_files="data.json",
    split="train"
)

print(dataset[0])