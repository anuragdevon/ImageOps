import cv2 
import numpy as np
drawing = False  #true if mouse is pressed
mode =  True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param) :
    global ix,iy,drawing,mode

    if event ==cv2.EVENT_LBUTTONDOWN :
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE :
        if drawing == True :
            if mode == True :
                cv2.rectangle(img,(ix,iy),(x,y),(140,190,200),-1)
            else :
                cv2.circle(img,(x,y),10,(255,255,255),-1)
    elif event == cv2.EVENT_LBUTTONUP :
        drawing = False
        if mode == True :
            cv2.rectangle(img,(ix,iy),(x,y),(140,190,200),1)
        else :
            cv2.circle(img(x,y),10,(255,255,255),2)

img = np.zeros((512,512,4),np.uint8)
cv2.namedWindow('Display')
cv2.setMouseCallback('Display',draw_circle)
while True :
    cv2.imshow('Display',img)
    k = cv2.waitKey(1) &0xFF
    if k == ord('m') :
        mode = not mode
    elif k == 27 :
        break

cv2.destroyAllWindows()