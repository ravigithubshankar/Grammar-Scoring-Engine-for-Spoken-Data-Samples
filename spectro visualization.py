# Load and visualize a few audio samples
samples_to_plot = 3  # Number of samples to visualize
for idx, row in df.head(samples_to_plot).iterrows():
    file_path = row['filename']
    y, sr = librosa.load(file_path, sr=None)  # Load with original sampling rate
    
    print(f"\nFile: {file_path}")
    print(f"Duration: {librosa.get_duration(y=y, sr=sr):.2f}s, Sample Rate: {sr}")
    
    # Plot waveform
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_dB = librosa.power_to_db(S, ref=np.max)

# Plot
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
    plt.title('Mel Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()
