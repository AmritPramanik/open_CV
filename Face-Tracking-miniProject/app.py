# Face Tracking System
import cv2

# haarcascade_frontalface_default.xml" if use for face stucture detection
face_cap = cv2.CascadeClassifier("C:/Users/prama/AppData/Roaming/Python/Python313/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

while True:
    ret,frame = video_cap.read()
    frame = cv2.flip(frame,1)

    col = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # B/W image help to identify the more facial structure
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # create the rectangle
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=2)

    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) == ord('x'):
        break

video_cap.release()
cv2.destroyAllWindows()