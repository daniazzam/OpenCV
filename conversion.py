""" 
"""

import cv2
import os

#cap = cv2.VideoCapture(0)
dirname, filename = os.path.split(os.path.abspath(__file__))

frame = cv2.imread(dirname+'\images\img2.jpeg',-1)
frame = cv2.resize(frame, (0,0) ,fx=0.5,fy=0.5)


''' we have 46.9 cm in the image horizontally
    we have 1200 pixels in the image horizontally
    we need to map pixels to 
    After rescaling by 0.5x, we get 600 pixels for 23.45 cm
'''
cm_from_pixel=23.45/600
pixel_from_cm = 600/23.45


#function to display the coordinates of point clicked
def click_event (event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, " ", y)
    

cv2.imshow('full frame',frame)

''' Starting X: 101 Ending X: 476
    Starting Y: 192 Ending Y: 571
'''
sub_frame = frame [195:570, 101:476]

cv2.rectangle(sub_frame, (0,0),(374,374), (0,0,0),2)
#cv2.imshow('sub frame', sub_frame)
#cv2.setMouseCallback('sub frame', click_event)

''' ******
    The frame is at 25 cm distance from the camera
    The blue object is at 20 cm distance from the camera
    ******
    Blue coordinates: X:152, Y: 29
    These coordinates are the output of the ML Model
    From the depth camera, we get the depth of this point, which is 20 cm
    To get the coordinate wrt 25 cm distance, using thales, apply the function below
    ******
'''

subframe_h, subframe_w, _ = sub_frame.shape
center_x, center_y = subframe_w/2, subframe_h/2

def getCoordinatesWRTCenter(coordinate_x,coordinate_y,center_x, center_y):
    return [coordinate_x-center_x,coordinate_y-center_y]

def getCoordinatesWRTFrame(coordinate_x,coordinate_y,center_x, center_y):
    return [coordinate_x+center_x,coordinate_y+center_y]

def getConversion (Model_x,Model_y,depth_z,reference_z):
    ratio_x= Model_x/depth_z
    new_x= ratio_x*reference_z

    ratio_y= Model_y/depth_z
    new_y= ratio_y*reference_z

    return [new_x,new_y]

''' Coordinates of blue object:
    X: 152 Y: 28
'''
#convert to cm
Model_x, Model_y = 152*cm_from_pixel, 28*cm_from_pixel
print('Initial coordinates in cm: X: ' + str(Model_x)+" Y: "+str(Model_y))

#get coordinates wrt center of frame (represents camera pointer)
coordinates = getCoordinatesWRTCenter(Model_x, Model_y, center_x*cm_from_pixel, center_y*cm_from_pixel)
x_wrtCenter, y_wrtCenter = coordinates[0], coordinates[1]
print('Initial coordinates in cm wrt center: X: ' + str(x_wrtCenter)+" Y: "+str(y_wrtCenter))

#get new coordinates wrt to initial frame depth
exact_coordinates = getConversion(x_wrtCenter, y_wrtCenter, depth_z=22, reference_z=25)
new_x, new_y = exact_coordinates[0], exact_coordinates[1]
print('Coordinates after conversion in cm: X: ' + str(new_x)+" Y: "+str(new_y))

#new coordinates wrt frame in pixels
excat_coordinates_wrtFrame = getCoordinatesWRTFrame(new_x*pixel_from_cm, new_y*pixel_from_cm, center_x, center_y )
new_x_wrtFrame, new_y_wrtFrame = int(excat_coordinates_wrtFrame[0]), int(excat_coordinates_wrtFrame[1])
print('new coordinates wrt frame in pixels: X: ' + str(new_x_wrtFrame)+" Y: "+str(new_y_wrtFrame))

cv2.circle(sub_frame, (new_x_wrtFrame, new_y_wrtFrame), 1, (0,0,255), 2)
cv2.imshow('sub frame', sub_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()