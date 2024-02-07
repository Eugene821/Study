# SIFT 검출
import cv2

img=cv2.imread('mot_color70.jpg') # 영상 읽기
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift=cv2.SIFT_create() 
# sift=cv2.SIFT_create(nfeatures=500) #신뢰도가 높은 500개의 특징점 , 0이면 모든 값
# 매개변수 
# nfeatures: 검출할 특징점 개수(기본값 0 : 검출한 특징점 모두 반환)
# nOctaveLayers : 옥타브 개수를 지정
# contrastThreshold : 테일러 확장
# edgeThresHold: 에지에서검출된 특징점을 걸러냄
# sigma : 옥타브 0의 입력 영상에 적용할 가우시안의 표준편차
# cv2.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04,
# edgeThresHold=10, sigma=1.6) 

kp,des=sift.detectAndCompute(gray,None)
# 특징점 kp, 기술자 des
# kp=sift.detect(gray,None)
# des=sift.compute(gray,kp)
print("len(kp)", len(kp))

gray=cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('sift', gray)

k=cv2.waitKey()
cv2.destroyAllWindows()