# import time
# time1 = time.time()
# time.sleep(15)
# time2 = time.time()
# print (int(time2 - time1))
#
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)  # 读入视频文件
time = 0 #计时器
def sleeptime(hour,min,sec):
    second = sleeptime(0, 0, 20)

if cap.isOpened():  # 判断是否正常打开
    rval, frame = cap.read()
else:
    rval = False


while rval:  # 循环读取视频帧
    rval, frame = cap.read()
    cv2.imshow("capture", frame) #视频窗口
    if (time % 100 == 0):  # 每隔timeF帧进行存储操作
        count='%d'%time
        url='%d'%time + ".png"
        #src='%d'%c
        cv2.imwrite(url, frame)  # 存储为图像

        #读图矫正
        a = cv2.imread(url)
        rows, cols, channels = a.shape
        list1 = np.float32([[69, 14], [500, 9], [23, 461], [549, 456]])
        list2 = np.float32([[0, 0], [720, 0], [0, 720], [720, 720]])
        M = cv2.getPerspectiveTransform(list1, list2)
        img_perspective = cv2.warpPerspective(a, M, (720, 720))

        print('perspective:\n', M)
        cv2.imwrite(url, img_perspective) #矫正后图片
        #cv2.imshow(url, img_perspective)

        #保存灰度差值图
        if time!=0:
            a = cv2.imread(url)
            src= '%d'%(time-100)
            lasturl = src + '.png'
            print(lasturl)
            b = cv2.imread(lasturl)
            Graya = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
            Grayb = cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)
            c = Grayb - Graya;
            Grayurl='sub'+count+'.png'

            cv2.imwrite(Grayurl, c) #灰度图
            #cv2.imshow(Grayurl, c)
            print("ccc=")


        cv2.waitKey(1)


    time = time + 1
    cv2.waitKey(1)
cap.release()