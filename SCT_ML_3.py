import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

IMG_SIZE = 64
DATASET_DIR = "dataset"


def load_images():
    X = []
    y = []
    labels = {"cats": 0, "dogs": 1}

    for label in labels:
        folder = os.path.join(DATASET_DIR, label)
        for img_file in os.listdir(folder):
            img_path = os.path.join(folder, img_file)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                X.append(img.flatten())
                y.append(labels[label])

    return np.array(X), np.array(y)


X, y = load_images()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
