import cv2
import numpy as np 

# accessing the red pixel
img = cv2.imread('hel.png')
px = img[960,300]
print(px)
px1 = img[10,10]
print("\n")
print(px1)
print(img.item(10,10,2))
img.itemset((10,10,2),255)
print(img.item(10,10,2))
cv2.imshow('HELLO',img)
if cv2.waitKey(0) & 0xFF ==27 :
    cv2.destroyAllWindows()

print(img.shape)
print(img.size)
print(img.dtype)

# working with the range of pixels
'''first  in resolution the y axis is specified and y axis is specified
   and in range the x range is provided first then y range is provided'''

obj = img[300:700, 600:1200]
img[100:500, 100:700] = obj
cv2.imshow('copied',img)
if cv2.waitKey(0) & 0xFF == 27 :
    cv2.destroyAllWindows()





