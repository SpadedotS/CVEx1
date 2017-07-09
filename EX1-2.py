import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('Valmanway.jpg', 0)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img = cv2.imread('Valmanway.jpg')
th2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

titles = ['Original Image', 'Binary Thresholding', 'Gray Image', 'HSV image']
images = [img, th1, th2, hsv]


plt.subplot(2,2,1),plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(images[1],'gray')
plt.title(titles[1])
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(images[2],'gray')
plt.title(titles[2])
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(images[3],'hsv')
plt.title(titles[3])
plt.xticks([]),plt.yticks([])
plt.show()