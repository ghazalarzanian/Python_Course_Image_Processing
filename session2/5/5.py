import cv2
import numpy as np
image1 = cv2.imread('1.jpg',0)
image2 = cv2.imread('2.jpg',0)

row , col = image2.shape
image1=cv2.resize(image1,(col,row))

result_1=np.zeros((row,col),dtype='uint8')
result_2=np.zeros((row,col),dtype='uint8')

result_1= image1//2 +image2//2

result_2 = image2//3 + image2//3  + image1//3

Hori = np.concatenate((image1,result_1,result_2, image2), axis=1)
cv2.imwrite('result.png',Hori)
# cv2.imshow('output',Hori)
cv2.waitKey()