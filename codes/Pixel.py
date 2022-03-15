import numpy as np 
import cv2


img = cv2.imread('hel.png')
px = img[100,100]
print(px)
blue = img[100,100,1]
print(blue)
img[100,100] = [255,255,255]
print(img[100,100])
cv2.imshow('Modified',img)
if cv2.waitKey(0) & 0xFF == 27 :
    cv2.destroyAllWindows()