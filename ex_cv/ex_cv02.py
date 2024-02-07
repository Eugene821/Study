#영상 열기

import cv2
import sys

#카메라와 연결 시도
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    sys.exit("카메라 연결 실패")
    
while True :
    ret, frame = cap.read()
    #비디오를 구성하는 프레임 획득
    
    if not ret:
        print("v프레임 획득에 실패하여 루프를 나갑니다.")
        break
    
    cv2.imshow("Video Display", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    