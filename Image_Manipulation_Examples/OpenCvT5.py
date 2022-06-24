import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Dani\FALL21\blue_img.jfif',-1)
img_width = img.shape[1]
img_height   = img.shape[0]

#change to HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#range of colors to be detected
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_blue,upper_blue) #returns a new mask(0s and 1s) of the image that have only the blue pixels existing

result = cv2.bitwise_and(img, img, mask=mask)   #blends first 2 sources, determines whether to keep the pixels or remove them
                                                # using the mask (comapring bits from mask to bits from our image)

# method to get the hsv values of an rgb color
# BGR_Color = np.array([[[255,0,0]]])
# HSV_Color = cv2.cvtColor(BGR_Color,cv2.COLOR_BGR2HSV)
# HSV_Color[0][0]
cv2.imshow('cat_',img)
cv2.imshow('cat',result)
cv2.waitKey(0)
cv2.destroyAllWindows()