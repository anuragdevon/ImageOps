import numpy as np
import cv2

img = cv2.imread('C:\\Users\\anurag\\Pictures\\Image.jpg', 0)
cv2.imshow('Image', img)
cv2.waitkey(0)
cv2.destroyAllWindows() 