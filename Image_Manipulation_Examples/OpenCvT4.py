import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Dani\FALL21\cat.jpg',-1)
img_width = img.shape[1]
img_height   = img.shape[0]

img = cv2.line(img, (0,0),(img_width,img_height),(255,0,0),10)
img = cv2.line(img, (img_width,0),(0,img_height),(255,255,255),10)

img = cv2.circle(img, (img_width//2,img_height//2), 60, (255,0,255),-1)

font=cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'Test Text',(0,img_height-20),font,2,(0,0,0),3, lineType=cv2.LINE_AA)

cv2.imshow('cat',img)
cv2.waitKey(0)
cv2.destroyAllWindows()