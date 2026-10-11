
import os

dataset_path = "data/tomato"

classes = [
    "Healthy",
    "Early_Blight",
    "Late_Blight"
]

extensions = (".jpg", ".jpeg", ".png")

total_images = 0

for class_name in classes:
    folder = os.path.join(dataset_path, class_name)

    if not os.path.isdir(folder):
        print(f"{class_name}: Folder missing!")
        continue

    count = sum(
        1 for filename in os.listdir(folder)
        if filename.lower().endswith(extensions)
    )

    total_images += count
    print(f"{class_name}: {count} images")

print("-" * 30)
print("Total images:", total_images)

print("\nClass percentages:")

for class_name in classes:
    folder = os.path.join(dataset_path, class_name)

    if not os.path.isdir(folder):
        continue

    count = sum(
        1 for filename in os.listdir(folder)
        if filename.lower().endswith(extensions)
    )

    percentage = (
        count / total_images * 100
        if total_images else 0
    )

    print(f"{class_name}: {percentage:.2f}%")
