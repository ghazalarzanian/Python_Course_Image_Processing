import cv2
import numpy as np
img_a=cv2.imread('a.tif',0)
img_b=cv2.imread('b.tif',0)

rows , cols = img_a.shape
result = np.zeros((rows,cols),dtype='uint8')

result= cv2.subtract(img_b,img_a)

cv2.imshow("output",result)
cv2.waitKey()