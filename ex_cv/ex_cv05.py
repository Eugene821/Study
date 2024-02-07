import cv2
import sys

img = cv2.imread("universe_cat.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")
    
img = cv2.imread("BBUIBBUI.jpg")
cv2.putText(img, "learn openCV", (200,24),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2) # 글씨쓰기
#cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])



cv2.imshow("Draw", img)

cv2.waitKey()
cv2.destroyAllWindows()
                 