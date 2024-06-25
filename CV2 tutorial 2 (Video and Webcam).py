import cv2
import numpy as np

cap = cv2.VideoCapture(1)
key = cv2.waitKey(1)
while True:
    ret, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", frame)
    cv2.imshow("GRAY FRAME", gray_scale)
    k = cv2.waitKey(5)
    # ESC -> 27
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
"""
cap = cv2.VideoCapture("red_panda_snow.mp4")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out =cv2.VideoWriter("flipped_red_panda.avi",fourcc,25,(640,360))
while True:
    ret,frame = cap.read()
    frame2 = cv2.flip(frame,1)
    frame3 = cv2.flip(frame,0)

    out.write(frame2)
    
    cv2.imshow("frame3", frame3)
    cv2.imshow("frame2", frame2)
    cv2.imshow("frame", frame)
    cv2.waitKey(3)

    
cap.release()
cv2.destroyAllWindows()
"""
