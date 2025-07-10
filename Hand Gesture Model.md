🖐️ Hand Gesture Recognition
Real-time hand gesture recognition using MediaPipe for landmark detection and Support Vector Machines (SVM) for classification. 🤖 Recognizes custom gestures from your webcam!

📝 Table of Contents
Overview

Features

Supported Gestures

Setup

Usage

How it Works

Contribute

License

✨ Overview
Train a machine learning model to understand your hand gestures! 👋 Capture samples, train an SVM, and then predict gestures live from your webcam.

🚀 Features
Gesture Capture: 📸 Collects hand landmark data for custom gestures.

SVM Training: 🧠 Trains a Support Vector Classifier on your captured data.

Real-time Prediction: ⚡ Recognizes gestures live from your webcam.

Interactive Controls: Simple keyboard commands for easy use.

Model Persistence: Saves and loads the trained model. 💾

👋 Supported Gestures
You can train the model to recognize these gestures:

Fist ✊

Palm ✋

Thumbs Up 👍

Peace ✌️

🛠️ Setup
Python required. Install the necessary libraries:

pip install opencv-python mediapipe scikit-learn joblib

🏃 Usage
Get Script: ⬇️ Save gesture_recognizer.py to your local machine.

Run: ▶️ Execute from your terminal:

python gesture_recognizer.py

Interact: Follow the on-screen instructions in the console and webcam window:

Press 1, 2, 3, 4 to select a gesture label.

Press c to capture the current hand pose for the selected label.

Press t to train the SVM model (needs at least 5 samples).

Press p to enter prediction mode. Press b to exit prediction mode.

Press q to quit the application.

🧠 How it Works
MediaPipe Hands: Detects 21 3D landmarks for a single hand in real-time.

Data Collection: Landmark coordinates are flattened and stored as training data.

SVM Classifier: A sklearn.svm.SVC (Support Vector Classifier) learns to map landmark patterns to gesture labels.

Prediction: The trained SVM predicts the gesture based on live webcam input.

🤝 Contribute
Fork, improve, PRs welcome! 🙏

📜 License
MIT License 📄
