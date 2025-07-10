🐾 Cat vs. Dog Image Classifier
A simple image classification project using Support Vector Machines (SVM) to distinguish between cats and dogs. 🐱🐶 Built with Python: opencv-python, numpy, scikit-learn.

📝 Table of Contents
Overview

Features

Dataset

Setup

Usage

Model

Evaluation

Contribute

License

✨ Overview
Train an SVM to classify images as either cats or dogs. 📸 This project demonstrates a basic image classification pipeline from data loading to model evaluation.

🚀 Features
Image Loading: 📂 Loads images from specified directories.

Preprocessing: 🖼️ Resizes images to 64x64 pixels and flattens them.

SVM Training: 🧠 Trains a Support Vector Classifier (SVC) with a linear kernel.

Train/Test Split: Divides data for robust model validation.

Classification Report: 📊 Provides precision, recall, f1-score, and support.

💾 Dataset
Expected directory structure:

.
└── dataset/
    ├── cats/
    │   ├── cat_1.jpg
    │   └── ...
    └── dogs/
        ├── dog_1.jpg
        └── ...

Place your cat and dog images inside their respective cats and dogs subfolders within a dataset directory.

🛠️ Setup
Python required. Install the necessary libraries:

pip install opencv-python numpy scikit-learn

🏃 Usage
Get Script & Data: ⬇️ Save cat_dog_classifier.py and create the dataset directory structure.

Run: ▶️ Execute from your terminal:

python cat_dog_classifier.py

See Results: The classification report will be printed to your console. 📋

🧠 Model
A sklearn.svm.SVC (Support Vector Classifier) with a linear kernel is used. SVMs are powerful for classification tasks by finding the optimal hyperplane that separates data points into different classes.

📊 Evaluation
The classification_report shows key metrics for model performance:

Precision: Accuracy of positive predictions.

Recall: Ability to find all positive samples.

F1-Score: Harmonic mean of precision and recall.

Support: Number of actual occurrences of each class.

🤝 Contribute
Fork, improve, PRs welcome! 🙏

📜 License
MIT License 📄
