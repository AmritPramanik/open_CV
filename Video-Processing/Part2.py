# Convert the video into grey scale

import cv2

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    new_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.imshow('webcam',new_frame)
    if cv2.waitKey(1) == ord('x'):
        break
cv2.destroyAllWindows()