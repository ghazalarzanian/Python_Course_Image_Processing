import cv2

img = cv2.imread('3.jpg',0)
img=cv2.resize(img,(1000,700))
height ,width = img.shape
list = [] 
index=0
temp=0
for i in reversed(range(height)):
    for j in reversed(range(width)):
        list.append(img[i,j])
        
index=0
for i in range(height):
    for j in range(width):
        img[i,j]=list[index]
        index+=1
cv2.imshow('img',img)
cv2.waitKey()