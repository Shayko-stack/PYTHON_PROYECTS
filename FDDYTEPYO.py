import cv2
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((400,400,3), np.uint8)

cv2.line(img,(0,0),(400,400),(255,0,0),3)
cv2.line(img,(200,0),(200,400),(255,0,0),3)
cv2.line(img,(0,200),(400,200),(255,0,0),3)

cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)
cv2.rectangle(img,(300,100),(350,50),(0,255,0),3)

cv2.circle(img,(200,200),100,(0,0,255),2)
cv2.circle(img,(325,75),25,(0,0,255),2)

cv2.ellipse(img,(200,200),(100,50),0,0,360,(0,0,255),3)
cv2.ellipse(img,(200,200),(100,50),45,0,360,(0,0,255),3,cv2.LINE_AA)
cv2.ellipse(img,(200,200),(100,50),90,0,360,(0,0,255),3)
cv2.ellipse(img,(200,200),(100,50),135,0,360,(0,0,255),3,cv2.LINE_AA)

pts=np.array([[200,0],[400,200],[200,400],[0,200]], np.int32)
##cv2.polylines(img,[pts],False,(0,255,255),4)
cv2.polylines(img,[pts],True,(0,255,255),4)

cv2.putText(img,"CATMATH",(10,380),5,1,(255,255,255),2,cv2.LINE_AA)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),vmin=0,vmax=255,)
plt.show()
