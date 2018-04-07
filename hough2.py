import sys
import math
import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
tracker_type = tracker_types[2]
if tracker_type == 'BOOSTING':
    tracker = cv.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker = cv.TrackerGOTURN_create()
# Define an initial bounding box
bbox = (287, 23, 86, 320)

ok, frame = video.read()

# Uncomment the line below to select a different bounding box
bbox = cv.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

while True:
    # Loads an image
    i, src = video.read()
    ok, bbox = tracker.update(src)
    dst = cv.Canny(src, 50, 200, None, 3)

    # Copy edges tos the images that will display the results in BGR
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    if i:
            # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv.rectangle(src, p1, p2, (255, 0, 0), 2, 1)
        cv.rectangle(cdstP, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv.putText(src, "Tracking failure detected", (100, 80),
                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display tracker type on frame
    cv.putText(src, tracker_type + " Tracker", (100, 20),
                cv.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display FPS on frame
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            if (p1[0] < l[0] < p2[0] and p1[0] < l[2] < p2[0]) or\
                (p1[1] < l[1] < p2[1] and p1[1] < l[3] < p2[1]): continue
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
