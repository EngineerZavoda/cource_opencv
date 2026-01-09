import cv2  # библиотека OpenCV

# Создаём субтрактор фона
bg_subtractor = cv2.createBackgroundSubtractorMOG2()  # модель фона для отделения движущихся объектов

cap = cv2.VideoCapture('Lesson_6/video.mp4')  # открываем видеофайл
while True:
    ret, frame = cap.read()  # читаем кадр
    if not ret:  # если кадры закончились
        break  # выходим из цикла
 
    # Применяем вычитание фона
    fg_mask = bg_subtractor.apply(frame)  # получаем маску движущихся областей
 
    # Находим контуры
    contours, _ = cv2.findContours(
        fg_mask,  # бинарная маска
        cv2.RETR_EXTERNAL,  # берём только внешние контуры
        cv2.CHAIN_APPROX_SIMPLE,  # упрощённое представление контуров
    )  # получаем список контуров

    # Простейшая отрисовка рамок по контурам
    for cnt in contours:  # перебираем найденные контуры
        x, y, w, h = cv2.boundingRect(cnt)  # вычисляем прямоугольник вокруг контура
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # рисуем рамку
 
    cv2.imshow('Mask', fg_mask)  # показываем маску
    cv2.imshow('Frame', frame)  # показываем кадр с рамками

    if cv2.waitKey(30) & 0xFF == ord('q'):  # ждём 30 мс и проверяем на 'q'
        break  # выходим по клавише

cap.release()  # освобождаем видео
cv2.destroyAllWindows()  # закрываем окна
