import cv2

img = cv2.imread(r'C:\Users\Dani\FALL21\cat.jpg',-1)
#img = cv2.resize(img, (400,400))
img = cv2.resize(img, (0,0), fx=0.5,fy=0.5) #this shrinks the image by a scale of 2

print(img.shape) #shape[2] represents the number of channels
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('newimage.jpg',img)
print(img[0][0])
cv2.imshow('Cat', img)

cv2.waitKey() #wait infinite amount of time untill a key is pressed
cv2.destroyAllWindows()
