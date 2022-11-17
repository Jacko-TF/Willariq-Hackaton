# Importamos las librerias
from deepface import DeepFace
import cv2
import mediapipe as mp

def emocion_p1(detros,rostros,dibujorostro,cap):
    #puntuaciones de los 4 indicadores
    pp1 = 0
    pp2 = 0
    pp3 = 0
    pp4 = 0
    imagen = "images\inicio.png"
    while True:
        # Leemos los fotogramas
        ret, frame = cap.read()
        # Leemos imagen
        img = cv2.imread(imagen)
        img = cv2.resize(img, (0, 0), None, 0.30, 0.30)
        ani, ali, c = img.shape

        # Correccion de color
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Procesamos
        resrostros = rostros.process(rgb)

        # Deteccion
        if resrostros.detections is not None:
            # Registramos
            for rostro in resrostros.detections:
                # Extraemos informacion de ubicacion
                al, an, c = frame.shape
                box = rostro.location_data.relative_bounding_box
                xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
                xf, yf = xi + w, yi + h

                # Dibujamos
                cv2.rectangle(frame, (xi, yi), (xf, yf), (500, 500, 0), 1)
                frame[10:ani + 10, 10:ali+10] = img

                # Informacion
                info = DeepFace.analyze(rgb, actions=['age', 'gender', 'race', 'emotion'], enforce_detection= False)

                # Emociones
                emociones = info['dominant_emotion']

                print("Estado de ánimo: " + str(emociones))

                # Puntuacion
                n = emocion(emociones)
                if imagen == "images\p1.png":
                    pp1 += n
                elif imagen == "images\p2.png":
                    pp2 += n
                elif imagen == "images\p3.png":
                    pp3 += n
                elif imagen == "images\p4.png":
                    pp4 += n

                #Traduccion
                emociones = traduccion(emociones)

                # Mostramos info
                if imagen != "images\inicio.png":
                    cv2.putText(frame, str(emociones), (200, 280), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # Mostramos los fotogramas
        cv2.imshow("Willariq", frame)

        # Leemos el teclado
        t = cv2.waitKey(5)
        print(t)
        #MENU
        if t == 13:
            array = [estado(pp1), estado(pp2), estado(pp3), estado(pp4)]
            return array
            break
        elif t == 49:
            print("pregunta1")
            imagen = "images\p1.png"
        elif t == 50:
            print("pregunta2")
            imagen = "images\p2.png"
        elif t == 51:
            print("pregunta3")
            imagen = "images\p3.png"
        elif t == 52:
            print("pregunta4")
            imagen = "images\p4.png"
        elif t == 27:
            break

def estado(n):
    if n > 0:
        return 1
    else:
        return 0

def interfaz(detros,rostros,dibujorostro,cap, path):
    image = cv2.imread(path)
    image = cv2.resize(image, (0, 0), None, 0.7, 0.7)
    window_name = 'Willariq'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def emocion(emociones):
    n = 0
    if emociones == 'angry':
        n = -1
    if emociones == 'disgust':
        n = -1
    if emociones == 'fear':
        n = -1
    if emociones == 'happy':
        n = 1
    if emociones == 'sad':
        n = -1
    if emociones == 'surprise':
        n = -1
    return n

def traduccion(emociones):
    if emociones == 'angry':
        emociones = 'enojado'
    if emociones == 'disgust':
        emociones = 'disgustado'
    if emociones == 'fear':
        emociones = 'miedoso'
    if emociones == 'happy':
        emociones = 'feliz'
    if emociones == 'sad':
        emociones = 'triste'
    if emociones == 'surprise':
        emociones = 'sorprendido'
    if emociones == 'neutral':
        emociones = 'neutral'
    return emociones