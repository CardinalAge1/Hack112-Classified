import sys
import math
import cv2 as cv
import numpy as np

video = cv.VideoCapture(1)

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
boundingBox = (287, 23, 86, 320)

ok, frame = video.read()

# Uncomment the line below to select a different bounding box
boundingBox = cv.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
trackOk = tracker.init(frame, boundingBox)

while True:
    linesSet = set()
    # Loads an image
    vidOk, src = video.read()
    trackOk, bbox = tracker.update(src)
    edge = cv.Canny(src, 50, 200, None, 3)

    # Copy edges tos the images that will display the results in BGR
    houghProb = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    linesProb = cv.HoughLinesP(edge, 1, np.pi / 180, 50, None, 50, 10)
    if trackOk:
        trackPoint1 = (int(bbox[0]), int(bbox[1]))
        trackPoint2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv.rectangle(src, trackPoint1, trackPoint2, (255, 0, 0), 2, 1)
        cv.rectangle(houghProb, trackPoint1, trackPoint2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv.putText(src, "Tracking failure detected", (100, 80),
                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display tracker type on frame
    cv.putText(src, tracker_type + " Tracker", (100, 20),
                cv.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display FPS on frame
    if linesProb is not None:
        for i in range(0, len(linesProb)):
            l = linesProb[i][0]
            if (trackPoint1[0] < l[0] < trackPoint2[0] and trackPoint1[0] < l[2] < trackPoint2[0]) or\
                (trackPoint1[1] < l[1] < trackPoint2[1] and trackPoint1[1] < l[3] < trackPoint2[1]): continue
            linesSet.add(((l[0], l[1]), (l[2], l[3])))
            cv.line(src, (l[0], l[1]), (l[2], l[3]),
                    (0, 0, 255), 3, cv.LINE_AA)
            cv.line(houghProb, (l[0], l[1]), (l[2], l[3]),
                    (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", houghProb)

    keyPressed = cv.waitKey(1) & 0xff
    if keyPressed == 27: break
video.release()
cv.destroyAllWindows()
