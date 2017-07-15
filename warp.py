import cv2
import numpy as np
import time
from matplotlib import pyplot as plt



def makewarp(url):
    a = cv2.imread(url)
    rows, cols, channels = a.shape
    list1 = np.float32([[71, 14], [499, 17], [16, 458], [542, 461]])
    list2 = np.float32([[0, 0], [720, 0], [0, 720], [720, 720]])
    M = cv2.getPerspectiveTransform(list1, list2)
    img_perspective = cv2.warpPerspective(a, M, (720, 720))

    print('perspective:\n', M)
    cv2.imwrite(url, img_perspective)  # 矫正后图片
    # cv2.imshow(url, img_perspective)
    cv2.waitKey(5)
