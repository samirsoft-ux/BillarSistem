import numpy as np
import cv2
import json

############### Trouver Caméra ###############

#se crea la ventana donde se va a mostrar
cv2.namedWindow("Camera", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#esta variable se va a referir a la primera cámara detectada
camera_number = 0

while True:
    
    #se captura un FRAME de esta primera cámara detectada
    cap = cv2.VideoCapture(camera_number)
    #se prueba si este FRAME tiene algún dato ya que en caso no lo tenga se vuelve a buscar otro FRAME
    ### DE ACÁ
    test, frame = cap.read()

    if not test:
        
        assert camera_number != 0, "No Camera Available !!!"
        camera_number = 0
        cap = cv2.VideoCapture(camera_number)
        test, frame = cap.read() # A ACÁ SE PRUEBA LO QUE DIJE ANTES
    
    #una vez se tenga el FRAME se cambia el tamaña de este a 1920x1080    
    frame = cv2.resize(frame, (1920, 1080))
    
    #este while permite que lo que tu mires parezca que es un video
    #porque lo que enrealidad captura rápidamente son FRAMES
    while True:#este while también tiene otro motivo
        #se usa en caso se quiero cambiar de cámara
        
        #acá verifica cáda FRAME recolectado, leyendo cada FRAME
        ok, frame = cap.read()
        #si todo esta ok se sigue ejecutando, en caso haya pasado algo se muestra el mensaje
        assert ok, "Camera disconnected"
        #en caso todo este ok cada frame recolectado se redimensiona
        frame = cv2.resize(frame, (1920, 1080))
        
        #aca pone este texto arriba de la ventana creada
        cv2.putText(frame,
                "Press enter to valide, or press any other touch to switch of camera :",
                (30,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1/2,
                (0,0,255),
                1,
                cv2.LINE_AA)

        #acá va mostrando cada FRAME
        cv2.imshow('Camera', frame)

        #se espera que el usuario presione una tecla para salir del bucle
        k = cv2.waitKey(1)
        if (k != -1):
            break

    #si es "enter" la tecla presionada se sale del primer while y no cambia el valor de camara_number 
    if k==13:
        break
    #si no es "enter" la tecla presionada se cambio el valor de camara_number para almacenar otra cámara
    camera_number += 1

#destruye todas las ventanas creadas
cv2.destroyAllWindows()

#se libera el recolector de FRAMES
cap.release()
#se crea el diccionario "data" y ahí se almacena el valor de camara_number | key - value
data={"camera_number": camera_number}
#toda esta info del diccionario se guarda en un archivo .json
with open('camera.json', 'w') as f:
    json.dump(data, f)

input("Calibration finished !!")
exit()
