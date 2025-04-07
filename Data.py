CSV_PATH = "/kaggle/input/shl-intern-hiring-assessment/dataset/train.csv"
AUDIO_DIR = "/kaggle/input/shl-intern-hiring-assessment/dataset/audios_train"  # replace if your audio files are in a different folder

df = pd.read_csv(CSV_PATH)

# Add full path to audio files
df['filename'] = df['filename'].apply(lambda x: os.path.join(AUDIO_DIR, x))

# Optional: check for missing files
missing_files = df[~df['filename'].apply(os.path.isfile)]
if not missing_files.empty:
    print("Missing audio files:")
    print(missing_files['audio_path'])

print(df.head(10))

