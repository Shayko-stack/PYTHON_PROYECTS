import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('RGB.jpg', 0)
u,th1=cv2.threshold (img,127,255,cv2.THRESH_BINARY)
u,th2=cv2.threshold (img,127,255,cv2.THRESH_BINARY_INV)
u, th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
u,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
u,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)



plt.subplot(3,2,1)
plt.imshow(img, 'gray',vmin=0,vmax=255); plt.title('Original')
plt.xticks(()), plt.yticks([])

plt.subplot(3,2,2)
plt.imshow(th1,'gray',vmin=0,vmax=255); plt.title('BINARY')
plt.xticks(()), plt.yticks([])

plt.subplot(3,2,3)
plt.imshow(th2, 'gray',vmin=0,vmax=255);plt.title('BINARY INV')
plt.xticks(()), plt.yticks([])

plt.subplot(3,2,4)
plt.imshow(th3, 'gray',vmin=0,vmax=255); plt.title('TRUNC')
plt.xticks(()), plt.yticks([])

plt.subplot(3,2,5)
plt.imshow(th4, 'gray',vmin=0,vmax=255); plt.title('TOZERO')
plt.xticks(()), plt.yticks([])

plt.subplot (3,2,6)
plt.imshow(th5, 'gray',vmin=0,vmax=255); plt.title('TOZERO_INV')
plt.xticks(()), plt.yticks([])

plt.show()
print(u)
