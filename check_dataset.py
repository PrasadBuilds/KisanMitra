
import os

dataset_path = "data/tomato"

classes = [
    "Healthy",
    "Early_Blight",
    "LateBlight"
]

for class_name in classes:
    folder_path = os.path.join(
        dataset_path, class_name
    )

    if not os.path.isdir(folder_path):
        print(class_name, "- Folder missing!")
        continue

    image_files = [
        file for file in os.listdir(folder_path)
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        )
    ]

    print(class_name, ":", len(image_files), "images")