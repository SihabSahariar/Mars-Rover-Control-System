#!/usr/bin/env python
import RPi.GPIO as GPIO           
import rospy
from std_msgs.msg import UInt8

# Navigation 
leftPin1= 10
leftPin2= 9
rightPin1= 7
rightPin2= 8 
rightExtenderPin1 = 2 
rightExtenderPin2 = 3
# leftExtenderPin1 =  3 #16
# leftExtenderPin2 = 18
#fpvPin1 = 9
#fpvPin2 = 11

#Arm
act1pin1 = 21
act1pin2 = 20
act2pin1 = 5 
act2pin2 = 12 
act3pin1 = 6 
act3pin2 = 13 
basePin1 =  26 
basePin2 =  19 
clawPin1 =  23 
clawPin2 =  24
wristPin1 = 27 
wristPin2 = 22 

#Arm - Functions
def act1Forward ():
    GPIO.output (act1pin1, 1)
    GPIO.output (act1pin2, 0)
def act1Backward ():
    GPIO.output (act1pin1, 0)
    GPIO.output (act1pin2, 1)
def act2Forward ():
    GPIO.output (act2pin1, 1)
    GPIO.output (act2pin2, 0)  
def act2Backward ():
    GPIO.output (act2pin1, 0)
    GPIO.output (act2pin2, 1)  
def act3Forward ():
    GPIO.output (act3pin1, 1)
    GPIO.output (act3pin2, 0)  
def act3Backward ():
    GPIO.output (act3pin1, 0)
    GPIO.output (act3pin2, 1)  
def baseClockwise():
    GPIO.output (basePin1, 1)
    GPIO.output (basePin2, 0)  
def baseCounterclockwise ():
    GPIO.output (basePin1, 0)
    GPIO.output (basePin2, 1)  
def clawOpen ():
    GPIO.output (clawPin1, 1)
    GPIO.output (clawPin2, 0)  
def clawClose ():
    GPIO.output (clawPin1, 0)
    GPIO.output (clawPin2, 1)  
def wristClockwise ():
    GPIO.output (wristPin1, 1)
    GPIO.output (wristPin2, 0)  
def wristCounterclockwise():
    GPIO.output (wristPin1, 0)
    GPIO.output (wristPin2, 1)  

#Navigation Functions
def runForward ():
    rightForward ()
    leftForward ()
def runBackward ():
    rightBackward ()
    leftBackward ()  
def moveRight ():  
    leftForward ()
    rightBackward ()
def moveLeft ():
    rightForward ()
    leftBackward ()
def stopWheels ():
    rightStop ()
    leftStop ()
def extend ():
    rightExtend ()
    #leftExtend ()
def shorten ():
    rightShorten ()
    #leftShorten ()

def rightForward ():
    GPIO.output(rightPin1, 1)
    GPIO.output(rightPin2, 0)
def rightBackward ():
    GPIO.output(rightPin1, 0)
    GPIO.output(rightPin2, 1)
    rospy.loginfo('Right Back')
def rightStop ():
    GPIO.output(rightPin1, 1)
    GPIO.output(rightPin2, 1)
def leftForward ():
    GPIO.output(leftPin1, 1)
    GPIO.output(leftPin2, 0)
def leftBackward ():
    GPIO.output(leftPin1, 0)
    GPIO.output(leftPin2, 1)
    rospy.loginfo('left back')
def leftStop ():
    GPIO.output(leftPin1, 1)
    GPIO.output(leftPin2, 1)

def rightExtend ():
    GPIO.output (rightExtenderPin1, 1)
    GPIO.output (rightExtenderPin2, 0)
#def leftExtend ():
#    GPIO.output(leftExtenderPin1, 1)
#    GPIO.output(leftExtenderPin2, 0)
def rightShorten ():
    GPIO.output(rightExtenderPin1, 0)
    GPIO.output(rightExtenderPin2, 1)
    #GPIO.output(leftExtenderPin2, 1)
#def leftShorten ():
#    GPIO.output(leftExtenderPin1, 0)
#    GPIO.output(leftExtenderPin2, 1)
#def fpvFeed1 ():
#    GPIO.output(leftExtenderPin1, 0)
#    GPIO.output(leftExtenderPin2, 1)
#def fpvFeed2 ():
#    GPIO.output(leftExtenderPin1, 1)
#    GPIO.output(leftExtenderPin2, 0)


#Callback 

def callback(message): 
    if message.data == 1:
        act1Forward()
    elif message.data == 2:
        act1Backward()
    elif message.data == 3:
        act2Forward()
    elif message.data == 4:
        act2Backward()
    elif message.data == 5:
        act3Forward()
    elif message.data == 6:
        act3Backward()
    elif message.data == 7:
        clawOpen()
    elif message.data == 8:
        clawClose()
    elif message.data == 9:
        baseClockwise()
    elif message.data == 10:
        baseCounterclockwise()
    elif message.data == 11:
        wristClockwise()
    elif message.data == 12:
        wristCounterclockwise()

    '''         NAVIGATION     '''
    elif message.data == 13: 
        runForward()
    elif message.data == 14: 
        moveLeft()
    elif message.data == 15: 
        moveRight()
    elif message.data == 16: 
        runBackward()
    elif message.data == 17: 
        extend()
    elif message.data == 18: 
        shorten()
    elif message.data == 21:
	leftForward()
    elif message.data == 22:
	rightForward()
    elif message.data == 23:
	rightBackward()
    elif message.data == 24:
		leftBackward()
#    elif message.data == 19: 
#	    fpvFeed1()
#    elif message.data == 20: 
#	    fpvFeed2()
    else:
    	#Arm
    	GPIO.output(act1pin1, 0)
        GPIO.output(act1pin2, 0)
        GPIO.output(act2pin1, 0)
    	GPIO.output(act2pin2, 0)
        GPIO.output(act3pin1, 0)
        GPIO.output(act3pin2, 0)
        GPIO.output(basePin1, 0)
    	GPIO.output(basePin2, 0)
        GPIO.output(clawPin1, 0)
        GPIO.output(clawPin2, 0)
        GPIO.output(wristPin1, 0)
    	GPIO.output(wristPin2, 0)
    	#Nav
    	GPIO.output(rightPin1, 0)
        GPIO.output(rightPin2, 0)
        GPIO.output(leftPin1, 0)
    	GPIO.output(leftPin2, 0)
        GPIO.output(rightExtenderPin1,0)
        GPIO.output(rightExtenderPin2,0)
        #GPIO.output(leftExtenderPin1,0)
        #GPIO.output(leftExtenderPin2,0)

            
    rospy.loginfo("Received data %s", message.data)


def listener():
	rospy.init_node("listener", anonymous=True)
	rospy.Subscriber("chatter", UInt8, callback)
	rospy.spin()


if __name__=='__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	#Arm
	GPIO.setup(act1pin1, GPIO.OUT)
	GPIO.setup(act1pin2, GPIO.OUT)
	GPIO.setup(act2pin1, GPIO.OUT)
	GPIO.setup(act2pin2, GPIO.OUT)
	GPIO.setup(act3pin1, GPIO.OUT)
	GPIO.setup(act3pin2, GPIO.OUT)
	GPIO.setup(basePin1, GPIO.OUT)
	GPIO.setup(basePin2, GPIO.OUT)
	GPIO.setup(clawPin1, GPIO.OUT)
	GPIO.setup(clawPin2, GPIO.OUT)
	GPIO.setup(wristPin1, GPIO.OUT)
	GPIO.setup(wristPin2, GPIO.OUT)
	GPIO.output(act1pin1, 0)
	GPIO.output(act1pin2, 0)
	GPIO.output(act2pin1, 0)
	GPIO.output(act2pin2, 0)
	GPIO.setup(act3pin1, 0)
	GPIO.setup(act3pin2, 0)
	GPIO.setup(basePin1, 0)
	GPIO.setup(basePin2, 0)
	GPIO.setup(clawPin1, 0)
	GPIO.setup(clawPin2, 0)
	GPIO.setup(wristPin1, 0)
	GPIO.setup(wristPin2, 0)

	#Nav
	GPIO.setup(leftPin1, GPIO.OUT)
	GPIO.setup(leftPin2, GPIO.OUT)
	GPIO.setup(rightPin1, GPIO.OUT)
	GPIO.setup(rightPin2, GPIO.OUT)
	GPIO.setup(rightExtenderPin1, GPIO.OUT)
	GPIO.setup(rightExtenderPin2, GPIO.OUT)
	#GPIO.setup(leftExtenderPin1, GPIO.OUT)
	#GPIO.setup(leftExtenderPin2, GPIO.OUT)
	#GPIO.setup(fpvPin1, GPIO.OUT)
	#GPIO.setup(fpvPin2, GPIO.OUT)
	GPIO.output(rightPin1, 0)
	GPIO.output(rightPin2, 0)
	GPIO.output(leftPin1, 0)
	GPIO.output(leftPin2, 0)
	GPIO.output(rightExtenderPin1,0)
	GPIO.output(rightExtenderPin2,0)
	#GPIO.output(leftExtenderPin1,0)
	#GPIO.output(leftExtenderPin2,0)
	#GPIO.output(fpvPin1,0)
	#GPIO.output(fpvPin2,0)
	listener()
