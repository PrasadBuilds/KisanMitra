
import os
from PIL import Image

folder = "data/processed/tomato/Healthy"

for filename in os.listdir(folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(folder, filename)

        with Image.open(path) as img:
            print("Image:", filename)
            print("Size:", img.size)
            print("Mode:", img.mode)

        break
