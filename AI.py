from graphics import *
import cv2
import time
import warp
import matchpicture
import graypictrue
import arm

timeF=0 #时间片
lasttimeF=0xffffff#上一次执行的时间片
win = GraphWin('testAI', 720, 720)
win.setBackground('yellow')

p = [[0 for a in range(20)] for b in range(20)]
black = [[0 for a in range(20)] for b in range(20)]
white = [[0 for a in range(20)] for b in range(20)]
q = [[0 for a in range(20)] for b in range(20)]
len = [0 for a in range(4)]
tb = [0 for a in range(4)]
m = [1 for a in range(3)]
n = [1 for a in range(3)]
AI = [[[0 for a in range(20)] for b in range(20)] for c in range(20)]
player = [[[0 for a in range(20)] for b in range(20)] for c in range(20)]


def WinBoard():
    for i in range(19):
        for j in range(19):
            p[i + 1][j + 1] = Point(j * 40, i * 40)

    for r in range(19):
        Line(p[r + 1][1], p[r + 1][19]).draw(win)
    for s in range(19):
        Line(p[1][s + 1], p[19][s + 1]).draw(win)
    center = Circle(p[10][10], 3)
    center.draw(win)
    center.setFill('black')

def Click(x,y):
    #while 1:
        #p1 = win.getMouse()
        #x1 = p1.getX()
        #y1 = p1.getY()
    x1 = x
    y1 = y
    print("黑棋位置：", x1, y1)
    for i in range(19):
        for j in range(19):
            sqrdis = ((x1 - p[i + 1][j + 1].getX()) * (x1 - p[i + 1][j + 1].getX())) + (y1 - p[i + 1][
                j + 1].getY()) * (y1 - p[i + 1][j + 1].getY())
            if sqrdis <= 200 and q[i + 1][j + 1] == 0:
                black[i + 1][j + 1] = 1
                q[i + 1][j + 1] = Circle(p[i + 1][j + 1], 19.5)
                # 每一个click点的像素位置都可跳出
                print("黑棋矫正位置：", p[i + 1][j + 1].getX(), p[i + 1][j + 1].getY())
                q[i + 1][j + 1].draw(win)
                q[i + 1][j + 1].setFill('black')
                return 0


def Check():
    for i in range(19):
        for j in range(15):
            if black[i + 1][j + 1] and black[i + 1][j + 2] and black[i + 1][j + 3] and black[i + 1][j + 4] and \
                    black[i + 1][j + 5]:
                return 1
                break
            if white[i + 1][j + 1] and white[i + 1][j + 2] and white[i + 1][j + 3] and white[i + 1][j + 4] and \
                    white[i + 1][j + 5]:
                return 2
                break
    for i in range(15):
        for j in range(19):
            if black[i + 1][j + 1] and black[i + 2][j + 1] and black[i + 3][j + 1] and black[i + 4][j + 1] and \
                    black[i + 5][j + 1]:
                return 1
                break
            if white[i + 1][j + 1] and white[i + 2][j + 1] and white[i + 3][j + 1] and white[i + 4][j + 1] and \
                    white[i + 5][j + 1]:
                return 2
                break
    for i in range(15):
        for j in range(15):
            if black[i + 1][j + 1] and black[i + 2][j + 2] and black[i + 3][j + 3] and black[i + 4][j + 4] and \
                    black[i + 5][j + 5]:
                return 1
                break
            if white[i + 1][j + 1] and white[i + 2][j + 2] and white[i + 3][j + 3] and white[i + 4][j + 4] and \
                    white[i + 5][j + 5]:
                return 2
                break
    for i in range(15):
        for j in range(19):
            if black[i + 1][j + 1] and black[i + 2][j] and black[i + 3][j - 1] and black[i + 4][j - 2] and black[i + 5][
                        j - 3]:
                return 1
                break
            if white[i + 1][j + 1] and white[i + 2][j] and white[i + 3][j - 1] and white[i + 4][j - 2] and white[i + 5][
                        j - 3]:
                return 2
                break


def AIcompute():
    for i in range(19):
        q[i][0] = 1
        q[i][18] = 1
    for j in range(17):
        q[0][j] = 1
        q[18][j] = 1
    for i in range(17):
        for j in range(17):
            if q[i + 1][j + 1] != 0:
                for k in range(4):
                    AI[i + 1][j + 1][k] = 1
            if q[i + 1][j + 1] == 0:
                b = j + 1
                d = j + 1
                while white[i + 1][b - 1] == 1:
                    b = b - 1
                while white[i + 1][d + 1] == 1:
                    d = d + 1
                len[0] = d - b + 1
                if q[i + 1][b - 1] == 0 and q[i + 1][d + 1] == 0:
                    tb[0] = 1
                if q[i + 1][b - 1] != 0 and q[i + 1][d + 1] == 0 or q[i + 1][b - 1] == 0 and q[i + 1][d + 1] != 0:
                    tb[0] = 2
                if q[i + 1][b - 1] != 0 and q[i + 1][d + 1] != 0:
                    tb[0] = 3

                a = i + 1
                c = i + 1
                while white[a - 1][j + 1] == 1:
                    a = a - 1
                while white[c + 1][j + 1] == 1:
                    c = c + 1
                len[1] = c - a + 1
                if q[a - 1][j + 1] == 0 and q[c + 1][j + 1] == 0:
                    tb[1] = 1
                if q[a - 1][j + 1] != 0 and q[c + 1][j + 1] == 0 or q[a - 1][j + 1] == 0 and q[c + 1][j + 1] != 0:
                    tb[1] = 2
                if q[a - 1][j + 1] != 0 and q[c + 1][j + 1] != 0:
                    tb[1] = 3

                a1 = i + 1
                a2 = i + 1
                b1 = j + 1
                b2 = j + 1
                while white[a1 - 1][b1 - 1] == 1:
                    a1 = a1 - 1
                    b1 = b1 - 1
                while white[a2 + 1][b2 + 1] == 1:
                    a2 = a2 + 1
                    b2 = b2 + 1
                len[2] = a2 - a1 + 1
                if q[a1 - 1][b1 - 1] == 0 and q[a2 + 1][b2 + 1] == 0:
                    tb[2] = 1
                if q[a1 - 1][b1 - 1] != 0 and q[a2 + 1][b2 + 1] == 0 or q[a1 - 1][b1 - 1] == 0 and q[a2 + 1][
                            b2 + 1] != 0:
                    tb[2] = 2
                if q[a1 - 1][b1 - 1] != 0 and q[a2 + 1][b2 + 1] != 0:
                    tb[2] = 3

                a1 = i + 1
                a2 = i + 1
                b1 = j + 1
                b2 = j + 1
                while white[a1 - 1][b1 + 1] == 1:
                    a1 = a1 - 1
                    b1 = b1 + 1
                while white[a2 + 1][b2 - 1] == 1:
                    a2 = a2 + 1
                    b2 = b2 - 1
                len[3] = a2 - a1 + 1
                if q[a1 - 1][b1 + 1] == 0 and q[a2 + 1][b2 - 1] == 0:
                    tb[3] = 1
                if q[a1 - 1][b1 + 1] != 0 and q[a2 + 1][b2 - 1] == 0 or q[a1 - 1][b1 + 1] == 0 and q[a2 + 1][
                            b2 - 1] != 0:
                    tb[3] = 2
                if q[a1 - 1][b1 - 1] != 0 and q[a2 + 1][b2 + 1] != 0:
                    tb[3] = 3
                for k in range(4):
                    AI[i + 1][j + 1][k] = tb[k] * 10 + len[k]


def playercompute():
    for i in range(19):
        q[i][0] = 1
        q[i][16] = 1
    for j in range(19):
        q[0][j] = 1
        q[16][j] = 1
    for i in range(17):
        for j in range(17):
            if q[i + 1][j + 1] != 0:
                for k in range(4):
                    player[i + 1][j + 1][k] = 1

            if q[i + 1][j + 1] == 0:
                b = j + 1
                d = j + 1
                while black[i + 1][b - 1] == 1:
                    b = b - 1
                while black[i + 1][d + 1] == 1:
                    d = d + 1
                len[0] = d - b + 1
                if q[i + 1][b - 1] == 0 and q[i + 1][d + 1] == 0:
                    tb[0] = 1
                if q[i + 1][b - 1] != 0 and q[i + 1][d + 1] == 0 or q[i + 1][b - 1] == 0 and q[i + 1][d + 1] != 0:
                    tb[0] = 2
                if q[i + 1][b - 1] != 0 and q[i + 1][d + 1] != 0:
                    tb[0] = 3

                a = i + 1
                c = i + 1
                while black[a - 1][j + 1] == 1:
                    a = a - 1
                while black[c + 1][j + 1] == 1:
                    c = c + 1
                len[1] = c - a + 1
                if q[a - 1][j + 1] == 0 and q[c + 1][j + 1] == 0:
                    tb[1] = 1
                if q[a - 1][j + 1] != 0 and q[c + 1][j + 1] == 0 or q[a - 1][j + 1] == 0 and q[c + 1][j + 1] != 0:
                    tb[1] = 2
                if q[a - 1][j + 1] != 0 and q[c + 1][j + 1] != 0:
                    tb[1] = 3

                a1 = i + 1
                a2 = i + 1
                b1 = j + 1
                b2 = j + 1
                while black[a1 - 1][b1 - 1] == 1:
                    a1 = a1 - 1
                    b1 = b1 - 1
                while black[a2 + 1][b2 + 1] == 1:
                    a2 = a2 + 1
                    b2 = b2 + 1
                len[2] = a2 - a1 + 1
                if q[a1 - 1][b1 - 1] == 0 and q[a2 + 1][b2 + 1] == 0:
                    tb[2] = 1
                if q[a1 - 1][b1 - 1] != 0 and q[a2 + 1][b2 + 1] == 0 or q[a1 - 1][b1 - 1] == 0 and q[a2 + 1][
                            b2 + 1] != 0:
                    tb[2] = 2
                if q[a1 - 1][b1 - 1] != 0 and q[a2 + 1][b2 + 1] != 0:
                    tb[2] = 3

                a1 = i + 1
                a2 = i + 1
                b1 = j + 1
                b2 = j + 1
                while black[a1 - 1][b1 + 1] == 1:
                    a1 = a1 - 1
                    b1 = b1 + 1
                while black[a2 + 1][b2 - 1] == 1:
                    a2 = a2 + 1
                    b2 = b2 - 1
                len[3] = a2 - a1 + 1
                if q[a1 - 1][b1 + 1] == 0 and q[a2 + 1][b2 - 1] == 0:
                    tb[3] = 1
                if q[a1 - 1][b1 + 1] != 0 and q[a2 + 1][b2 - 1] == 0 or q[a1 - 1][b1 + 1] == 0 and q[a2 + 1][
                            b2 - 1] != 0:
                    tb[3] = 2
                if q[a1 - 1][b1 - 1] != 0 and q[a2 + 1][b2 + 1] != 0:
                    tb[3] = 3
                for k in range(4):
                    player[i + 1][j + 1][k] = tb[k] * 10 + len[k]


def score():
    for i in range(15):
        for j in range(15):
            AI[i + 1][j + 1][4] = 0
            player[i + 1][j + 1][4] = 0
            for k in range(4):
                if AI[i + 1][j + 1][k] == 22:
                    AI[i + 1][j + 1][4] = 10
                if player[i + 1][j + 1][k] == 22:
                    player[i + 1][j + 1][4] = 10
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 22 and AI[i + 1][j + 1][l] == 22:
                        AI[i + 1][j + 1][4] = 15
                    if player[i + 1][j + 1][k] == 22 and player[i + 1][j + 1][l] == 22:
                        player[i + 1][j + 1][4] = 15
            for k in range(4):
                if AI[i + 1][j + 1][k] == 12:
                    AI[i + 1][j + 1][4] = 20
                if player[i + 1][j + 1][k] == 12:
                    player[i + 1][j + 1][4] = 20
            for k in range(4):
                if AI[i + 1][j + 1][k] == 23:
                    AI[i + 1][j + 1][4] = 30
                if player[i + 1][j + 1][k] == 23:
                    player[i + 1][j + 1][4] = 30
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 12 and AI[i + 1][j + 1][l] == 12:
                        AI[i + 1][j + 1][4] = 40
                    if player[i + 1][j + 1][k] == 12 and player[i + 1][j + 1][l] == 12:
                        player[i + 1][j + 1][4] = 40
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 12 and AI[i + 1][j + 1][l] == 23 or AI[i + 1][j + 1][k] == 12 and \
                                    AI[i + 1][j + 1][l] == 23:
                        AI[i + 1][j + 1][4] = 45
                    if player[i + 1][j + 1][k] == 23 and player[i + 1][j + 1][l] == 12 or player[i + 1][j + 1][
                        k] == 12 and player[i + 1][j + 1][l] == 23:
                        player[i + 1][j + 1][4] = 45
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 13:
                        AI[i + 1][j + 1][4] = 50
                    if player[i + 1][j + 1][k] == 13:
                        player[i + 1][j + 1][4] = 50
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 24:
                        AI[i + 1][j + 1][4] = 60
                    if player[i + 1][j + 1][k] == 24:
                        player[i + 1][j + 1][4] = 50
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 13 and AI[i + 1][j + 1][l] == 12 or AI[i + 1][j + 1][k] == 12 and \
                                    AI[i + 1][j + 1][l] == 13:
                        AI[i + 1][j + 1][4] = 65
                    if player[i + 1][j + 1][k] == 13 and player[i + 1][j + 1][l] == 12 or player[i + 1][j + 1][
                        k] == 12 and player[i + 1][j + 1][l] == 13:
                        player[i + 1][j + 1][4] = 55
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 23 and AI[i + 1][j + 1][l] == 13 or AI[i + 1][j + 1][k] == 13 and \
                                    AI[i + 1][j + 1][l] == 23:
                        AI[i + 1][j + 1][4] = 70
                    if player[i + 1][j + 1][k] == 23 and player[i + 1][j + 1][l] == 13 or player[i + 1][j + 1][
                        k] == 13 and player[i + 1][j + 1][l] == 23:
                        player[i + 1][j + 1][4] = 70
            for k in range(4):
                for l in range(k + 1, 4):
                    if AI[i + 1][j + 1][k] == 13 and AI[i + 1][j + 1][l] == 13:
                        AI[i + 1][j + 1][4] = 80
                    if player[i + 1][j + 1][k] == 13 and player[i + 1][j + 1][l] == 13:
                        player[i + 1][j + 1][4] = 80
            for k in range(4):
                if AI[i + 1][j + 1][k] == 14:
                    AI[i + 1][j + 1][4] = 90
                if player[i + 1][j + 1][k] == 14:
                    player[i + 1][j + 1][4] = 90
            for k in range(4):
                for l in range(4):
                    if AI[i + 1][j + 1][k] == 24 and AI[i + 1][j + 1][l] == 13 or AI[i + 1][j + 1][k] == 13 and \
                                    AI[i + 1][j + 1][l] == 24:
                        AI[i + 1][j + 1][4] = 90
                    if player[i + 1][j + 1][k] == 24 and player[i + 1][j + 1][l] == 13 or player[i + 1][j + 1][
                        k] == 13 and player[i + 1][j + 1][l] == 24:
                        player[i + 1][j + 1][4] = 90
            for k in range(4):
                for l in range(4):
                    if AI[i + 1][j + 1][k] == 24 and AI[i + 1][j + 1][l] == 24:
                        AI[i + 1][j + 1][4] = 90
                    if player[i + 1][j + 1][k] == 24 and player[i + 1][j + 1][l] == 24:
                        player[i + 1][j + 1][4] = 90
            for k in range(4):
                if AI[i + 1][j + 1][k] % 5 == 0:
                    AI[i + 1][j + 1][4] = 100
                if player[i + 1][j + 1][k] % 5 == 0:
                    player[i + 1][j + 1][4] = 100

    for i in range(15):
        for j in range(15):
            if AI[m[1]][n[1]][4] < AI[i + 1][j + 1][4]:
                if q[i + 1][j + 1] == 0:
                    m[1] = i + 1
                    n[1] = j + 1
            if player[m[2]][n[2]][4] < player[i + 1][j + 1][4]:
                if q[i + 1][j + 1] == 0:
                    m[2] = i + 1
                    n[2] = j + 1
    m[0] = m[2]
    n[0] = n[2]
    if AI[m[1]][n[1]][4] >= player[m[2]][n[2]][4]:
        m[0] = m[1]
        n[0] = n[1]

#输出地点
def AIput():
    white[m[0]][n[0]] = 1
    arm.myarm(n[0], m[0])
    q[m[0]][n[0]] = Circle(p[m[0]][n[0]], 19.5)
    q[m[0]][n[0]].draw(win)
    q[m[0]][n[0]].setFill('white')
    print("AI输出相对位置：",n[0],m[0])
    for i in range(19):
        for j in range(19):
            for k in range(5):
                AI[i + 1][j + 1][k] = 0
                player[i + 1][j + 1][k] = 0
    for i in range(4):
        tb[i] = 0
        len[i] = 0


def computeree():
    WinBoard()
    cap = cv2.VideoCapture(1)  # 读入视频文件
    time1 = time.time()  # 开始下棋，计时器打开，记录开始时间
    blackx = 0
    blacky = 0
    if cap.isOpened():  # 判断是否正常打开
        rval, frame = cap.read()
    else:
        rval = False


    global lasttimeF
    signalphoto = 0

    #进入计时器循环，30s一个回合
    timeslice=30
    while rval:  # 循环读取视频帧
        rval, frame = cap.read()
        rval, frame2 = cap.read()
        #cv2.imshow("capture", frame)  # 视频窗口
        time2 = time.time()
        timeF = time2 - time1
        timeF = int(timeF)
        print("时间片",timeF)



        #signalphoto不为0时，存储白棋照片，然后将signalphoto重置为0
        if signalphoto!=0:
            url = '%d' %signalphoto + ".png"
            cv2.imwrite(url, frame2)  # 存储为图像
            cv2.imshow(url, frame2)
            print("视频测试")
            #读图矫正
            warp.makewarp(url)
            print("测试完毕")
            signalphoto=0




        #每隔30s进行操作，注意时间片不能相同，即第n秒只能执行一次
        elif timeF % timeslice == 0 and lasttimeF!=timeF:  # 每隔timeF帧进行存储操作

            lasttimeF=timeF
            count = '%d' % timeF
            url = '%d' % timeF + ".png"
            # src='%d'%c

            #输出0.png
            if timeF==0:
                cv2.imwrite(url, frame)  # 存储为图像
                cv2.imshow(url, frame)
                cv2.waitKey(10)
                # 读图矫正
                warp.makewarp(url)




            # 黑棋
            # 保存黑棋灰度差值图
            if timeF != 0 and (timeF / timeslice) % 2 == 1:
                cv2.imwrite(url, frame)  # 存储为图像
                cv2.imshow(url, frame)
                cv2.waitKey(10)
                # 读图矫正
                warp.makewarp(url)
                numtime=timeF
                #灰度图处理
                Grayurl=graypictrue.makegraypicture(url, numtime)
                # 模板匹配
                matchpicture.makematchpicture(Grayurl)
                #得到黑棋坐标
                blackx=matchpicture.x
                blacky=matchpicture.y


            #白棋
            #前十秒无棋状态，不能下棋
            elif timeF >= timeslice*2:
                # 输入黑棋坐标
                signalphoto=timeF
                Click(blackx, blacky)
                Check()
                if Check() == 1:
                    rec = Rectangle(Point(240, 240), Point(450, 450))
                    rec.setFill('green')
                    rec.draw(win)
                    Text(Point(350, 350), 'the black is the winner').draw(win)
                    break
                if Check() == 2:
                    rec = Rectangle(Point(240, 240), Point(450, 450))
                    rec.setFill('green')
                    rec.draw(win)
                    Text(Point(350, 350), 'the white is the winner').draw(win)
                    print("check1")
                    break
                AIcompute()
                playercompute()
                score()
                AIput()

                #x的坐标：p.getX()
                #y的坐标：p.getY()
                Check()
                if Check() == 1:
                    rec = Rectangle(Point(240, 240), Point(450, 450))
                    rec.setFill('green')
                    rec.draw(win)
                    Text(Point(350, 350), 'the black is the winner').draw(win)
                    break
                if Check() == 2:
                    rec = Rectangle(Point(240, 240), Point(450, 450))
                    rec.setFill('green')
                    rec.draw(win)
                    Text(Point(350, 350), 'the white is the winner').draw(win)
                    print("check2")
                    print("一回合结束")
                    break

        cv2.waitKey(1)






    #结束游戏
    cap.release()
    win.getMouse()
    win.close()
    return 0


