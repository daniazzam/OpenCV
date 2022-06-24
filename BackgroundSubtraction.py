import numpy as np
import cv2 
import os

#cap = cv2.VideoCapture(0)
dirname, filename = os.path.split(os.path.abspath(__file__))
while True:
    # _,frame = cap.read()
    frame = cv2.imread(dirname+'\images\img1.jpeg',-1)
    frame = cv2.resize(frame, (0,0) ,fx=0.5,fy=0.5)
    
    gray_image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('background',gray_image1)

    k = cv2.waitKey(0) & 0xff  
    if k == 27: 
        break 

while True:
    # _, frame = cap.read()
    frame = cv2.imread(dirname+'\images\img2.jpeg',-1)
    frame = cv2.resize(frame, (0,0) ,fx=0.5,fy=0.5)
    
    gray_image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('foreground',gray_image2)

    differnece = np.absolute(np.matrix(np.int16(gray_image2))-np.matrix(np.int16(gray_image1)))
    differnece[differnece>255] = 255
    differnece = np.uint8(differnece)

    cv2.imshow('Difference',differnece)

    BW=differnece
    BW[BW<=100]=0
    BW[BW>100]=1

    k = cv2.waitKey(1) & 0xff  
    if k == 27: 
        break 

cv2.destroyAllWindows()

height, width= differnece.shape

column_sum = np.matrix(np.sum(BW,0))
column_number = np.matrix(np.arange(width)) 
column_multiply = np.multiply(column_sum,column_number)
totalc = np.sum(column_multiply)
total_totalc = np.sum(np.sum(BW))
column_loc = totalc/total_totalc

print('X: ' +str(int(column_loc)))
print(frame.shape)    