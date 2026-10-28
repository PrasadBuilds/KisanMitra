
from pathlib import Path
import hashlib
import shutil

old_folder = Path("tomato_dataset")

new_test_folder = Path(
    r"C:\Users\lenovo\Desktop\Tomato_Test_Dataset\Extracted\Dataset\test"
)

output_folder = Path(
    r"C:\Users\lenovo\Desktop\KisanMitra_Independent_Test"
)

classes = {
    "Tomato___healthy": "Healthy",
    "Tomato___Early_blight": "Early_Blight",
    "Tomato___Late_blight": "Late_Blight",
}

extensions = {".jpg", ".jpeg", ".png"}


def get_hashes(folder):
    hashes = set()

    for file in folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in extensions:
            try:
                hashes.add(
                    hashlib.sha256(file.read_bytes()).hexdigest()
                )
            except OSError:
                print("Could not read:", file)

    return hashes


if not old_folder.exists() or not new_test_folder.exists():
    print("ERROR: Dataset folder not found.")
else:
    old_hashes = get_hashes(old_folder)

    print("Preparing independent test candidates...")
    print("Original images will not be deleted.")

    for source_class, output_class in classes.items():
        source_folder = new_test_folder / source_class
        destination_folder = output_folder / output_class

        if not source_folder.exists():
            print("Missing class folder:", source_folder)
            continue

        destination_folder.mkdir(parents=True, exist_ok=True)
        copied = 0

        for file in source_folder.rglob("*"):
            if not file.is_file() or file.suffix.lower() not in extensions:
                continue

            try:
                digest = hashlib.sha256(file.read_bytes()).hexdigest()
            except OSError:
                print("Could not read:", file)
                continue

            if digest not in old_hashes:
                destination = destination_folder / file.name

                if destination.exists():
                    destination = destination_folder / (
                        file.stem + "_" + digest[:8] + file.suffix
                    )

                shutil.copy2(file, destination)
                copied += 1

        print(f"{output_class}: copied {copied} images")

    print("\nFinished.")
    print("Candidate images saved to:", output_folder)
    print("These are exact-nonduplicate candidates, not fully verified independent data.")
