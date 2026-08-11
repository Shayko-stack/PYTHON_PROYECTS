import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("RGB.jpg",0)
cv2.imshow("RGB",img)

hist=cv2.calcHist([img],[0],None, [256],[0,256])

fig,ax=plt.subplots(2,2)
ax[0,0].imshow(img,cmap="gray")
ax[0,0].set_title("Bros")
ax[0,0].axis("off")

ax[0,1].plot(hist, color="gray")
ax[0,1].set_title("Bros")

ax[1,0].imshow(img,cmap="gray")
ax[1,0].set_title("Bros")
ax[1,0].axis("off")

ax[1,1].hist(img.ravel(),256,[0,256])
ax[1,1].set_title("Bros")

plt.show()

u,th=cv2.threshold(img,175,255,cv2.THRESH_BINARY)
cv2.imshow('img',th)

cv2.waitKey(0)
cv2.destroyAllWindows()
