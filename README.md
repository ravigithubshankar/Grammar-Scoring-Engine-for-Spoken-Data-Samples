<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
# Grammar-Scoring-Engine-for-Spoken-Data-Samples

This repository contains a pipeline to evaluate the grammatical accuracy of spoken audio using a fusion of **ASR (Automatic Speech Recognition)** and **deep learning models**. The solution transcribes audio using Wav2Vec2, preprocesses the text, and predicts grammar scores using a **BERT + BiLSTM regression model**.

---

![image](https://github.com/user-attachments/assets/96c6b4fa-fbad-4991-8043-4d7349839b64)
Architecture

## 🚀 Overview

### 🧠 Task
Given an audio clip of a candidate speaking, predict a **grammar score (1–5)** reflecting their spoken grammar quality.

### 📊 Dataset
- **`train.csv`**: Contains audio file names + grammar labels.
- **`audios_train/`**: Folder of training `.wav` files.
- **`test.csv`** / **`audios_test/`**: Evaluation set without labels.

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


---

![image](https://github.com/user-attachments/assets/3a93cbab-e90d-47c6-b378-f92c55f2b9e9)


## 🧪 Running the Pipeline

```bash
# Step 1: Texttranscription
python texttranscription.py

# Step 2: Preprocess text
python preprocess.py

# Step 3: Train model
python grammar_score_model.py

# Step 4: Run inference on test set
python inference.py




>>>>>>> dc43c328627c7557fdf3260c13f9be7b30cdc9c8
