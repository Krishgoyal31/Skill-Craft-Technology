import cv2
import mediapipe as mp
import numpy as np
from sklearn.svm import SVC
import joblib
import os

# --- Setup ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

GESTURES = {
    'fist': 0,
    'palm': 1,
    'thumbs_up': 2,
    'peace': 3
}
REVERSE = {v: k for k, v in GESTURES.items()}

X = []
y = []

# --- Landmark extraction ---
def extract_landmarks(results):
    if not results.multi_hand_landmarks:
        return None
    data = []
    for lm in results.multi_hand_landmarks[0].landmark:
        data.extend([lm.x, lm.y, lm.z])
    return data

# --- Main app ---
print("🖐️ Hand Gesture Recognition")
print("Instructions:")
print("  [1] Press 1–4 to select gesture label:")
for name, val in GESTURES.items():
    print(f"      {val+1}: {name}")
print("  [c] to capture gesture")
print("  [t] to train model")
print("  [p] to predict gestures")
print("  [q] to quit")

current_label = 0
model = None

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        mp_draw.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

    key = cv2.waitKey(1)

    if key in [49, 50, 51, 52]:  # Keys 1–4
        current_label = key - 49  # Maps to 0–3
        print(f"🔤 Selected label: {REVERSE[current_label]}")

    elif key == ord('c'):
        data = extract_landmarks(results)
        if data:
            X.append(data)
            y.append(current_label)
            print(f"✅ Captured: {REVERSE[current_label]} ({len(X)} samples)")

    elif key == ord('t'):
        if len(X) < 5:
            print("⚠️ Not enough samples to train.")
            continue
        clf = SVC(kernel='linear')
        clf.fit(X, y)
        joblib.dump(clf, 'gesture_model.pkl')
        print("🎉 Model trained and saved as gesture_model.pkl")

    elif key == ord('p'):
        if not os.path.exists('gesture_model.pkl'):
            print("⚠️ Train the model first!")
            continue
        clf = joblib.load('gesture_model.pkl')
        print("📦 Loaded model. Predicting...")
        while True:
            _, live = cap.read()
            live = cv2.flip(live, 1)
            rgb_live = cv2.cvtColor(live, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_live)
            if results.multi_hand_landmarks:
                mp_draw.draw_landmarks(live, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
                data = extract_landmarks(results)
                if data:
                    prediction = clf.predict([data])[0]
                    label = REVERSE[prediction]
                    cv2.putText(live, f'Gesture: {label}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            cv2.imshow("Real-Time Prediction", live)
            if cv2.waitKey(1) & 0xFF == ord('b'):
                break
        print("🛑 Exiting prediction mode.")

    elif key == ord('q'):
        print("👋 Exiting program.")
        break

    cv2.putText(frame, f'Label: {REVERSE[current_label]}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)
    cv2.imshow("Hand Gesture Recognizer", frame)

cap.release()
cv2.destroyAllWindows()
