import tkinter as tk
from tkinter import filedialog
import cv2
import mediapipe as mp
from PIL import Image, ImageTk
from PosturaFrame import procesar_frame

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Postura")
        
        mp_pose = mp.solutions.pose #Referencia al módulo pose de MediaPipe
        #Esto (de abajo) inicializa un modelo de IA preentrenado para detectar poses humanas en imágenes o videos.
        self.pose = mp_pose.Pose(       #Prepara el método .process(image), que detecta el cuerpo y devuelve los puntos clave (landmarks) de la pose (hobros, rodillas, etc.)
            min_detection_confidence=0.5,   #Qué tan seguro debe estar para detectar el cuerpo
            min_tracking_confidence=0.5     #Confianza para seguir el cuerpo entre frames
        )

        self.cap = cv2.VideoCapture(0)  # cámara

        self.label = tk.Label(root)
        self.label.pack()

        self.btn = tk.Button(root, text="Subir video", command=self.subir_video)
        self.btn.pack()

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            #PROCESAR FRAME
            frame = procesar_frame(frame, self.pose)

            #Muestra en Tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.root.after(10, self.update_frame)  # loop no bloqueante

    def subir_video(self):
        path = filedialog.askopenfilename()
        if path:
            self.cap.release()
            self.cap = cv2.VideoCapture(path)
            
    def on_close(self):
        print("Cerrando app...")
        self.cap.release()
        self.pose.close()
        self.root.destroy()

root = tk.Tk()
app = App(root)
root.protocol("WM_DELETE_WINDOW", app.on_close)
root.mainloop()