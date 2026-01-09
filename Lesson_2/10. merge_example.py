import cv2

img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_2/image.jpg') # Загрузка изображения
if img is None: # Проверка успешной загрузки
 print("Ошибка: файл не найден")

gray = cv2.cvtColor( # Конвертация в оттенки серого
    img, cv2.COLOR_BGR2GRAY
)

blurred = cv2.GaussianBlur( # Применение гауссова размытия
    img, (5, 5), 0 # Размер ядра и стандартное отклонение по Гауссу
)

_, thresh = cv2.threshold( # Применение пороговой обработки
    gray, 127, 255, # Пороговое значение и максимальное значение
    cv2.THRESH_BINARY # Тип пороговой обработки
)

smooth = cv2.medianBlur( # Применение медианного размытия
    img, 5 # Размер ядра
)

# Отображение изображений в отдельных окнах
cv2.imshow('image', img)  # Отображение оригинального изображения
cv2.imshow('blurred', blurred)  # Отображение гауссова размытия
cv2.imshow('threshold', thresh)  # Отображение пороговой обработки
cv2.imshow('smooth', smooth)  # Отображение медианного размытия

cv2.waitKey(0) # Ожидание нажатия клавиши
cv2.destroyAllWindows() # Закрытие (уничтожение) окон
