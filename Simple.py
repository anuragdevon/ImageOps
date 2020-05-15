import cv2

img=cv2.imread(r'sor.jpg',0)
cv2.imshow('This is my window',img)
k=cv2.waitKey(0) & 0xFF
if k == 27 :
    cv2.destroyAllWindows()
elif k == ord('s') :
    cv2.imwrite('sor1.jpg',img)
    cv2.destroyAllWindows()
    