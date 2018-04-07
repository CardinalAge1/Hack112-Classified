import cv2
import numpy as np
video = cv2.VideoCapture(0)
while True:
    u, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 2, np.pi / 180, 100,
                            minLineLength, maxLineGap)
    if not lines is None:
        for x1, y1, x2, y2 in lines[0]:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("Tracking", img)
    k = cv2.waitKey(1) & 0xff
    if k == 27: break
video.release()
cv2.destroyAllWindows()
