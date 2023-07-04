


import numpy as np
import cv2

cap = cv2.VideoCapture(0);

while True:
    leido, frame = cap.read();    
    cv2.imshow('Visor',frame);

    if cv2.waitKey(1) &0xFF < ord('q'):
        cv2.imwrite("foto.png",frame);
        print("Foto tomada correctamente")
        break;

cap.release();
cv2.destroyAllWindows()        
