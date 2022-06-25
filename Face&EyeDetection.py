import numpy as np
import cv2

cap = cv2.VideoCapture(0)

'''
HAAR Cascade is a pre-trained classifier that picks
specific features in and image 
https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
'''
FaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
EyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

while True:
    _,frame = cap.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = FaceCascade.detectMultiScale(grayFrame)
    i=0
    for (x, y, w, h) in faces:
        cv2.putText(frame, 'Face'+str(i), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (36,255,12), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

        #roi : region of interest
        roi_gray  = grayFrame[y:y+h, x:x+h]

        eyes = EyeCascade.detectMultiScale(roi_gray)
        j=0
        for (x2,y2,w2,h2) in eyes:
            cv2.putText(frame, 'eye'+str(j), (x+x2, y+y2-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
            frame = cv2.rectangle(frame, (x+x2, y+y2), (x + x2 + w2, y + y2 + h2), (0,255,0), 3 )
            j+=1
        i+=1
    cv2.imshow('frame',frame)

    #press esc to exit
    k = cv2.waitKey(1) & 0xff  
    if k == 27: 
        break

cap.release()
cv2.destroyAllWindows()