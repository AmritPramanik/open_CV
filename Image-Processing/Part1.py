# Read & Display image
import cv2
import numpy as np

# Read the Image
img = cv2.imread('img/image.png')

print(img) # The Image numpy Array
print(img.shape) # Image Shape
print(type(img))
# Shape (512, 512, 3) mean 512 x 512 size & 3 for RGB color

# Display the Image
cv2.imshow('window',img)
cv2.waitKey(0)
