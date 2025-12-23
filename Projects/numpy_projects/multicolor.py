import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Load image from URL
def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Load Elephant image
tiger_url = ("https://transforms.stlzoo.org/production/animals/"
             "amur-tiger-01-01.jpg?w=1200&h=1200&auto="
             "compress%2Cformat&fit=crop&dm=1658935145&s=95d03aceddd44dc8271beed46eae30bc")
tiger = load_image_from_url(tiger_url).convert("RGB")
tiger_np = np.array(tiger)

# Split RGB channels
R, G, B = tiger_np[:, :, 0], tiger_np[:, :, 1], tiger_np[:, :, 2]

# Create images emphasizing each channel
red_img = np.zeros_like(tiger_np)
green_img = np.zeros_like(tiger_np)
blue_img = np.zeros_like(tiger_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display original and RGB color-emphasized images
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(tiger_np)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(red_img)
plt.title("Red Channel Emphasis")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(green_img)
plt.title("Green Channel Emphasis")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(blue_img)
plt.title("Blue Channel Emphasis")
plt.axis("off")

plt.tight_layout()
plt.show()

# Optional: Apply a colormap to grayscale
elephant_gray = tiger.convert("L")
elephant_gray_np = np.array(elephant_gray)

plt.figure(figsize=(6, 5))
plt.imshow(elephant_gray_np, cmap="viridis")  # Change cmap to 'hot', 'cool', etc.
plt.title("Colormapped Grayscale")
plt.axis("off")
plt.colorbar()
plt.show()
