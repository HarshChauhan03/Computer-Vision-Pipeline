import os

train_path = "dataset/train"
test_path = "dataset/test"

# -----------------------------
# 1️⃣ Count Images
# -----------------------------
def count_images(folder):
    total = 0
    for category in os.listdir(folder):
        category_path = os.path.join(folder, category)
        total += len(os.listdir(category_path))
    return total

train_count = count_images(train_path)
test_count = count_images(test_path)

print("📊 Dataset Info")
print(f"Training Images: {train_count}")
print(f"Testing Images: {test_count}")

# -----------------------------
# 2️⃣ Show Classes
# -----------------------------
classes = os.listdir(train_path)

print("\n📁 Classes:")
print(classes)