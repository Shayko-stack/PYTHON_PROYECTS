import cv2
import numpy as np
import copy
img=cv2.imread("RGB.jpg",1)

b=copy.copy(img)
g=copy.copy(img)
r=copy.copy(img)

b[:,:,1]=0
b[:,:,2]=0

g[:,:,0]=0
g[:,:,2]=0

r[:,:,0]=0
r[:,:,1]=0

bgr=np.hstack([b,g,r])

cv2.imshow("bgr",bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
