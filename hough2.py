import sys
import math
import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    # Loads an image
    i, src = video.read()
    # Check if image is loaded fine
    dst = cv.Canny(src, 50, 200, None, 3)

    # Copy edges to the images that will display the results in BGR
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(src, (l[0], l[1]), (l[2], l[3]),
                    (0, 0, 255), 3, cv.LINE_AA)
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]),
                    (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

    k = cv.waitKey(1) & 0xff
    if k == 27: break
video.release()
cv.destroyAllWindows()
