import cv2
import  numpy as np 

def nothing(x) :
    pass

# Create Black window image
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Trackbar')

# create trackbar for color changes
cv2.createTrackbar('R','Trackbar',0,255,nothing)
cv2.createTrackbar('G','Trackbar',0,255,nothing)
cv2.createTrackbar('B','Trackbar',0,255,nothing)

# create switch for On/Off functionality
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch,'Trackbar',0,1,nothing)

# entering while loop
while(1) :
    cv2.imshow('Trackbar',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 :
        break
    
    #getting the current positions of 4 trackbars
    r = cv2.getTrackbarPos('R','Trackbar')
    r = cv2.getTrackbarPos('R','Trackbar')
    r = cv2.getTrackbarPos('R','Trackbar')
    r = cv2.getTrackbarPos('R','Trackbar')
    if k == 0 :
        img[:] = 0
    else :
        
   
        


cv2.destroyAllWindows
