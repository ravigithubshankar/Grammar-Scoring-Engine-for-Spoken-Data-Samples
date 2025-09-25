from grammar_score_model import model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BERT_BiLSTM_Regression().to(device)
model.load_state_dict(torch.load("bert_bilstm_regression.pth", map_location=device))
model.eval()
print(" Model loaded and set to evaluation mode.")

TEST_CSV_PATH = "/kaggle/input/shl-intern-hiring-assessment/dataset/test.csv"
TEST_AUDIO_DIR = "/kaggle/input/shl-intern-hiring-assessment/dataset/audios_test"

# Load test CSV
test_df = pd.read_csv(TEST_CSV_PATH)
test_df['filename'] = test_df['filename'].apply(lambda x: os.path.join(TEST_AUDIO_DIR, x))
test_df = test_df[test_df['filename'].apply(os.path.isfile)]

# Load Wav2Vec2
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
asr_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h").to(device)

def transcribe_audio(file_path):
    audio, _ = librosa.load(file_path, sr=16000)
    inputs = processor(audio, return_tensors="pt", sampling_rate=16000)
    with torch.no_grad():
        logits = asr_model(**{k: v.to(device) for k, v in inputs.items()}).logits
    pred_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(pred_ids)[0]
    return transcription.lower()

def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

# Transcribe and clean
tqdm.pandas(desc="🎙️ Transcribing test set")
test_df["transcription"] = test_df["filename"].progress_apply(transcribe_audio)
test_df["clean_text"] = test_df["transcription"].apply(clean_text)

tokenizer = BertTokenizer.from_pretrained("bert_tokenizer/")



encodings = tokenizer(
    test_df["clean_text"].tolist(),
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors="pt"
)


from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

encodings = tokenizer(
    test_df["clean_text"].tolist(),
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors="pt"
)
from torch.utils.data import Dataset, DataLoader
import numpy as np

class TestDataset(Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __len__(self):
        return len(self.encodings['input_ids'])

    def __getitem__(self, idx):
        return {
            'input_ids': self.encodings['input_ids'][idx],
            'attention_mask': self.encodings['attention_mask'][idx]
        }

test_dataset = TestDataset(encodings)
test_loader = DataLoader(test_dataset, batch_size=32)

predictions = []
model.eval()
with torch.no_grad():
    for batch in test_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        outputs = model(input_ids, attention_mask)
        predictions.extend(outputs.cpu().numpy())

# Clip predictions and format
predictions = np.clip(np.round(predictions, 2), 0, 5).flatten()
submission_df = pd.DataFrame({
    "filename": [os.path.basename(f) for f in test_df["filename"]],
    "label": predictions
})
submission_df.to_csv("submission.csv", index=False)
print(" Saved predictions to submission.csv")
