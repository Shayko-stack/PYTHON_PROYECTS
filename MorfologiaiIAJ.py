import cv2
import numpy as np

img=cv2.imread('RGb.jpg',0)
ret,th=cv2.threshold (img,127,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
##kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
##kernel=cv2.getStructuringElement (cv2.MORPH_ELLIPSE, (9,9))
##kernel=cv2.getStructuringElement (cv2.MORPH_CROSS, (9,9))
##
dilatacion = cv2.dilate (th, kernel, iterations = 1)
erosion = cv2.erode (th, kernel, iterations = 1)
apertura = cv2.morphologyEx (th, cv2.MORPH_OPEN, kernel)
##cierre = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
##gradiente = cv2.morphologyEx (th, cv2.MORPH_GRADIENT, kernel)
##tophat = cv2.morphologyEx(th,cv2.MORPH_TOPHAT, kernel)
##blackhat = cv2.morphologyEx (th,cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('orig',th)
##cv2.imshow('dil', dilatacion)
##cv2.imshow('ero', erosion)
##cv2.imshow('open', apertura)
##cv2.imshow('cier',cierre)
##cv2.imshow('grad',gradiente) 
##cv2.imshow('toph',tophat)
##cv2.imshow('blackh',blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
