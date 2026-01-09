import cv2 # Библиотека OpenCV
import numpy as np # Библиотека NumPy

# Создаём холст
canvas = np.zeros((600, 800, 3), dtype=np.uint8)

# Рисуем линии
cv2.line(canvas, (50, 50), (750, 50), (100, 100, 255), 2)
cv2.line(canvas, (50, 50), (50, 550), (100, 100, 255), 2)

# Рисуем прямоугольник с подписью
cv2.rectangle(canvas, (100, 100), (300, 250), (0, 255, 255), 2)
cv2.putText(canvas, 'Detected', (110, 130), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

# Рисуем окружность
cv2.circle(canvas, (500, 175), 80, (255, 0, 200), 3)
cv2.putText(canvas, 'Object', (460, 180), 
            cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 200), 2)

# Добавляем заголовок
cv2.putText(canvas, 'OpenCV Drawing Demo', (200, 500), 
            cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3, 
            cv2.LINE_AA)

# Отображаем изображение
cv2.imshow("Drawing with OpenCV", canvas)
cv2.waitKey(0) # Ожидание нажатия клавиши
