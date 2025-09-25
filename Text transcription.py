from Data import CSV_PATH,AUDIO_PATH,CACHE_PATH

# === Load Wav2Vec2 Model ===
print("Loading Wav2Vec2 model...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h").to(device)

# === Transcription Function ===
def transcribe_audio(file_path, max_duration=60):
    try:
        audio, sr = librosa.load(file_path, sr=16000, duration=max_duration)
        inputs = processor(audio, return_tensors="pt", sampling_rate=16000)
        with torch.no_grad():
            logits = model(**{k: v.to(device) for k, v in inputs.items()}).logits
        pred_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(pred_ids)[0]
        return transcription.lower()
    except Exception as e:
        print(f" Error transcribing {file_path}: {e}")
        return None

# === Safe wrapper for parallel use ===
def safe_transcribe(row):
    return transcribe_audio(row['filename'])

# === If cached file exists, load that ===
if os.path.exists(CACHE_PATH):
    print(" Using cached transcriptions...")
    df = pd.read_csv(CACHE_PATH)
else:
    print(" Starting parallel transcription...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        df['transcription'] = list(tqdm(executor.map(safe_transcribe, df.to_dict('records')), total=len(df)))
    
    # Drop failed ones and cache the results
    df = df.dropna(subset=["transcription"])
    df.to_csv(CACHE_PATH, index=False)
    print(f" Transcriptions saved to {CACHE_PATH}")


print(f"Transcriptions available for {len(df)} audio files.")
