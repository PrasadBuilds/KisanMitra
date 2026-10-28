from pathlib import Path
from PIL import Image

image_folder = Path(
    r"C:\Users\lenovo\Desktop\KisanMitra_Error_Images"
)

if not image_folder.exists():
    print("ERROR: Image folder not found!")
else:
    images = list(image_folder.glob("*"))

    print("Images found:", len(images))

    for image_path in images:
        try:
            with Image.open(image_path) as img:
                print("Opening:", image_path.name)
                img.show()
        except Exception as error:
            print("Could not open:", image_path.name, error)