import cv2

# Читаем кадр со сдвигом
cap = cv2.VideoCapture("Lesson_6/video.mp4")
start_frame = 135  # с какого кадра начать
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# Уменьшаем кадры для скорости (1.0 — без изменения)
scale = 0.5

ret, frame = cap.read()
if not ret:
    raise SystemExit(f"Не удалось прочитать кадр {start_frame}")

if scale != 1.0:
    frame = cv2.resize(frame, None, fx=scale, fy=scale)

# Выбираем область объекта вручную
border_object = cv2.selectROI("Выберите объект", frame, False)
cv2.destroyWindow("Выберите объект")
if border_object == (0, 0, 0, 0):
    raise SystemExit("Область не выбрана")

# Создаём трекер (MOSSE быстрее для FPS; вернёт KCF, если MOSSE недоступен)
tracker = cv2.TrackerMOSSE_create() if hasattr(cv2, "TrackerMOSSE_create") else cv2.TrackerKCF_create()

# Инициализируем трекер
tracker.init(frame, border_object)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if scale != 1.0:
        frame = cv2.resize(frame, None, fx=scale, fy=scale)

    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
