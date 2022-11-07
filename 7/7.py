import cv2
import numpy as np
result = np.zeros((400,400),dtype='uint8')
result[0:20,40:80]=255
result[20:60,20:40]=255
result[60:80,40:80]=255
result[40:70,80:95]=255
result[30:40,60:100]=255
cv2.imshow('image',result)
cv2.waitKey()