import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("r.png")
cv2.imshow("original",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/9
f1=cv2.filter2D(img,-1,kernel)
f2=cv2.blur(img,(5,5))
f3=cv2.GaussianBlur(img,(5,5),0)
f4=cv2.medianBlur(img,5)

f=[f1,f2,f3,f4]
t=["Convolucion", "promedio", "Gaussiano", "medianBlur"]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(f[i], vmin=0, vmax=255)
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
