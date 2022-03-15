import numpy as np
import cv2

pts = np.array([[10,5], [20,30], [70,20], [50,10]],np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.ploylines(img,[pts],True,(0,255,255))

