
import os
from PIL import Image

source_path = "data/tomato"
output_path = "data/processed/tomato"

classes = [
    "Healthy",
    "Early_Blight",
    "Late_Blight"
]

extensions = (".jpg", ".jpeg", ".png")
target_size = (224, 224)

for class_name in classes:
    source_folder = os.path.join(source_path, class_name)
    output_folder = os.path.join(output_path, class_name)

    if not os.path.isdir(source_folder):
        print(f"Folder missing: {source_folder}")
        continue

    os.makedirs(output_folder, exist_ok=True)

    processed = 0
    failed = 0

    for filename in os.listdir(source_folder):
        if not filename.lower().endswith(extensions):
            continue

        source_file = os.path.join(source_folder, filename)
        output_file = os.path.join(
            output_folder,
            os.path.splitext(filename)[0] + ".jpg"
        )

        try:
            with Image.open(source_file) as img:
                img = img.convert("RGB")
                img = img.resize(target_size)
                img.save(output_file, format="JPEG", quality=95)

            processed += 1

        except Exception as error:
            print("Could not process:", source_file, error)
            failed += 1

    print(f"\n{class_name}")
    print("Processed:", processed)
    print("Failed:", failed)

print("\nResizing completed!")
