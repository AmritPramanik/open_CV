# How to save Image..
import cv2

img = cv2.imread('img/CR7.jpg')
resize_img = cv2.resize(img,(550,700))

# save the image
cv2.imwrite('Cristiano.png',resize_img)

cv2.imshow("CR7",resize_img)
cv2.waitKey(0)