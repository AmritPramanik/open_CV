# click and drag the mouse to creat a box

import cv2
import numpy as np

img = np.zeros((600,600,3))

flag = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):
    global ix,iy,flag
    if event == 1 :
        ix = x
        iy = y
        flag = True

    elif event == 0:
        if flag == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)

    elif event == 4:
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        flag = False

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',draw)

while True:
    cv2.imshow('window',img)
    if cv2.waitKey(1) == ord('x'):
        break

cv2.destroyAllWindows()