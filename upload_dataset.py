# upload_dataset.py

from datasets import load_dataset
import pandas as pd

csv_file_path = 'suplyd_intents_v2.csv'

print(f"Loading new dataset from: {csv_file_path}")
new_dataset = load_dataset('csv', data_files={'train': csv_file_path})

print("\nDataset loaded successfully. Here's a preview:")
print(new_dataset)
print(new_dataset['train'][0])

repo_id = "ShazaAly/suplyd-arabic-intents-dataset-v1"

print(f"\nPushing dataset to the Hub at: {repo_id}")
new_dataset.push_to_hub(
    repo_id=repo_id,
    commit_message="Feat: Update dataset with 27 intents, balanced with colloquial Arabic and English examples"
)

print("\nUpdate complete! Check your dataset on the Hugging Face Hub.")