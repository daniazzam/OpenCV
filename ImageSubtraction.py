from pickletools import uint8
import numpy as np
import cv2 

#cap = cv2.VideoCapture(0)

while True:
    #_, frame = cap.read()
    frame = cv2.imread(r'C:\Users\Dani\Desktop\30x30.jpeg',-1)
    frame = cv2.resize(frame, (0,0) ,fx=0.5,fy=0.5)

    height, width, _ = frame.shape
    print('height is: '+str(int(height))+' and width is: '+str(int(width)))

    
    red   = np.matrix(frame[:,:,2])
    green = np.matrix(frame[:,:,1])
    blue  = np.matrix(frame[:,:,0])

    # green_only = np.int16(green)-np.int16(blue)
    # green_only[green_only<0]=0
    # green_only[green_only>255]=255
    # green_only = np.uint8(green_only)

    '''
        Now we will be getting the center of brightness
    '''
    column_sum = np.matrix(np.sum(green,0))
    column_number = np.matrix(np.arange(width)) 
    column_multiply = np.multiply(column_sum,column_number)
    totalc = np.sum(column_multiply)
    total_totalc = np.sum(np.sum(green))
    column_loc = totalc/total_totalc

    row_sum = np.matrix(np.sum(green,1))
    row_number = np.matrix(np.arange(height)) 
    row_multiply = np.multiply(row_sum,row_number)
    totalr = np.sum(row_multiply)
    total_totalr = np.sum(np.sum(green))
    row_loc = totalr/total_totalr

    print('X: ' +str(int(column_loc)) +'\nY: '+str(int(row_loc)))

    cv2.imshow('rgb', frame)
    #cv2.imshow('red', red)
    cv2.imshow('green', green)
    #cv2.imshow('blue', blue)

    #cv2.imshow('green only',green_only)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break

print(frame.shape)    