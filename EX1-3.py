# the script for filtering
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Valmanway.jpg')
b,g,r = cv2.split(img)
img = cv2.merge([r, g, b])

kernel = np.array([[1, 2, 0.25],[0.5, 1.0, 0.5],[0.25, 0.5, 0.25]])/2.0
dst = cv2.filter2D(img,0,kernel)

avgBlur = cv2.blur(img,(3,3))
median = cv2.medianBlur(img,5)
GauBlur = cv2.GaussianBlur(img,(5,5),0)
BilateralFil = cv2.bilateralFilter(img,9,75,75)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(avgBlur),plt.title('AvgBlurred')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(median),plt.title('MedianBlurred')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(dst),plt.title('Untitled')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(GauBlur),plt.title('GaussianBlurred')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(BilateralFil),plt.title('BilateralFiltered')
plt.xticks([]), plt.yticks([])
plt.show()