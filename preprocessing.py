import cv2
import os
import numpy as np

# -----------------------------
# 1️⃣ Dataset Path
# -----------------------------
train_path = "dataset/train"

# -----------------------------
# 2️⃣ Parameters
# -----------------------------
IMG_SIZE = 224

data = []
labels = []

# -----------------------------
# 3️⃣ Load and Process Images
# -----------------------------
for category in os.listdir(train_path):
    category_path = os.path.join(train_path, category)
    label = os.listdir(train_path).index(category)

    for img_name in os.listdir(category_path):
        img_path = os.path.join(category_path, img_name)

        try:
            # Read image
            img = cv2.imread(img_path)

            # Resize
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

            # Normalize
            img = img / 255.0

            data.append(img)
            labels.append(label)

        except:
            pass

# -----------------------------
# 4️⃣ Convert to NumPy Arrays
# -----------------------------
X = np.array(data)
y = np.array(labels)

print("✅ Preprocessing Done")
print("X shape:", X.shape)
print("y shape:", y.shape)