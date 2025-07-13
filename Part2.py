# Convert RGB Image to GrayScale image
# It is useFull for face detection by B/W facial carve

import cv2
import numpy as np

img = cv2.imread("img/image.png")

#  create GrayScale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
# here shape is (512, 512)
#  it have no 3 because it is B/W image

cv2.imshow('window',gray_img)
cv2.waitKey(0)  # 0 for infinity tyme