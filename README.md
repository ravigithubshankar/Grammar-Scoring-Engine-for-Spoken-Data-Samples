# Grammar-Scoring-Engine-for-Spoken-Data-Samples

This repository contains a pipeline to evaluate the grammatical accuracy of spoken audio using a fusion of **ASR (Automatic Speech Recognition)** and **deep learning models**. The solution transcribes audio using Wav2Vec2, preprocesses the text, and predicts grammar scores using a **BERT + BiLSTM regression model**.

---

## 🚀 Overview

### 🧠 Task
Given an audio clip of a candidate speaking, predict a **grammar score (1–5)** reflecting their spoken grammar quality.

### 📊 Dataset
- **`train.csv`**: Contains audio file names + grammar labels.
- **`audios_train/`**: Folder of training `.wav` files.
- **`test.csv`** / **`audios_test/`**: Evaluation set without labels.

---

---

## 🛠️ Pipeline

### 1. 🎙️ Audio Transcription
- Model: `facebook/wav2vec2-base-960h`
- Output: Lowercased text using `batch_decode`.

### 2. 🧹 Text Preprocessing
- Remove punctuation, normalize spaces, lowercase.

### 3. 🧠 Modeling
- Architecture: **BERT Embeddings → BiLSTM → Dense Regression Head**
- Loss: **MSELoss**, optional Pearson/CCC loss
- Framework: PyTorch

### 4. 🧪 Evaluation
- Metric: **Pearson Correlation** on validation set.
- Visualization: Score distributions, loss curves.

---

## 📈 Results

| Metric        | Value      |
|---------------|------------|
| Pearson (val) | `0.599`     |
| MSE (val)     | `5.78 50 epochs`     |

Sample visualizations:
- ✅ Score distributions by label
- ✅ Attention heatmaps (optional)
- ✅ Confusion/box plots (optional)

---

## 🧪 Running the Pipeline

```bash
# Step 1: Transcribe audio
python scripts/transcribe.py

# Step 2: Preprocess text
python scripts/preprocess.py

# Step 3: Train model
python scripts/train.py

# Step 4: Run inference on test set
python scripts/predict.py
