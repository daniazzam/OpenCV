import numpy as np
import cv2
 

img = cv2.imread(r'C:\Users\Dani\FALL21\cat.jpg',-1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 1) #returns floating pt values
corners = np.int0(corners) #turn into integers

for corner in corners:
    x, y = corner.ravel() #flatens the array (removes interior array) [[x,y]]==>[x,y]
    cv2.circle(img, (x,y), 5, (255,0,0), -1)


cv2.imshow('frame',img)

cv2.waitKey(0)
cv2.destroyAllWindows()