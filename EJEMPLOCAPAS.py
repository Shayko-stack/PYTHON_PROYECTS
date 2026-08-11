import cv2
import numpy as np
img=cv2.imread("RGB.jpg",1)
cv2.imshow("RGB_IMAGWEN",img)
#cv2.imwrite("vergilsentado.png",img)
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
bgr=np.hstack([b,g,r])
cv2.imshow("capas",bgr)

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
r1=rgb[:,:,0]
g1=rgb[:,:,1]
b1=rgb[:,:,2]
rgb1=np.hstack([r1,g1,b1])
cv2.imshow("capas 2",rgb1)

cv2.waitKey(0)
cv2.destroyAllWindows()
