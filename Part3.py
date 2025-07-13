# do some RGB Color channels

import cv2
import numpy as np

def display(img):
    cv2.imshow('window',img)
    cv2.waitKey(0)

img = cv2.imread('img/image.png')

# In openCV color shade is BGR( Blue, Green, Red)

# here 0 means Blue define as 0 so Blue color is removed from BGR
# img[:,:,0] = 0
# display(img)

# here 1 means Green define as 0 so Green color is removed from BGR
# img[:,:,1] = 0
# display(img)

# here 2 means Red define as 0 so Red color is removed from BGR
# img[:,:,2] = 0
# display(img)


# Stack color channels
imBlue = img[:,:,0]
imGreen = img[:,:,1]
imRed = img[:,:,2]

new_img = np.hstack((imBlue,imGreen,imRed))
display(new_img)