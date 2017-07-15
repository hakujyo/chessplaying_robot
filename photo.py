import cv2
import numpy as np
from matplotlib import pyplot as plt



a = cv2.imread('10.png')
rows, cols, channels = a.shape
cv2.imshow('origin',a)

plt.imshow(a,'gray')
plt.show()
list1 = np.float32([[71, 14], [499, 17], [16, 458], [542, 461]])
list2 = np.float32([[0, 0], [720, 0], [0, 720], [720, 720]])
M = cv2.getPerspectiveTransform(list1, list2)
         #M = cv2.findHomography(list1,list2)
img_perspective = cv2.warpPerspective(a, M, (720, 720))

print('perspective:\n', M)
cv2.imwrite("model3.jpg", img_perspective)

plt.imshow(img_perspective,'gray')
plt.show()
cv2.imshow('perspective',img_perspective)


cv2.waitKey(0)