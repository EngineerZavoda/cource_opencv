import numpy as np
import cv2

# Чёрный холст 512×512
black_canvas = np.zeros((512, 512, 3), 
 dtype=np.uint8)

# Белый холст
white_canvas = np.ones((512, 512, 3), 
 dtype=np.uint8) * 255

cv2.imshow("black_canvas", black_canvas)
cv2.imshow("white_canvas", white_canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()