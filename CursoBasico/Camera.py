import cv2;

cap = cv2.VideoCapture(0);
leido,frame = cap.read();

if leido==True:
    cv2.imwrite("foto.png",frame);
    print("Foto tomada correctamente:> ");
else:
    print("Error, no se tomo la foto: ");

cap.release();