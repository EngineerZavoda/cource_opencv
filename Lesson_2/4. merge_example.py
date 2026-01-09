import cv2
img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_2/image.jpg') # Загрузка изображения
if img is None: # Проверка успешной загрузки
 print("Ошибка: файл не найден")
height, width, channels = img.shape # Получение размеров
print(f"Размер: {width}x{height}, каналов: {channels}")
cv2.imshow('image', img)  # Отображение изображения
cv2.waitKey(0) # Ожидание нажатия клавиши
cv2.destroyAllWindows() # Закрытие (уничтожение) окон