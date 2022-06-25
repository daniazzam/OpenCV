import numpy as np
import cv2 
import os

#cap = cv2.VideoCapture(0)
dirname, filename = os.path.split(os.path.abspath(__file__))

frame = cv2.imread(dirname+'\images\img1.jpeg',-1)
frame = cv2.resize(frame, (0,0) ,fx=0.5,fy=0.5)
print(frame.shape)  

''' we have 46.9 cm in the image horizontally
    we have 1200 pixels in the image horizontally
    we need to map pixels to 
    After rescaling by 0.5x, we get 600 pixels for 23.45 cm
'''
cm_to_pixel=23.45/600

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

X_location = column_loc * cm_to_pixel

row_sum = np.matrix(np.sum(BW,1))
row_sum = row_sum.transpose()
row_number = np.matrix(np.arange(height)) 
row_multiply = np.multiply(row_sum,row_number)
totalr = np.sum(row_multiply)
total_totalr = np.sum(np.sum(BW))
row_loc = totalr/total_totalr

Y_location = row_loc * cm_to_pixel


print('X: ' +str(int(column_loc)) +'\nY: '+str(int(row_loc)))
print('X: ' +str(X_location) +' cm\nY: '+str(Y_location)+' cm') 