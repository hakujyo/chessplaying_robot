import cv2
import numpy as np
import time

cap = cv2.VideoCapture(1)  # 读入视频文件
c = 1

if cap.isOpened():  # 判断是否正常打开
    rval, frame = cap.read()
else:
    rval = False

timeF = 1000  # 视频帧计数间隔频率

while rval:  # 循环读取视频帧
    rval, frame = cap.read()
    cv2.imshow("capture", frame)
    if (c % 100 == 0):  # 每隔timeF帧进行存储操作
        src='%d'%c
        cv2.imwrite(src+".jpg", frame)  # 存储为图像
    c = c + 1
    cv2.waitKey(1)
cap.release()