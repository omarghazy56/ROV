#import opencv and numpy
import cv2  
import numpy as np

#trackbar callback fucntion does nothing but required for trackbar
def nothing(x):
	pass

#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10);

#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('r','controls',0,255,nothing)
cv2.createTrackbar('g','controls',0,255,nothing)
cv2.createTrackbar('b','controls',0,255,nothing)



while(1):
	#create a black image 
	img = np.zeros((512,512,3), np.uint8)
	
	#returns current position/value of trackbar 
	r= int(cv2.getTrackbarPos('r','controls'))
	g=int(cv2.getTrackbarPos('g','controls'))
	b=int(cv2.getTrackbarPos('b','controls'))

	#assign trackbar value to r,g,b channel of the image
	img[:,:,0]=b
	img[:,:,1]=g
	img[:,:,2]=r

	cv2.imshow('img',img)
	
	#waitfor the user to press escape and break the while loop 
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
		
#destroys all window
cv2.destroyAllWindows()
