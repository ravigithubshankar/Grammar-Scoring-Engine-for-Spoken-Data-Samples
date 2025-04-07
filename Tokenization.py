from transformers import BertTokenizer
import pandas as pd
from texttranscription import df
import re

df = pd.read_csv("transcribed_dataset.csv")
texts = df["transcription"].tolist()
labels = df["label"].tolist()
import re
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip().lower()  # Normalize spaces
    return text

df["clean_text"] = df["transcription"].apply(clean_text)

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenize the texts
encodings = tokenizer(
    texts,
    padding=True,          # Pads to the longest sentence
    truncation=True,       # Truncate longer sentences
    max_length=128,        # You can adjust based on your model
    return_tensors="pt"    # Return PyTorch tensors
)

# Optional: convert labels to tensor
labels_tensor = torch.tensor(labels, dtype=torch.float32)
