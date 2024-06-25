import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX

def find_shape(shape_list):
    l1 = np.sqrt((shape_list[0]-shape_list[2])**2+(shape_list[1]-shape_list[3])**2)
    l2 = np.sqrt((shape_list[0]-shape_list[6])**2+(shape_list[1]-shape_list[7])**2)
    if abs(l1-l2 < 5 ):
        return "Square"
    else:
        return "Rectangle"
        
img = cv2.imread(r"C:\Users\Ghazy\AppData\Local\Programs\Python\Python39\images\shapes.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("shapes", img)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
Triangle,Square,Rectangle,Circle,Ellipse = 0,-1,0,0,0
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
        Triangle+=1
    elif len(approx) == 4:
        shape = find_shape(approx.ravel())
        if shape =="Square":
            cv2.putText(img, "Square", (x, y), font, 1, (0))
            Square+=1
        else:
            cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
            Rectangle+=1
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
        
    elif 6 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        Ellipse +=1
        
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))
        Circle+=1
        
y = img.shape[0]
x = img.shape[1]
#Not used
green = (0,255,0)
#Triangle
points = np.array([[ [x-130,240] ,[x-80,240],[x-105,190] ]])
cv2.polylines(img,[points],True,green,thickness = 5)
cv2.putText(img, str(Triangle), (x-40, 220), font, 0.8, (0))
#Square
cv2.rectangle(img, (x-130,280),(x-80,330),green,5)
cv2.putText(img, str(Square), (x-40, 310), font, 0.8, (0))
#Rectangle
cv2.rectangle(img, (x-145,370),(x-65,410),green,5)
cv2.putText(img, str(Rectangle), (x-40, 395), font, 0.8, (0))
#Circle
cv2.circle(img,(x-100,475),25,green,5)
cv2.putText(img, str(Circle), (x-40, 480), font, 0.8, (0))
#Ellipse
cv2.ellipse(img , (x-100,560) , (50,20) , 0 , 0,360, green , 5)
cv2.putText(img, str(Ellipse), (x-40, 565), font, 0.8, (0))


    
cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
