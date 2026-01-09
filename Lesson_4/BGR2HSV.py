import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_4/circle.png')

# Преобразование BGR в HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Выделение желтых объектов
lower_yellow = np.array([20,100,100]) # Нижняя граница желтого цвета в HSV
upper_yellow = np.array([35,255,255]) # Верхняя граница желтого цвета в HSVmask
mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow) # Создание маски для желтых объектов

result = cv2.bitwise_and(image, image, mask=mask) # Применение маски к исходному изображению

# Отображение результатов
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('Yellow Objects Mask', mask)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()