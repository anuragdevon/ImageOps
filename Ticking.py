import cv2

e1=cv2.getTickCount()
e2=cv2.getTickCount()
time=(e2-e1)/cv2.getTickFrequency()
print(time)