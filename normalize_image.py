
import os
import numpy as np
from PIL import Image

folder = "data/processed/tomato/Healthy"

files = [
    f for f in os.listdir(folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

if not files:
    print("No images found!")
else:
    image_path = os.path.join(folder, files[0])

    with Image.open(image_path) as img:
        img = img.convert("RGB")
        pixels = np.array(img, dtype=np.float32)

    normalized = pixels / 255.0

    print("Original minimum:", pixels.min())
    print("Original maximum:", pixels.max())

    print("Normalized minimum:", normalized.min())
    print("Normalized maximum:", normalized.max())

    print("Original first pixel:", pixels[0, 0])
    print("Normalized first pixel:", normalized[0, 0])

    print("Normalized shape:", normalized.shape)
