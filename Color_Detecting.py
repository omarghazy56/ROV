# importing packages
import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

# Changing camera resolution
cap.set(3,640)
cap.set(4,480)

while True:
    # load the image, convert it to HSV
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Defining white color threshold
    #Edited from 0 0 210
    lower_white = np.array([0, 0, 250])
    ##Edited from 130 255 255
    upper_white = np.array([255, 255, 255])

    # Filtiring white colors in the HSV frame
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    # Getting contours of white color shapes
    cnts1 = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    for c in cnts1:
        white_area = cv2.contourArea(c)
        if white_area >2500:
            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            M = cv2.moments(c)
            
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            # Creating circle at the middle of contour
            cv2.circle(frame, (cx,cy), 7, (0,255,0), -1)
            # Creating text string to display(If it is infected)
            cv2.putText(frame, "Infected", (cx -20, cy -20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
            
    
    
    cv2.imshow("Output",frame)
    k = cv2.waitKey(5)
    # ESC -> 27
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
