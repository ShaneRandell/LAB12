import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.line(frame,(0,0),(511,511),(255,0,0),2)
    cv.rectangle(frame,(100,100),(300,300),(0,255,0),2)
    cv.circle(frame,(400,300),100,(0,0,255),2)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'Embedded Systems Class',(10,300), font, 2,(255,255,255),2,cv.LINE_AA)
    # Display the resulting frame
    cv.imshow('frame in Gray', gray)
    cv.imshow('frame in Colour', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

