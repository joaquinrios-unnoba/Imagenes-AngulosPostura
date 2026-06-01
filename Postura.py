from PosturaAngulo import calcular_angulos_cuerpo   # Importamos la función para calcular los ángulos del cuerpo


import cv2
import mediapipe as mp
import numpy as np


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#def dibujar_angulos(image, angulos):
#    for i, (nombre, ang) in enumerate(angulos.items()):
#        cv2.putText(image, f"{nombre}: {int(ang)}",
#            (10, 40 + i*35),          # separo un poco más las líneas
#            cv2.FONT_HERSHEY_SIMPLEX,
#            1.0,                      # tamaño más grande
#            (0, 0, 255),              # rojo (BGR)
#            2)                        # más grosor
def dibujar_angulos(image, angulos):                #Solo codo_derecho
    for i, (nombre, ang) in enumerate(angulos.items()):
        if (nombre == "codo_der") or (nombre == "hombro_der"):
            cv2.putText(image, f"{nombre}: {int(ang)} grados",
                (10, 40 + i*35),          # separo un poco más las líneas
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,                      # tamaño más grande
                (0, 0, 0),              # rojo (BGR)
                3)                        # más grosor

def dibujar_esqueleto(image, landmarks):
    mp_drawing.draw_landmarks(
        image,
        landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
    )
   
anguloMaxCodoD = 0
anguloMinCodoD = 180  
anguloMaxHombroD = 0
anguloMinHombroD = 180    
#def mostrar_panel_angulo(angulo):
#    global anguloMaxCodoD, anguloMinCodoD
#    if angulo > anguloMaxCodoD:
#        anguloMaxCodoD = angulo
#    if angulo < anguloMinCodoD:
#        anguloMinCodoD = angulo

#    panel = np.zeros((400, 400, 3), dtype=np.uint8)

    # Texto principal
#    cv2.putText(panel,
#        f"{int(angulo)} grados",
#        (70, 85),
#        cv2.FONT_HERSHEY_SIMPLEX,
#        1.5,
#        (0,255,0),
#        3)
#    # Max y Min abajo del todo
#    cv2.putText(panel,
#        f"Maximo: {int(anguloMaxCodoD)}",
#        (70, 340),
#        cv2.FONT_HERSHEY_SIMPLEX,
#        0.9,
#        (0,255,255),
#        2)

#    cv2.putText(panel,
#        f"Minimo: {int(anguloMinCodoD)}",
#        (70, 380),
#        cv2.FONT_HERSHEY_SIMPLEX,
#        0.9,
#        (255,255,0),
#        2)

    # círculo base
#    cv2.circle(panel, (200,200), 100, (255,255,255), 2)

    # línea fija
 #   cv2.line(panel, (200,200), (300,200), (255,255,255), 3)

    # línea móvil según ángulo
#    x = int(200 + 100*np.cos(np.radians(angulo)))
#    y = int(200 - 100*np.sin(np.radians(angulo)))

    #cv2.line(panel, (200,200), (x,y), (0,255,0), 4)

#    cv2.imshow("Angulo Codo Derecho", panel)     

def mostrar_panel_angulo(anguloCodo, anguloHombro):
    global anguloMaxCodoD, anguloMinCodoD, anguloMaxHombroD, anguloMinHombroD

    # ---- Actualizar máximos y mínimos ----
    if anguloCodo > anguloMaxCodoD:
        anguloMaxCodoD = anguloCodo
    if anguloCodo < anguloMinCodoD:
        anguloMinCodoD = anguloCodo

    if anguloHombro > anguloMaxHombroD:
        anguloMaxHombroD = anguloHombro
    if anguloHombro < anguloMinHombroD:
        anguloMinHombroD = anguloHombro

    # Panel más grande
    panel = np.zeros((400, 500, 3), dtype=np.uint8)

    # ======================================================
    # ================== CODO DERECHO =======================
    # ======================================================

    # Textos codo
    cv2.putText(panel, f"Codo: {int(anguloCodo)}", (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.putText(panel, f"Max:{int(anguloMaxCodoD)}", (20, 55),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 1)

    cv2.putText(panel, f"Min:{int(anguloMinCodoD)}", (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 1)

    # Centro
    centroCodo = (120, 200)

    cv2.circle(panel, centroCodo, 100, (255,255,255), 2)

    cv2.line(panel,
        centroCodo,
        (centroCodo[0] + 100, centroCodo[1]),
        (255,255,255),
        3)

    x1 = int(centroCodo[0] + 100*np.cos(np.radians(anguloCodo)))
    y1 = int(centroCodo[1] - 100*np.sin(np.radians(anguloCodo)))

    cv2.line(panel, centroCodo, (x1,y1), (0,255,0), 4)

    # ======================================================
    # ================= HOMBRO DERECHO =====================
    # ======================================================

    cv2.putText(panel, f"Hombro: {int(anguloHombro)}", (270, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.putText(panel, f"Max:{int(anguloMaxHombroD)}", (270, 55),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 1)

    cv2.putText(panel, f"Min:{int(anguloMinHombroD)}", (270, 75),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 1)

    centroHombro = (380, 200)

    cv2.circle(panel, centroHombro, 100, (255,255,255), 2)

    cv2.line(panel,
        centroHombro,
        (centroHombro[0] + 100, centroHombro[1]),
        (255,255,255),
        3)

    x2 = int(centroHombro[0] + 100*np.cos(np.radians(anguloHombro)))
    y2 = int(centroHombro[1] - 100*np.sin(np.radians(anguloHombro)))

    cv2.line(panel, centroHombro, (x2,y2), (0,255,0), 4)

    cv2.imshow("Angulos", panel)
    
def procesar_video(video):
    global anguloMaxCodoD, anguloMinCodoD, anguloMaxHombroD, anguloMinHombroD
    cap = cv2.VideoCapture(video)

    cv2.namedWindow('Pose Detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Pose Detection', 800, 600)

    print(cap.isOpened())

    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:

        while cap.isOpened():

            success, frame = cap.read()
            if not success:
                break

            # BGR → RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            # RGB → BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:

                landmarks = results.pose_landmarks.landmark
                h, w, _ = image.shape

                # 🔹 calcular ángulos
                angulos = calcular_angulos_cuerpo(landmarks, w, h)
                
                if angulos["codo_der"] > anguloMaxCodoD:     #Para guardar el angulo max del codo derecho
                    anguloMaxCodoD = angulos["codo_der"]
                if angulos["codo_der"] < anguloMinCodoD:     #Para guardar el angulo min del codo derecho
                    anguloMinCodoD = angulos["codo_der"]
                if angulos["hombro_der"] > anguloMaxHombroD:
                    anguloMaxHombroD = angulos["hombro_der"]
                if angulos["hombro_der"] < anguloMinHombroD:
                    anguloMinHombroD = angulos["hombro_der"]

                # 🔹 dibujar ángulos
                dibujar_angulos(image, angulos)

                # 🔹 dibujar esqueleto
                dibujar_esqueleto(image, results.pose_landmarks)
                
                mostrar_panel_angulo(angulos["codo_der"], angulos["hombro_der"])

            cv2.imshow('Pose Detection', image)

            if cv2.waitKey(10) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


# Ruta del video (usar / o raw string)
video_path1 = 'C:/Users/joaquin/OneDrive/Documentos/Marcha/leoMovimiento.mp4'

# un video
procesar_video(video_path1)

cv2.destroyAllWindows()