import cv2 
import numpy as np 

img =cv2.imread('Image.jpg', 0)

cv2.imshow('img',img)  
cv2.waitKey(0)
cv2.destroyAllWindows()

rows,cols = img.shape

M=np.float32([[1,0,100], [0,1,50]])
dst = cv2.warpAffine(img, M,(cols, rows))

cv2.imshow('img', dst)  
cv2.waitKey(0)
cv2.destroyAllWindows()



#This is for testing Image in the python Openc CV code in the pyhton kernel 
#This program is used to do the translation in the image nad produce the result in the Native Window
