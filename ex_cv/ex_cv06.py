# 마우스로 클릭한 곳에 직사각형 그리기
import cv2
import sys

img = cv2.imread("BBUIBBUI.jpg")

if img is None :
    sys.exit("파일을 찾을 수 없습니다.")
    
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x+200, y+200), (0,0,255), 2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x+100, y+100), (0,255,0), 2)
        
    cv2.imshow("draw", img)

cv2.namedWindow("Drawing")
cv2.imshow("Drawing", img)

cv2.setMouseCallback("Drawing", draw)

while True :
    if cv2.waitKey(1)==ord("q"):
        cv2.destroyAllWindows()
        break