import cv2
import numpy as np

img = np.zeros((512,512,4),np.uint8)
img = cv2.line(img,(0,511), (255,0), (0,0,255), 8)
img = cv2.line(img,(255,0), (511,511), (0,255,0), 8)

img = cv2.rectangle(img,(128,128),(384,384),(255,255,255),8)
img = cv2.circle(img,(255,255),60,(255,130,190),4)
img = cv2.ellipse(img, (320,320), (60,60), -45, 0, 270, (255.255,255), 5)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img,'This is my image', (140,255), font, 1, (255,255,255),1,cv2.LINE_AA)


#drawing a polygon


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('WhatIsThis',img)
if cv2.waitKey(0) & 0xFF == ord('q') :
    cv2.destroyAllWindows