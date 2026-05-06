from PosturaAngulo import calcular_angulos_cuerpo   # Importamos la función para calcular los ángulos del cuerpo


import cv2
import mediapipe as mp
import numpy as np


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def dibujar_angulos(image, angulos):
    for i, (nombre, ang) in enumerate(angulos.items()):
        cv2.putText(image, f"{nombre}: {int(ang)}",
            (10, 40 + i*35),          # separo un poco más las líneas
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,                      # tamaño más grande
            (0, 0, 255),              # rojo (BGR)
            2)                        # más grosor

def dibujar_esqueleto(image, landmarks):
    mp_drawing.draw_landmarks(
        image,
        landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
    )

def procesar_video(video):

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

                # 🔹 dibujar ángulos
                dibujar_angulos(image, angulos)

                # 🔹 dibujar esqueleto
                dibujar_esqueleto(image, results.pose_landmarks)

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