import cv2
import numpy as np

highway=[]
for i in range (15):
    img=cv2.imread(f'h{i}.jpg',0)
    highway.append(img)
    rows , cols = img.shape

result=np.zeros((rows,cols),dtype='uint8')
for img in highway:
    result+=img//15


print (result)
cv2.imwrite('result.jpg',result)
cv2.imshow('output',result)
cv2.waitKey()