# Event create like create a circle when we clik the mouse

import cv2
import numpy as np

img = np.zeros((510,510,3))

"""
event have 3 value:
  event = 0 --> works when mouse is moving
  event = 1 --> works when we clicked
  event = 4 --> when when we click off from mouse
"""
def draw(event,x,y,flags,params):
    if event == 1:
        cv2.circle(img,(x,y),50,(255,0,0),-1)

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',draw)

# This function use for refresh the image
#  when i press 'x' then it stop
while True:
    cv2.imshow('window', img)
    if cv2.waitKey(1) == ord('x') :
        break;

cv2.destroyAllWindows()

