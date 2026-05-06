import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def calcular_angulo(a, b, c): #Calcula el ángulo entre tres puntos a, b y c (hombro,codo,muñeca)
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cos_angulo = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angulo = np.arccos(cos_angulo)

    return np.degrees(angulo)

def get_point(landmarks, landmark, w, h):
    return [
        landmarks[landmark].x * w,
        landmarks[landmark].y * h
    ]


def calcular_angulos_cuerpo(landmarks, w, h):
    angulos = {}

    # LADO DERECHO
    shoulder_r = get_point(landmarks, mp_pose.PoseLandmark.RIGHT_SHOULDER, w, h)
    elbow_r    = get_point(landmarks, mp_pose.PoseLandmark.RIGHT_ELBOW, w, h)
    wrist_r    = get_point(landmarks, mp_pose.PoseLandmark.RIGHT_WRIST, w, h)
    hip_r      = get_point(landmarks, mp_pose.PoseLandmark.RIGHT_HIP, w, h)
    knee_r     = get_point(landmarks, mp_pose.PoseLandmark.RIGHT_KNEE, w, h)
    ankle_r    = get_point(landmarks, mp_pose.PoseLandmark.RIGHT_ANKLE, w, h)

    # LADO IZQUIERDO
    shoulder_l = get_point(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER, w, h)
    elbow_l    = get_point(landmarks, mp_pose.PoseLandmark.LEFT_ELBOW, w, h)
    wrist_l    = get_point(landmarks, mp_pose.PoseLandmark.LEFT_WRIST, w, h)
    hip_l      = get_point(landmarks, mp_pose.PoseLandmark.LEFT_HIP, w, h)
    knee_l     = get_point(landmarks, mp_pose.PoseLandmark.LEFT_KNEE, w, h)
    ankle_l    = get_point(landmarks, mp_pose.PoseLandmark.LEFT_ANKLE, w, h)

    # CODO
    angulos["codo_der"] = calcular_angulo(shoulder_r, elbow_r, wrist_r)
    angulos["codo_izq"] = calcular_angulo(shoulder_l, elbow_l, wrist_l)

    # HOMBRO
    angulos["hombro_der"] = calcular_angulo(elbow_r, shoulder_r, hip_r)
    angulos["hombro_izq"] = calcular_angulo(elbow_l, shoulder_l, hip_l)

    # CADERA
    angulos["cadera_der"] = calcular_angulo(shoulder_r, hip_r, knee_r)
    angulos["cadera_izq"] = calcular_angulo(shoulder_l, hip_l, knee_l)

    # RODILLA
    angulos["rodilla_der"] = calcular_angulo(hip_r, knee_r, ankle_r)
    angulos["rodilla_izq"] = calcular_angulo(hip_l, knee_l, ankle_l)

    return angulos