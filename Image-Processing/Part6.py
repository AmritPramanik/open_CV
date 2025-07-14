# Cropping an Image..

import cv2
import numpy as np

img = cv2.imread('img/image.png')
new_img1 = img[0:300,0:200]
new_img2 = img[0:300,100:300]

stack_img = np.hstack((new_img1,new_img2))
cv2.imshow('window',stack_img)
cv2.waitKey(0)