import matplotlib.pyplot as plt
import os
import cv2

# -----------------------------
# 1️⃣ Dataset Path
# -----------------------------
train_path = "dataset/train"

# -----------------------------
# 2️⃣ Show Sample Images
# -----------------------------
categories = os.listdir(train_path)

plt.figure(figsize=(10, 5))

for i, category in enumerate(categories):
    category_path = os.path.join(train_path, category)
    img_name = os.listdir(category_path)[0]
    img_path = os.path.join(category_path, img_name)

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(1, len(categories), i + 1)
    plt.imshow(img)
    plt.title(category)
    plt.axis("off")

plt.suptitle("Sample Images from Each Class")
plt.show()

# -----------------------------
# 3️⃣ Class Distribution
# -----------------------------
print("\n📊 Class Distribution:")

for category in categories:
    category_path = os.path.join(train_path, category)
    count = len(os.listdir(category_path))
    print(f"{category}: {count} images")

# -----------------------------
# 4️⃣ Image Shape Check
# -----------------------------
sample_img = cv2.imread(img_path)

print("\n📐 Image Shape:")
print(sample_img.shape)