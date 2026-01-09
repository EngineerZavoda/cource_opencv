import cv2

img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_2/image.jpg') # Загрузка изображения
if img is None: # Проверка успешной загрузки
 print("Ошибка: файл не найден")

# Получение метаданных
print(f"Размер: {img.shape}")
print(f"Тип данных: {img.dtype}")
print(f"Общее число пикселей: {img.size}")

# Проверка типа изображения
if len(img.shape) == 3:
 print("Цветное изображение")
else:
 print("Изображение в оттенках серого")

cv2.imshow('image', img)  # Отображение изображения
cv2.waitKey(0) # Ожидание нажатия клавиши
cv2.destroyAllWindows() # Закрытие (уничтожение) окон
