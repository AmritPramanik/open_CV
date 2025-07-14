# crop an Image by dragging a rectangle shape by mouse

import cv2
from sympy import false

img = cv2.imread('img/image.png')

flag = false
ix = -1
iy = -1

def crop_img(event,x,y,flags,params):
    global flag,ix,iy
    if  event == 1:
        ix = x
        iy = y
        flag = True

    elif event == 0:
        if flag:
            temp_img = img.copy()
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 0,0), 1)
            cv2.imshow('window', temp_img)

    elif event == 4:
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), 1)
        flag = False
        crop = img[iy:y,ix:x]
        cv2.imshow('new_window',crop)
        cv2.waitKey(0)


cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',crop_img)

while True :
    cv2.imshow('window',img)
    if cv2.waitKey(1) == ord('x'):
        break

cv2.destroyAllWindows()