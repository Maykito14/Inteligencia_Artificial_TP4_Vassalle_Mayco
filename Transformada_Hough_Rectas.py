import cv2
import numpy as np
import matplotlib.pyplot as plt

# Se carga la imagen, y se convierte en escala de grises
img = cv2.imread('rectas.jpg', 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3) # Aplica el detector de bordes de Canny a la imagen.

# Aplica la transformada de Hough para detectar líneas en la imagen de bordes.
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Recorre todas las líneas detectadas y dibuja cada una en la imagen original.
for rho, theta in lines[:, 0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Muestra la imagen con las líneas detectadas.
plt.imshow(img)
plt.show()
