import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('RGB.jpg', 0)
u,th1=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
u,th2=cv2.threshold (img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
u,th3=cv2.threshold (img,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
u,th4=cv2.threshold (img,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
u,th5=cv2.threshold(img,0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)

imagenes=[img,th1,th2,th3,th4,th5]
titulo=['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

for i in range(6):
    plt.subplot (3,2,i+1)
    plt.imshow(imagenes[i], 'gray',vmin=0,vmax=255);
    plt.title(titulo [i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
print(u)
