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

## 📁 Project Structure
.                                # Root directory of your project
├── train.csv                   # Training labels & audio file names
├── test.csv                    # Test file names (no labels)
├── audios_train/               # Folder containing training audio (.wav) files
├── audios_test/                # Folder containing test audio (.wav) files
├── transcribed_dataset.csv     # Cached transcriptions (output of Wav2Vec2)
├── bert_bilstm_model.pt        # Saved PyTorch model (BERT + BiLSTM)
├── submission.csv              # Final predictions for submission
├── scripts/                    # Folder containing modular Python scripts
│   ├── textranscription.py           # Script for audio transcription using Wav2Vec2
│   ├── preprocess.py           # Script for text cleaning and tokenization
│   ├── grammar_score_model.py                # Model definition (BERT + BiLSTM) Training loop for the model
│   └── inference.py              # Inference script that generates submission.csv
