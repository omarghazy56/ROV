import numpy as np
import cv2
image = cv2.imread("red_panda.jpg")

rows, cols , channel = image.shape

'''
roi = image[0:rows , 0:cols]
cv2.imshow("roi",roi)
'''

roi = image[100:280 , 150:320]

cv2.imshow("Panda",image)
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
