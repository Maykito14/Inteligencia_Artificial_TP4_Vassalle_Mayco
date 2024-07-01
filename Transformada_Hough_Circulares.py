import cv2
import numpy as np
import matplotlib.pyplot as plt

# Se carga la imagen, y se convierte en escala de grises
img = cv2.imread('circulos.jpg', 0)
img_color = cv2.imread('circulos.jpg')

# Aplica el detector de bordes de Canny a la imagen.
edges = cv2.Canny(img, 50, 150, apertureSize=3)

# Aplica la transformada de Hough para detectar circunsferencias en la imagen.
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=50, param2=30, minRadius=20, maxRadius=50)

# Dibuja las circunferencias detectadas
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img_color, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(img_color, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# Muestra la imagen resultante
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.show()
