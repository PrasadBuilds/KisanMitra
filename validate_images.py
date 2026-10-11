
import os
from PIL import Image

dataset_path = "data/tomato"
classes = ["Healthy", "Early_Blight", "Late_Blight"]
extensions = (".jpg", ".jpeg", ".png")

for class_name in classes:
    folder = os.path.join(dataset_path, class_name)
    valid_count = 0
    invalid_files = []

    for filename in os.listdir(folder):
        if not filename.lower().endswith(extensions):
            continue

        path = os.path.join(folder, filename)

        try:
            with Image.open(path) as image:
                image.verify()
            valid_count += 1
        except Exception:
            invalid_files.append(filename)

    print(f"\n{class_name}")
    print("Valid images:", valid_count)
    print("Invalid images:", len(invalid_files))

    for filename in invalid_files:
        print("Check this file:", filename)