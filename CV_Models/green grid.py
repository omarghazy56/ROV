# Import libraries
import cv2
import numpy as np

# Define a function to calculate MSE
def mse(imageA, imageB):
    # Compute the mean squared error between two images
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

# Load the images of coral reefs
imageA = cv2.imread("coral1.jpg")
imageB = cv2.imread("coral2.jpg")

# Convert them to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# Calculate MSE and print it
mse_value = mse(grayA, grayB)
print(f"MSE: {mse_value}")

# Highlight differences by subtracting images and save it
diff = cv2.subtract(grayA, grayB)
cv2.imwrite("diff.jpg", diff)
