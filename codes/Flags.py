import cv2
flags =[i for i in dir(cv2) if i.startwith('COLOR_')]
print(flags)