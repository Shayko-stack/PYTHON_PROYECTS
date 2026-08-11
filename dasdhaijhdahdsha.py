import cv2
import numpy as np
img=cv2.imread("M.png")

gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th=cv2.threshold(gris,200,255,cv2.THRESH_BINARY_INV)

img2=th.copy()
h,w=img2.shape
mask=np.zeros((h+2,w+2), np.uint8)

cv2.floodFill(img2,mask,(0,0),255)
inv=cv2.bitwise_not(img2)

sinhuecos= th | inv

cv2.imshow("img",img)
cv2.imshow("th",th)
cv2.imshow("relleno",img2)
cv2.imshow("negada",inv)
cv2.imshow("sinhuecos",sinhuecos)

cv2.waitKey(0)
cv2.destroyAllWindows()
