import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread("M.png")
f = img.copy()

cv2.floodFill(f,None,(20,20),(200,0,0),(7,7,7,7),(7,7,7,7))
cv2.circle(f,(20, 20),4,(0,0,255),2)

cv2.floodFill(f,None,(84,84),(170,0,0),(7,7,7,7),(7,7,7,7))
cv2.circle(f,(84, 84),4,(0,0,255),2)

cv2.floodFill(f,None,(77, 50),(0,170,0),(7,7,7,7),(7,7,7,7))
cv2.circle(f,(77, 50),4,(0,0,255),2)

imgs=[img,f]
t=["original","rellenado"]

for i in range (2):
    plt.subplot(1,2,i+1)
    plt.imshow(cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB),vmin=0, vmax=255)
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()
