import cv2
import os

input_dir = "raw_images"
output_dir = "dataset"
os.makedirs(f"{output_dir}/cats", exist_ok=True)
os.makedirs(f"{output_dir}/dogs", exist_ok=True)

# Tell which file is a cat or a dog
images = {
    "cat1.jpg": "cats",
    "cat2.jpg": "cats",
    "dog1.jpg": "dogs",
    "dog2.jpg": "dogs",
    "cat3.jpg": "cats",
    "cat4.jpg": "cats",
    "dog3.jpg": "dogs",
    "dog4.jpg": "dogs",
    "cat5.jpg": "cats",
    "dog5.jpg": "dogs"
}

# Resize each image to 64x64 and save in right folder
for file, label in images.items():
    img_path = os.path.join(input_dir, file)
    img = cv2.imread(img_path)
    if img is not None:
        img = cv2.resize(img, (64, 64))
        out_path = os.path.join(output_dir, label, file)
        cv2.imwrite(out_path, img)
        print(f"Saved: {out_path}")
    else:
        print(f"Could not read: {file}")
