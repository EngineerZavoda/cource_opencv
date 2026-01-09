import cv2
img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_2/image.jpg') # Загрузка изображения 
if img is None: # Проверка успешной загрузки
 print("Ошибка: файл не найден")

resized = cv2.resize( # метод изменения размера изображения
    img,        # исходное изображение 
    (200, 100)  # новые размены (ширина, высота)
)
cropped = img[ # метод обрезки изображения
    100:400, # координаты x0;y0 
    200:600  # координаты x1;y1
]
#
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Конвертация BGR в RGB
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Конвертация в оттенки серого

# Отображение изображений в отдельных окнах
cv2.imshow('image', img)  # Отображение оригинального изображения
cv2.imshow('resized', resized)  # Отображение измененного изображения
cv2.imshow('cropped', cropped)  # Отображение обрезанного изображения
cv2.imshow('rgb', img_rgb)  # Отображение RGB изображения
cv2.imshow('gray', img_gray)  # Отображение серого изображения

cv2.waitKey(0) # Ожидание нажатия  клавиши
cv2.destroyAllWindows() # Закрытие (уничтожение) окон 