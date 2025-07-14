#  Resize an image

import cv2
import numpy as np

img = cv2.imread('img/CR7.jpg')
print(img.shape)

# reshape image
# openCV first take (width,hight) but index of hight(0) & width(1)
new_img = cv2.resize(img,(450,600))
print(new_img.shape)

#  half size of an image
half_img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
print(half_img.shape)

cv2.imshow('window',half_img)
cv2.waitKey(0)