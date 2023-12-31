import cv2
import numpy as np

# Reading Dog Image
img = cv2.imread("./assets/dog.jpg")

# Converting it to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Showing images on screen
cv2.imshow("initial", img)
cv2.imshow("gray", gray)

# Turning gray image into negative
img_neg = 255 - gray
cv2.imshow('negative', img_neg)

# Blurring the negative image
img_blur = cv2.GaussianBlur(img_neg, (21, 21), 0)

# Dividing images to create pencil sketch effect
sketch = cv2.divide(gray, img_blur, scale=256.0)

# Showing final resoult
cv2.imshow("sketch", sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
