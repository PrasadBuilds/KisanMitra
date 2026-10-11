
import os
import random
import shutil

source_path = "data/processed/tomato"
output_path = "data/splits"

classes = [
    "Healthy",
    "Early_Blight",
    "Late_Blight"
]

extensions = (".jpg", ".jpeg", ".png")
random.seed(42)

for class_name in classes:
    source_folder = os.path.join(source_path, class_name)

    if not os.path.isdir(source_folder):
        raise FileNotFoundError(
            f"Missing folder: {source_folder}. "
            "Run resize_images.py first."
        )

    files = [
        name for name in os.listdir(source_folder)
        if name.lower().endswith(extensions)
    ]

    if not files:
        raise ValueError(f"No images found in {source_folder}")

    random.shuffle(files)

    total = len(files)
    train_end = int(total * 0.70)
    val_end = int(total * 0.85)

    splits = {
        "train": files[:train_end],
        "validation": files[train_end:val_end],
        "test": files[val_end:]
    }

    for split_name, split_files in splits.items():
        destination = os.path.join(
            output_path, split_name, class_name
        )
        os.makedirs(destination, exist_ok=True)

        for filename in split_files:
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination, filename)
            shutil.copy2(source_file, destination_file)

        print(f"{class_name} - {split_name}: {len(split_files)}")

print("\nDataset splitting completed!")
