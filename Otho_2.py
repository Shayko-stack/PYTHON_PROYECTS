import cv2
import numpy as np
img=cv2.imread('RGB.jpg',0)
A=img.copy()/255

m,n= A.shape
B=np.zeros((m,n));
i= 2
j= 2

h=np.array([[-1, -1, -1], [-1, 8, 1], [-1,-1,-1]])
for i in range(m-1):
    for j in range(n-1):
        B[i,j]=( h[0,0] * A[i -1, j -1] +h [0,1] * A[i -1, j] +h [0, 2] * A[i - 1, j + 1]
                  +h [1,0]*A[i,j-1] +h [1,1]*A[i,j] +h [1,2]*A[i,j+1]
                  +h[2,0]* A [i + 1, j + 1] +h[2,1]*A[i+1,j] +h [2,2]*A[i+1,j+1])
        B[i,j]=abs(B[i,j])

cv2.imshow('img',img)
cv2.imshow('imgb',B)
cv2.waitKey(0)
cv2.destroyAllWindows()
