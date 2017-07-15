import cv2
import numpy as np
import time
from matplotlib import pyplot as plt


# 保存黑棋灰度差值图
if timeF != 0 and (timeF / 10) % 2 == 1:
    a = cv2.imread(url)
    src = '%d' % (timeF - 10)
    lasturl = src + '.png'
    print(lasturl)
    b = cv2.imread(lasturl)
    Graya = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    Grayb = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    c = Grayb - Graya;

    Grayurl = 'sub' + count + '.png'

    cv2.imwrite(Grayurl, c)  # 灰度图
    # cv2.imshow(Grayurl, c)



    # 模板匹配
    x = 0
    y = 0
    img = cv2.imread(Grayurl, 0)
    img2 = img.copy()
    template = cv2.imread('test.png', 0)
    w, h = template.shape[::-1]

    methods = ['cv2.TM_SQDIFF']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        print(int(top_left[0] + w / 2), int(top_left[1] + h / 2))
        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        plt.figure()
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
