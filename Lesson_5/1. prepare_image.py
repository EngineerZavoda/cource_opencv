import cv2

img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_4/circle.png') # Чтение изображения

gray = cv2.cvtColor(img, # Преобразование в оттенки серого
 cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur( # Применение гауссовского размытия
 gray, (5, 5), 0)           # Размер ядра 5x5

cv2.imshow('Gray Image', gray)             # Отображение изображения в оттенках серого
cv2.imshow('Blurred Image', blurred)       # Отображение размытого изображения
cv2.waitKey(0)                            # Ожидание нажатия клавиши
cv2.destroyAllWindows()                   # Закрытие всех окон