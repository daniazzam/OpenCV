import cv2
import random

img = cv2.imread(r'C:\Users\Dani\FALL21\cat.jpg',-1)
print(type(img))
print(img.shape)
img = cv2.resize(img,(0,0),fx=1,fy=1)

for i in range(0,100):
    for j in range(img.shape[1]):  #img.shape[1] gives the # of column pixels where the output of shape is [#rows,#columns,#channels] 
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

###################
#copy part of an image
part = img [100:350,50:150]
cv2.imshow('part',part)

cv2.imshow('cat',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(img.shape)