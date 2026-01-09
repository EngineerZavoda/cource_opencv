img = cv2.imread('/Users/pvs/Desktop/Программы/cv_ai/Lesson_2/image.jpg') # Загрузка изображения
if img is None: # Проверка успешной загрузки
 print("Ошибка: файл не найден")