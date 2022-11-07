from turtle import shape
import cv2
img = cv2.imread('1.jpg',0)
img=cv2.resize(img,(800,800))
pixel=0
for i in range(800):
    for j in range(800):
        img[i][j]=pixel
        if j%100==0 and pixel==255:
            pixel=0
        elif j%100==0 and pixel ==0:
            pixel=255
    if i%100==0 and pixel==255:
        pixel=0
    elif i%100==0 and pixel==0:
        pixel=255
cv2.imwrite('result.jpg',img)
print(img.shape)
cv2.imshow('img',img)
cv2.waitKey()