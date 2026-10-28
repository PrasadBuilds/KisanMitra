
from pathlib import Path
import hashlib

old_folder = Path("tomato_dataset")

new_test_folder = Path(
    r"C:\Users\lenovo\Desktop\Tomato_Test_Dataset\Extracted\Dataset\test"
)

classes = {
    "Tomato___healthy": "Healthy",
    "Tomato___Early_blight": "Early Blight",
    "Tomato___Late_blight": "Late Blight",
}

extensions = {".jpg", ".jpeg", ".png"}


def get_image_hashes(folder):
    hashes = {}

    if not folder.exists():
        print(f"Folder not found: {folder}")
        return hashes

    for file in folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in extensions:
            try:
                digest = hashlib.sha256(file.read_bytes()).hexdigest()
                hashes.setdefault(digest, []).append(file)
            except OSError:
                print("Could not read:", file)

    return hashes


if not old_folder.exists() or not new_test_folder.exists():
    print("ERROR: Check the dataset folder paths.")
else:
    print("INDEPENDENT TEST DATASET CHECK")
    print("=" * 45)

    old_hashes = get_image_hashes(old_folder)

    for folder_name, label in classes.items():
        class_folder = new_test_folder / folder_name

        if not class_folder.exists():
            print(f"\n{label}: Class folder not found")
            continue

        new_hashes = get_image_hashes(class_folder)

        total = sum(len(files) for files in new_hashes.values())
        duplicate_hashes = set(old_hashes) & set(new_hashes)
        duplicate_images = sum(
            len(new_hashes[digest])
            for digest in duplicate_hashes
        )

        print(f"\n{label}")
        print("Total images:", total)
        print("Exact duplicates with old dataset:", duplicate_images)
        print("Images without exact match:", total - duplicate_images)

    print("\nNote: No images were moved or deleted.")
    print("Exact matching does not detect visually similar images.")
