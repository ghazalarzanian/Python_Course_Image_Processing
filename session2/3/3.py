from unittest import result
import cv2
import numpy as np

# jpg o png feshorde sazi mikonan vali TIF nmikone barae hamin dar pezeshki az in format estefade mikonan


img1 = cv2.imread("board - origin.bmp",0)
img2 = cv2.imread("board - test.bmp",0)
img2=cv2.flip(img2,1)
rows , cols = img1.shape
result = np.zeros((rows,cols),dtype='uint8')

result= cv2.subtract(img1,img2)
result=cv2.resize(result,(450,450))
cv2.imshow("output",result)
cv2.waitKey()