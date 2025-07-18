# Store the captured video

import cv2

cap =cv2.VideoCapture(0)
# store the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20,(640,480))

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame, 1)

    out.write(frame)  # frame storing

    cv2.imshow('Webcam',frame)

    if cv2.waitKey(1) == ord('x'):
        break

out.release()
cv2.destroyAllWindows()