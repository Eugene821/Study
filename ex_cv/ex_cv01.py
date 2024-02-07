#이미지 열기

import cv2
import sys

#print(cv2.__version__) # 버전출력

img = cv2.imread("universe_cat.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")
    
#print(type(img))
#print(img.shape)

print(img[0,0,0],img[0,0,1],img[0,0,2])
print("*"*80)
print(img[0,1,0],img[0,1,1],img[0,1,2])
print("*"*80)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_small = cv2.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

cv2.imwrite("window_gray.jpg", gray)
cv2.imwrite("window_gray_small.jpg", gray_small)

cv2.imshow("COLOR", img)
cv2.imshow("GRAY", gray)
cv2.imshow("GRAY_SMALL", gray_small)


cv2.waitKey() # key 입력이 없으면 1초뒤 종료(밀리초 단위 입력)
cv2.destroyAllWindows()
