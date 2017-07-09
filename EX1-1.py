import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.figure(num='EX1.1',figsize=(12,4))
img = cv2.imread('Valmanway.jpg', 1)
b,g,r = cv2.split(img)
img = cv2.merge([r, g, b])
plt.subplot(1,3,1),plt.imshow(img)

img = cv2.imread('Valmanway.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    plt.subplot(1,3,2)
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

img = cv2.imread('Valmanway.jpg', 0)
plt.subplot(1,3,3)
a = img.ravel()
print a.dtype
a = a.astype(np.uint32)
print a.dtype
for i in range(1,256):
    a[i] += a[i-1]
    plt.bar(left=float(i)-0.5, height = a[i], width=1, facecolor = '#0000ff')
plt.show()