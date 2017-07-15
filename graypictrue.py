import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

timeslice=30

def makegraypicture(url,numtime):
    a = cv2.imread(url)
    src = '%d' % (numtime - timeslice)
    lasturl = src + '.png'
    b = cv2.imread(lasturl)
    Graya = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    Grayb = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    c = Grayb - Graya;

    count = '%d' % numtime
    Grayurl = 'sub' + count + '.png'

    cv2.imwrite(Grayurl, c)  # 灰度图
    # cv2.imshow(Grayurl, c)
    return Grayurl

