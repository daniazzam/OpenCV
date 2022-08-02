''' This code gets the coordinate of a floating object
    in the predefined frame, wrt to a depth measured from
    a 3d camera
'''
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
_,frame = cap.read()
frame_y, frame_x, _ = frame.shape

''' we have 46 cm in the image width
    we have 480 pixels in the image horizontally
    we need to map pixels to cm
    480 pixels ==> 42.5 cm 
'''
cm_from_pixel=46.0/600
pixel_from_cm=600/46.0

'''function to display the coordinates of point clicked'''
def click_event (event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
        return [x,y]
#cv2.setMouseCallback('background', click_event)

''' ROI Boundaries:
    (155,91)==>(454,390)
    299 pixels width and height
'''

def getCoordinatesWRTCenter(coordinate_x,coordinate_y,center_x, center_y):
    return coordinate_x-center_x,coordinate_y-center_y

def getCoordinatesWRTFrame(coordinate_x,coordinate_y,center_x, center_y):
    return coordinate_x+center_x,coordinate_y+center_y

def getConversion (Model_x,Model_y,depth_z,reference_z):
    ratio_x= Model_x/depth_z
    new_x= ratio_x*reference_z

    ratio_y= Model_y/depth_z
    new_y= ratio_y*reference_z

    return new_x,new_y

while True:
    _,frame = cap.read()
    frame =cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    ROI_frame = frame [155:454, 91:390]

    gray_image1 = cv2.cvtColor(ROI_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('background',gray_image1)

    k = cv2.waitKey(1) & 0xff  
    if k == 27: 
        break 

while True:
    _, frame = cap.read()
    frame =cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    ROI_frame = frame [155:454, 91:390]

    ROI_h, ROI_w, _ = ROI_frame.shape
    ROI_x_center, ROI_y_center = ROI_w/2, ROI_h/2

    gray_image2 = cv2.cvtColor(ROI_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('foreground',gray_image2)

    difference = np.absolute(np.matrix(np.int16(gray_image2))-np.matrix(np.int16(gray_image1)))
    difference[difference>255] = 255
    difference = np.uint8(difference)

    cv2.imshow('Difference',difference)

    BW=difference
    BW[BW<=100]=0
    BW[BW>100]=1

    height, width= difference.shape

    column_sum = np.matrix(np.sum(BW,0))
    column_number = np.matrix(np.arange(width)) 
    column_multiply = np.multiply(column_sum,column_number)
    totalc = np.sum(column_multiply)
    total_totalc = np.sum(np.sum(BW))
    
    if total_totalc != 0:
        column_loc = totalc/total_totalc
    else:
        column_loc = 155+150
    coilumn_loc = int(column_loc)

    row_sum = np.matrix(np.sum(BW,1))
    row_sum = row_sum.transpose()
    row_number = np.matrix(np.arange(height)) 
    row_multiply = np.multiply(row_sum,row_number)
    totalr = np.sum(row_multiply)
    total_totalr = np.sum(np.sum(BW))
    
    if total_totalr != 0:
        row_loc = totalr/total_totalr
    else:
        row_loc = 155+150
    row_loc=int(row_loc)

    if column_loc>0 and row_loc>0:
        cv2.circle(ROI_frame,(int(column_loc),int(row_loc)),1,(0,0,255),2)
        
        #print('X: ' +str(int(column_loc)) +'\nY: '+str(int(row_loc)))

        row_loc_cm = row_loc * cm_from_pixel
        column_loc_cm = column_loc * cm_from_pixel
        #print('Initial coordinates in cm: X: ' + str(column_loc_cm)+" Y: "+str(row_loc_cm))

        #get coordinates wrt center of ROI (represents camera pointer)
        x_wrtCenter, y_wrtCenter = getCoordinatesWRTCenter(column_loc_cm, row_loc_cm, ROI_x_center*cm_from_pixel, ROI_y_center*cm_from_pixel)
        #print('Initial coordinates in cm wrt center: X: ' + str(x_wrtCenter)+" Y: "+str(y_wrtCenter))

        #get new coordinates wrt to initial frame depth
        depth_z=45
        new_x_cm, new_y_cm  = getConversion(x_wrtCenter, y_wrtCenter, depth_z=depth_z, reference_z=50)
        #print('Coordinates after conversion in cm: X: ' + str(new_x_cm)+" Y: "+str(new_y_cm))

        cv2.putText(frame, f'X: {x_wrtCenter:.1f} | Y: {y_wrtCenter:.1f} | Z: {50-depth_z} (cm)', (int(91+column_loc-72),
                    int(155+row_loc-5)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.3, (0,0,255), 1)

        #new coordinates wrt frame in pixels
        new_x_wrtFrame, new_y_wrtFrame = getCoordinatesWRTFrame(new_x_cm * pixel_from_cm, new_y_cm * pixel_from_cm, ROI_x_center, ROI_y_center )
        #print('new coordinates wrt frame in pixels: X: ' + str(new_x_wrtFrame)+" Y: "+str(new_y_wrtFrame))

        cv2.line(ROI_frame, (int(ROI_x_center),int(ROI_y_center)), (int(new_x_wrtFrame),int(new_y_wrtFrame)), (0,0,0), 1) 
        cv2.circle(ROI_frame,(int(new_x_wrtFrame),int(new_y_wrtFrame)),1,(255,0,0),2) 
        cv2.putText(frame, f'X: {new_x_cm:.1f} | Y: {new_y_cm:.1f} | Z: 0 (cm)', (int(91+new_x_wrtFrame-72),int(155+new_y_wrtFrame-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,0,0), 1)
    cv2.imshow('final ROI',ROI_frame)
    cv2.imshow('Camera',frame)
    k = cv2.waitKey(1) & 0xff  
    if k == 27: 
        break 

cv2.destroyAllWindows()

 