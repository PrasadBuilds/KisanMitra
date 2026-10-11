
import numpy as np
from PIL import Image

image_path = (
    "data/processed/tomato/Healthy"
)

# Find the first image in the folder
import os

files = [
    f for f in os.listdir(image_path)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

if not files:
    print("No images found!")
else:
    path = os.path.join(image_path, files[0])

    with Image.open(path) as img:
        img = img.convert("RGB")
        pixels = np.array(img)

    print("Image shape:", pixels.shape)
    print("First pixel RGB:", pixels[0, 0])
    print("Minimum pixel value:", pixels.min())
    print("Maximum pixel value:", pixels.max())
    print("Data type:", pixels.dtype)
