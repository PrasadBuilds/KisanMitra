from PIL import Image

image_path = "data/tomato/Healthy"

# Get the first image from the folder
import os

files = os.listdir(image_path)

for file in files:
    if file.endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(image_path, file)
        break

# Open image
image = Image.open(image_path)

print("Original image size:", image.size)

# Resize image
image = image.resize((224, 224))

print("New image size:", image.size)

# Get one pixel
pixel = image.getpixel((0, 0))

print("RGB value of one pixel:", pixel)