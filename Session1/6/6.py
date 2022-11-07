import cv2
img = cv2.imread('1.jpg',0)
img=cv2.resize(img,(255,255))
pixel=255
for i in range(255):
    for j in range(255):
        img[i][j]=pixel
    pixel-=1
cv2.imshow('img',img)
cv2.waitKey()
    