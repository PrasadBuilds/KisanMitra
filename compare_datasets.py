
from pathlib import Path
import hashlib

folders = {
    "old_dataset": Path("tomato_dataset"),
    "new_test": Path(
        r"C:\Users\lenovo\Desktop\Tomato_Test_Dataset\Extracted\Dataset\test"
    ),
}

extensions = {".jpg", ".jpeg", ".png"}

def get_hashes(root):
    results = {}

    for file in root.rglob("*"):
        if file.is_file() and file.suffix.lower() in extensions:
            try:
                digest = hashlib.sha256(file.read_bytes()).hexdigest()
                results.setdefault(digest, []).append(str(file))
            except OSError:
                print("Could not read:", file)

    return results

for name, folder in folders.items():
    print(f"\n{name}: {folder}")

    if not folder.exists():
        print("Folder not found!")
    else:
        count = sum(
            1 for f in folder.rglob("*")
            if f.is_file() and f.suffix.lower() in extensions
        )
        print("Images:", count)

data_hashes = get_hashes(folders["old_dataset"])
dataset_hashes = get_hashes(folders["new_test"])

common = set(data_hashes) & set(dataset_hashes)

print("\nExact duplicate image contents across folders:", len(common))
print("This checks exact duplicates only.")
print("It does not prove whether images were used for training.")
