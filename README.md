# chessplaying_robot
工程实训的课设，菜神教你三天挑战极限，“给大佬递棋”！
四个人组队完成的，之前完全没接触过图像处理，也没玩过机械臂这种跟硬件结合的玩法。。。带小伙伴配python的环境就用了半天，最后两天大家抢机械臂调试也是很火热。。。好在总算赶在最后一刻完成了orz

规则：人下黑棋，电脑下白棋，黑棋先手。机械臂运动结束后方可继续下黑棋。

main.py是主程序，调用AI.computeree()。

AI.py包含了五子棋AI算法，参考了网上的开源代码，函数AI.computeree()包含了整个人机下棋的流程（打开计时器和摄像头，根据时间片让电脑跟人轮流下棋）。
AInomachine.py是不带机械臂的代码，调试时用的。

VideoCapture.py是测试摄像头用的代码。

uArmRobot.py，uArmRobot.pyc是机械臂的控制代码（机械臂自带的，调用它们需要安装驱动和使用合适的com口），machintest.py是一个调试机械臂用的代码，basic_example.py和multi_robot_example.py是两个官方实例。

arm.py是根据计算出的棋盘相对位置让机械臂摆放棋子的代码。

graypictrue.py是使得图片灰度化的算法，matchpicture.py是模板匹配算法，warp.py是图像矫正算法，这三个算法都有借鉴开源代码。

数字.jpg是人机下棋过程中摄像机拍照产生的原始照片。

