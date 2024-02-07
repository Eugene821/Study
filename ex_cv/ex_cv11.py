import cv2
import sys


img = cv2.imread("BBUIBBUI.jpg")

t, bin_img = cv2.threshold(img[:,:,2],0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("오츄 알고리즘이 찾은 최적 임곗값 = ", t)

cv2.imshow("R channel", img[:,:,2])
cv2.imshow("R channel binarization", bin_img)

cv2.waitKey()
cv2.destroyAllWindows()