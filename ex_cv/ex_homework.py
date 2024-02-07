import cv2
import numpy as np

img_gray = cv2.imread('hamster.jpg', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement( cv2.MORPH_RECT, ( 2,1 ),(-1,-1) )

img_result = cv2.erode(img_gray, kernel, iterations = 1)

cv2.imshow("Input", img_gray) 
cv2.imshow("Result", img_result)

cv2.waitKey(0) 
cv2.destroyAllWindows()

