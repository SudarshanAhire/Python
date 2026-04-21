import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read image 
img = cv2.imread("sample.jpg")

# 2. Convert to Grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Display image + pixel grid 
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1); plt.imshow(gray, cmap="gray");
# plt.title("Grayscale Image"); plt.axis("off")
# plt.subplot(1, 2, 2); plt.imshow(gray, cmap="gray");
# plt.colorbar(label="Pixel Value"); plt.title("Pixel Values")
# plt.show()

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(gray, cmap="gray")
plt.colorbar(label="Pixel Value") 
plt.title("Pixel Values")
plt.show()