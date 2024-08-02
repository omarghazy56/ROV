import cv2
import numpy as np


def nothing(x):
    pass


def nothing1(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")
cv2.createTrackbar("test", "frame", 50, 500, nothing)
cv2.createTrackbar("Colored/Gray", "frame", 0, 1, nothing1)

key = cv2.waitKey(1)

while True:
    _, frame = cap.read()
    print(_)
    test = cv2.getTrackbarPos("test", "frame")
    flag = cv2.getTrackbarPos("Colored/Gray", "frame")

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, str(test), (20, 120), font, 4, (0, 0, 255))
    if (flag == 0):
        pass
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)
    key -= cv2.waitKey(1)
    if key == 250:
        break

cap.release()
cv2.destroyAllWindows()
