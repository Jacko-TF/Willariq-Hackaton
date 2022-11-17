# Importamos
# las librerias
from deepface import DeepFace
import cv2
import mediapipe as mp
from functions import emocion_p1, interfaz
import webbrowser

# Declaramos la deteccion de rostros
detros = mp.solutions.face_detection
rostros = detros.FaceDetection(min_detection_confidence= 0.8, model_selection=0)
# Dibujo
dibujorostro = mp.solutions.drawing_utils

# Realizamos VideoCapturaa

cap = cv2.VideoCapture(0)

# MAIN
interfaz(detros, rostros, dibujorostro, cap, "images/entrada.png")
interfaz(detros, rostros, dibujorostro, cap, "images/entrada2.png")

#Devuelve el array con los resultados entre 0 y 1
resultados = emocion_p1(detros, rostros, dibujorostro, cap)
print(resultados)

#categorias (0,1,2,3,4)
suma = 0
for i in range (0,len(resultados)-1):
    suma += resultados[i]
#Bullying
if suma == 0:
    interfaz(detros, rostros, dibujorostro, cap, "images/opcion1.png")
    print("Según los resultados probablemente eres o has sido victima de bullying,"+
          " te invitamos a hacer tu denuncia press enter")
    t = cv2.waitKey(5)
    print(t)
    webbrowser.open("http://www.siseve.pe/Web/", new=2, autoraise=True)
#No Bullying
else:
    interfaz(detros, rostros, dibujorostro, cap, "images/cierre.png")

cv2.destroyAllWindows()
cap.release()