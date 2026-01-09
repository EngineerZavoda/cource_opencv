import cv2
import numpy as np

# Загрузка изображения
img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_2/photo.jpg')
if img is None: # Проверка успешной загрузки
 print("Ошибка: файл не найден")
 exit(1)

# Увеличение контрастности
alpha = 1.5 # Контраст (1.0-3.0)
beta = 10 # Яркость (0-100)
enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Применение размытия для сглаживания
blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)

# Отображение результатов
cv2.imshow('Original', img)
cv2.imshow('With a filter', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Сохранение результата
# cv2.imwrite('filtered_photo.jpg', blurred)
