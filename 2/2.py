import cv2

img1 = cv2.imread('1.jpg',0)
img2 = cv2.imread('2.jpg',0)
height , width = img1.shape
for i in range(height):
    for j in range(width):
        img1[i,j]=255-img1[i,j]
height , width = img2.shape
for i in range(height):
    for j in range(width):
        img2[i,j]=255-img2[i,j]
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()