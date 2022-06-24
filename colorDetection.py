import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\Dani\FALL21\testblue.mp4') #by 0, we access only 1 webcam

width = int(cap.get(3))
height = int(cap.get(4))

out = cv2.VideoWriter('C:/Users/Dani/FALL21/outpy.avi',cv2.VideoWriter_fourcc(*'XVID'), 30, (width,height))
while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    out.write(result)

    cv2.imshow('video',frame)
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()