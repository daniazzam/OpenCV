import cv2

img = cv2.imread(r'C:\Users\Dani\Desktop\30x30.jpeg',-1)
print(img.shape)

# imgS = cv2.resize(img, (0,0) ,fx=0.5,fy=0.5)
# print(imgS.shape)
# cv2.imshow('resized frame',imgS)


''' we have 46.9 cm in the image horizontally
    we have 768 pixels in the image horizontally
    we need to map pixels to cm
'''

cm_to_pixel = 46.9/768.0

cv2.imshow('full frame',img)


cv2.waitKey(0)
cv2.destroyAllWindows()