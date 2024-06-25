import numpy as np
import cv2
image = cv2.imread("flag.png")
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image_grayscale)
print(image[0, 201])
print(image[0, 0])
print(image[0, 403])
image[175, 300] = (255, 0, 0)

image_grayscale[175, 100] = 255
image_grayscale[175, 300] = 255
image_grayscale[175, 500] = 255
cv2.imshow("image_grayscale", image_grayscale)
print(image_grayscale.shape)
cv2.imshow("flag", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
image = np.array(
    [
        [
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
],
        [
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
],
        [
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
],
        [
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
],
        [
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
],
        [
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
        [255,0,0],
],    
],np.uint8 )


print(image.shape)
cv2.imshow("flag",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
