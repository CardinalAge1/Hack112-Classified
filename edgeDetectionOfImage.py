import cv2
import numpy as np

img = cv2.imread('maze2.png', cv2.IMREAD_GRAYSCALE)

filters = cv2.Canny(img, 100, 200)

cv2.imwrite("mazeEdge.png", filters)

cv2.waitKey(0)
