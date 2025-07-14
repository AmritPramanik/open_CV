# Drawing shapes
# it is use for object tracking

import cv2
import numpy as np

img = np.zeros((512,512,3))

# Rectangle
cv2.rectangle(img,(50,50),(250,250),color=(0,0,255),thickness=2)

# Circle
cv2.circle(img,(250,250),50,(255,0,0),2)

# Line
cv2.line(img,(50,50),(250,250),(0,255,0),2)

cv2.rectangle(img,(50,35),(100,50),color=(0,0,255),thickness=-1)
# Text
cv2.putText(img,org=(55,45),fontScale=0.5,color=(255,255,255),thickness=1,lineType=cv2.LINE_AA,text="AMRIT",fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)

# if thickness = -1 then it fill the area

cv2.imshow('window',img)
cv2.waitKey(0)