# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.1 - June 2017 - Still under development

import uArmRobot
import time

#Configure Serial Port
serialport = "com4"          # for windows
#serialport = "/dev/ttyACM0"  # for linux like system
#a=2
#b=10

def myarm(a,b):
    x = 14 * a + 136
    y = 140 - 14 * b

    # Connect to uArm
    myRobot = uArmRobot.robot(serialport)
    # myRobot.__init__(serialport)
    myRobot.debug = True  # Enable / Disable debug output on screen, by default disabled
    myRobot.connect()
    myRobot.mode(0)  # Set mode to Normal

    time.sleep(1)

    # Move robot, command will complete when motion is completed

    myRobot.goto(150, 0, 100, 30000)
    myRobot.goto(120, 0, 100, 30000)
    myRobot.pump(True)
    time.sleep(5)

    # 一格14mm
    # 落下33mm
    myRobot.goto(x, y, 35, 30000)
    time.sleep(2)
    myRobot.pump(False)
    time.sleep(3)
    # myRobot.async_goto(112,0,32,6000)
    myRobot.goto(150, 0, 100, 30000)

    time.sleep(5)

    # Disconnect serial connection
    myRobot.disconnect()



