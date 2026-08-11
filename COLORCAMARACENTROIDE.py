import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    # separar canales (matrices)
    B = frame[:,:,0]
    G = frame[:,:,1]
    R = frame[:,:,2]

    # detección simple de colores
    rojo = (R > 150) & (G < 100) & (B < 100)
    verde = (G > 150) & (R < 100) & (B < 100)
    azul = (B > 150) & (R < 100) & (G < 100)

    # convertir a imagen binaria
    rojo = rojo.astype(np.uint8) * 255
    verde = verde.astype(np.uint8) * 255
    azul = azul.astype(np.uint8) * 255

    # encontrar contornos
    contornos_r, _ = cv2.findContours(rojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos_v, _ = cv2.findContours(verde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos_a, _ = cv2.findContours(azul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # rojo
    for c in contornos_r:
        if cv2.contourArea(c) > 1000:
            x,y,w,h = cv2.boundingRect(c)

            cx = int(x + w/2)
            cy = int(y + h/2)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
            cv2.putText(frame,"X:"+str(cx)+" Y:"+str(cy),(cx,cy),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    # verde
    for c in contornos_v:
        if cv2.contourArea(c) > 1000:
            x,y,w,h = cv2.boundingRect(c)

            cx = int(x + w/2)
            cy = int(y + h/2)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame,(cx,cy),5,(0,255,0),-1)
            cv2.putText(frame,"X:"+str(cx)+" Y:"+str(cy),(cx,cy),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    # azul
    for c in contornos_a:
        if cv2.contourArea(c) > 1000:
            x,y,w,h = cv2.boundingRect(c)

            cx = int(x + w/2)
            cy = int(y + h/2)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.circle(frame,(cx,cy),5,(255,0,0),-1)
            cv2.putText(frame,"X:"+str(cx)+" Y:"+str(cy),(cx,cy),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == ord("g"):
        break

cap.release()
cv2.destroyAllWindows()
