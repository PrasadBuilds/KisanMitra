
from pathlib import Path

test_folder = Path(
    r"C:\Users\lenovo\Desktop\Tomato_Test_Dataset\Extracted\Dataset\test"
)

extensions = {".jpg", ".jpeg", ".png"}

if not test_folder.exists():
    print("ERROR: Test folder not found!")
else:
    print("NEW TEST DATASET CLASS COUNTS")
    print("-" * 40)

    for folder in sorted(test_folder.iterdir()):
        if folder.is_dir():
            count = sum(
                1
                for file in folder.rglob("*")
                if file.is_file()
                and file.suffix.lower() in extensions
            )
            print(f"{folder.name}: {count} images")
