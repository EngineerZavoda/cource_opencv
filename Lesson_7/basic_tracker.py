import cv2  # подключаем OpenCV

tracker = cv2.TrackerKCF_create()  # создаём трекер KCF

cap = cv2.VideoCapture("Lesson_6/video.mp4")  # открываем видеофайл
ret, frame = cap.read()  # читаем первый кадр
if not ret:  # проверяем, что кадр прочитан
    raise SystemExit("Не удалось прочитать первый кадр")  # завершаем при ошибке

border_object = (287, 23, 86, 320)  # задаём рамку объекта (x, y, w, h)

tracker.init(frame, border_object)  # инициализируем трекер первым кадром и рамкой

while True:  # цикл по кадрам видео
    ret, frame = cap.read()  # читаем следующий кадр
    if not ret:  # если кадры закончились
        break  # выходим из цикла

    # Обновляем трекер
    success, border_object = tracker.update(frame)

    cv2.imshow("Tracking", frame)  # показываем кадр
    if cv2.waitKey(30) & 0xFF == ord("q"):  # ждём 30 мс и проверяем клавишу q
        break  # выходим по нажатию q

cap.release()  # освобождаем видеофайл
cv2.destroyAllWindows()  # закрываем окна OpenCV
