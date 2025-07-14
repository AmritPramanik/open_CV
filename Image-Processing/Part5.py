# Flip an image
import cv2
import numpy as np

img = cv2.imread('img/image.png')

# 3 type of flip is possible
# it is called data aggumentation use for randamization in image data to remove overfitting
img_flip1 = cv2.flip(img,0) # reverse horizontally
img_flip2 = cv2.flip(img,1) # reverse vertically
img_flip3 = cv2.flip(img,-1) # reverse both vertically & horizontally

new_img = np.hstack((img_flip1,img_flip2,img_flip3))
cv2.imshow('Window',new_img)
cv2.waitKey(0)
