import time
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r'C:\Users\Dani\FALL21\testblue.mp4') #cap is an object of the VideoCapture Class
                                                            #by specifying a directory, we ask to get the video already captured from the directory                                                            
                                                            #by 0, we access only 1 webcam

while True:
    ret, frame = cap.read()
    height=int(cap.get(4))
    width=int(cap.get(3))

    image = np.zeros(frame.shape, np.uint8) #(shape, type: unsigned integer 8bits)

    smaller_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv.rotate(smaller_frame, cv.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv.rotate(smaller_frame, cv.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv.imshow('frame',image)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()