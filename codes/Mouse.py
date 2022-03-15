import cv2
import numpy as np 

def draw_circle(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDBLCLK :
        cv2.circle(img,(x,y),50,(140,200,100),-1)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('DoUBle clICk')
cv2.setMouseCallback('DoUBle clICk',draw_circle)

while True:
    cv2.imshow('DoUBle clICk',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    elif cv2.waitKey(20) & 0xFF == ord('s') :
        cv2.imwrite("circles.jpg",img)
cv2.destroyAllWindows()
