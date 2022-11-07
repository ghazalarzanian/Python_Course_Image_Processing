import cv2
img = cv2.imread('4.jpg',0)
img=cv2.resize(img,(800,800))
threshold=170
for i in range(800):
    for j in range(800):
        if img[i,j]<threshold:
            img[i,j]=0
cv2.imwrite('result.jpg',img)
cv2.imshow('img',img)
cv2.waitKey()