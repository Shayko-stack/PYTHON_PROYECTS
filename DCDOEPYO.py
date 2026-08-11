import cv2
import numpy as np
imagen=cv2.imread("F.png")
gray=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
ret,th=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)

contornos,jerarquia=cv2.findContours(th,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##contornos,jerarquia=cv2.findContours(th,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
##contornos,jerarquia=cv2.findContours(th,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for i in range(len(contornos)):
    cv2.drawContours(imagen,contornos,i,(0,255,0),3)
    print("contorno",i,"=",len(contornos[i]))
    cv2.imshow("imagen",imagen)
    cv2.waitKey(0)


cv2.imshow("th",th)
cv2.waitKey(0)
cv2.destroyAllWindows()
