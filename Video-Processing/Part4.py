# play the video

import cv2
import time

video = cv2.VideoCapture('video/sample.mp4')

while True:
    ret,frame = video.read()
    # machin play fast to get actual speed we use sleep(1/24) because this video fps is 24
    time.sleep(1/24)

    cv2.imshow('window',frame)
    if cv2.waitKey(1) == ord('x'):
        break

video.release()
cv2.destroyAllWindows()