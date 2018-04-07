import sys
import math
import cv2
import numpy as np

video = cv2.VideoCapture(0)

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
tracker_type = tracker_types[2]
if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()

#boundingBox = (287, 23, 86, 320)

ok, frame = video.read()
if not ok:
    print(1 / 0)
#boundingBox = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
#trackOk = tracker.init(frame, boundingBox)

template = cv2.imread('trackTemplate.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

while True:
    linesSet = set()
    # Loads an image
    vidOk, src = video.read()
    # print(vidOk)
    #trackOk, bbox = tracker.update(src)
    edge = cv2.Canny(src, 50, 200, None, 3)
    # Apply template Matching
    greySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(greySrc, template, eval(methods[2]))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if eval(methods[2]) in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(src, top_left, bottom_right, (255, 255, 255), 2)

    # Copy edges tos the images that will display the results in BGR
    houghProb = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    linesProb = cv2.HoughLinesP(edge, 1, np.pi / 180, 50, None, 50, 10)
    # if trackOk:
    #     trackPoint1 = (int(boundingBox[0]), int(boundingBox[1]))
    #     trackPoint2 = (
    #         int(boundingBox[0] + boundingBox[2]), int(boundingBox[1] + boundingBox[3]))
    #     cv2.rectangle(src, trackPoint1, trackPoint2, (255, 0, 0), 2, 1)
    #     cv2.rectangle(houghProb, trackPoint1, trackPoint2, (255, 0, 0), 2, 1)
    # else:
    #     # Tracking failure
    #     cv2.putText(src, "Tracking failure detected", (100, 80),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display tracker type on frame
    cv2.putText(src, tracker_type + " Tracker", (100, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display FPS on frame
    if linesProb is not None:
        for i in range(0, len(linesProb)):
            l = linesProb[i][0]
            # if (trackPoint1[0] < l[0] < trackPoint2[0] and trackPoint1[0] < l[2] < trackPoint2[0]) or\
            #     (trackPoint1[1] < l[1] < trackPoint2[1] and trackPoint1[1] < l[3] < trackPoint2[1]): continue
        linesSet.add(((l[0], l[1]), (l[2], l[3])))
        cv2.line(src, (l[0], l[1]), (l[2], l[3]),
                (0, 0, 255), 3, cv2.LINE_AA)
        cv2.line(houghProb, (l[0], l[1]), (l[2], l[3]),
                (0, 0, 255), 3, cv2.LINE_AA)
    cv2.imshow("Source", src)
    cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", houghProb)

    keyPressed = cv2.waitKey(1) & 0xff
    if keyPressed == 27: break
video.release()
cv2.destroyAllWindows()
