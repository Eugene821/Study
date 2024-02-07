import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,100,200)

contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) #이 매개변수를 통해 여러 가지 근사 방법 제공\
#contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #직선에 대해 양 끝 점만
#contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_TC89_KCOS) #굴곡이 심한 애만

lcontour=[]
for i in range(len(contour)):
    if contour[i].shape[0]>100: # 길이가 100보다 크면
        lcontour.append(contour[i])

#cv.drawContours(img, lcontour,-1,(0,255,0),3)
cv.drawContours(img, lcontour,48,(0,255,0),3)

cv.imshow('Original with contours',img)
cv.imshow('Canny',canny)

cv.waitKey()
cv.destroyAllWindows()