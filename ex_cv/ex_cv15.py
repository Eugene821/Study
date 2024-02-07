#프로그램 [3-6]
#히스토그램 평활화하기

import cv2
import matplotlib.pyplot as plt
img = cv2.imread('bbuibbui.jpg')

plt.subplot(2, 2, 1) #동시에 창을 띄우고 싶을 때
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.xticks([])
plt.yticks([])
#plt.show()

plt.subplot(2, 2, 2)
h = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(h, color='b', linewidth=1)
#plt.show()


plt.subplot(2, 2, 3)
equal = cv2.equalizeHist(gray)
plt.imshow(equal, cmap='gray')
plt.xticks([])
plt.yticks([])
#plt.show()

plt.subplot(2, 2, 4)
h = cv2.calcHist([equal], [0], None, [256], [0, 256])
plt.plot(h, color='r', linewidth=1)
plt.show()


