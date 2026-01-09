# Пример с разными методами аппроксимации

contours_full, _ = cv2.findContours(binary,  # Поиск контуров без упрощения
                                    cv2.RETR_EXTERNAL,  # Берем только внешние контуры
                                    cv2.CHAIN_APPROX_NONE)  # Сохраняем все точки

contours_simple, _ = cv2.findContours(binary,  # Поиск контуров с упрощением
                                      cv2.RETR_EXTERNAL,  # Берем только внешние контуры
                                      cv2.CHAIN_APPROX_SIMPLE)  # Упрощаем точки
