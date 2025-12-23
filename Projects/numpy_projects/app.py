import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Helper function to load image from a URL
def load_image_from_url(url):
    response = requests.get(url)
    print(response.status_code)
    return Image.open(BytesIO(response.content))

# Elephant image URL
tiger_url = ("https://transforms.stlzoo.org/production/animals/"
             "amur-tiger-01-01.jpg?w=1200&h=1200&auto="
             "compress%2Cformat&fit=crop&dm=1658935145&s=95d03aceddd44dc8271beed46eae30bc")

# Load elephant image
tiger = load_image_from_url(tiger_url)

# Display original image
plt.figure(figsize=(6, 4))
plt.imshow(tiger)
plt.title("Tiger")
plt.axis("off")
plt.show()

# Convert to NumPy array and print shape
tiger_np = np.array(tiger)
print("Tiger image shape:", tiger_np.shape)

# Convert to grayscale
tiger_gray = tiger.convert("L")

# Display grayscale image
plt.figure(figsize=(6, 4))
plt.imshow(tiger_gray, cmap="gray")
plt.title("Tiger (Grayscale)")
plt.axis("off")
plt.show()
