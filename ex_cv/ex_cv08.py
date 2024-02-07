import cv2

def draw_shape(event, x, y, flags, param):
    global drawing, start_point

    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        end_point = (x, y)
        cv2.rectangle(img, start_point, end_point, (0, 0, 255), 2)
        cv2.imshow("Draw Shapes", img)
    elif event == cv2.EVENT_RBUTTONDOWN: 
        center = (x, y)
        radius = 30  
        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.imshow("Draw Shapes", img)

img = cv2.imread("BBUIBBUI.jpg")
if img is None:
    print("파일을 찾을 수 없습니다.")
    exit()

cv2.imshow("Draw Shapes", img)
drawing = False
start_point = (0, 0)

cv2.setMouseCallback("Draw Shapes", draw_shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

