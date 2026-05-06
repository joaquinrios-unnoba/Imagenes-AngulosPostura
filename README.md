# Análisis de Postura con Python

Este proyecto permite analizar la postura de una persona utilizando procesamiento de imágenes y video.

## 🚀 Funcionalidades

* 📷 Análisis en tiempo real usando cámara
* 🎥 Análisis de postura a partir de un video
* 📐 Cálculo de ángulos del cuerpo

---

## ▶️ Cómo ejecutar

### 🔴 Tiempo real (cámara)

```bash
python Vista.py
```

### 🎬 Video

```bash
python Postura.py
```

> ⚠️ Importante: en el modo video, especificar la ruta del archivo dentro del código.

---

## 🧰 Requisitos

* Python 3.11
  
Si se tiene otra version de python y la queres mantener, crea un entorno virtual
con python 3.11 (si o si hay que instalarlo) y ejecuta este comando:

* py -3.11 -m venv venv

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 📦 Instalación

```bash
git clone https://github.com/joaquinrios-unnoba/Imagenes-AngulosPostura.git
cd Imagenes-AngulosPostura
python -m venv venv
venv\Scripts\activate   # En Windows
pip install -r requirements.txt
```

---

## 📁 Estructura

* `Postura.py` → análisis desde video
* `PosturaFrame.py` → análisis en tiempo real
* `PosturaAngulo.py` → cálculo de ángulos
* `Vista.py` → manejo de visualización

---

## ⚠️ Notas

* No se incluye el entorno virtual (`venv`)
* Asegurarse de usar Python 3.11 para evitar incompatibilidades (especialmente con MediaPipe)

---

## 👤 Autor

Joaquin Rios
