import cv2
import numpy as np

image = cv2.imread("red_panda.jpg")
image_true = cv2.imread("red_panda.jpg")

blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
violet = (180,0,180)
yellow = (0, 180, 180)
white = (255, 255, 255)

cv2.line(image,(50,30),(450,35),blue,thickness = 30)
cv2.circle(image,(240,205),25,red,-1)
cv2.rectangle(image, (50,60),(450,95),green,-1)
cv2.ellipse(image , (250,150) , (80,20) , 5 , 0,360, violet , -1)
points = np.array([[ [140,230] ,[380,230],[320,250] ,[250,280]]])
cv2.polylines(image,[points],False,yellow,thickness = 3)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"PANDA" , (50,60),font,4,white)


points = np.array([[ [140,230] ,[380,230],[320,290] ]])
cv2.polylines(image_true,[points],True,yellow,thickness = 3)

print(points)
print(image.shape)
cv2.imshow("red panda Edited" , image)
cv2.imshow("red panda" , image_true)



cv2.waitKey(0)



cv2.destroyAllWindows()

