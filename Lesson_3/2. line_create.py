import cv2
import numpy as np

# Создаём чёрный холст
canvas = np.zeros((400, 600, 3), # Размеры холста
                  dtype=np.uint8) # Тип данных

# Рисуем фиолетовую линию
start_point = (50, 50) # Начальная точка
end_point = (550, 350) # Конечная точка
color = (255, 0, 200)  # Фиолетовый
thickness = 3

cv2.line(canvas, start_point,   # Начало линии
         end_point, color,      # Цвет линии
         thickness, cv2.LINE_AA) #Антиалиасинг

# Показываем результат
cv2.imshow('Line', canvas) # Окно с линией
cv2.waitKey(0) # Ждём нажатия клавиши
cv2.destroyAllWindows() # Закрываем окна