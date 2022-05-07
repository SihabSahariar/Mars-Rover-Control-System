#!/usr/bin/env python
import RPi.GPIO as GPIO           
import rospy
from std_msgs.msg import UInt8

pwmValue = 70

#Arm
act1pin1 = 20 #26
act1pin2 = 21 #19
act1PWM = 18 
act2pin1 = 26 #23 
act2pin2 = 19 #24
act2PWM = 12
act3pin1 = 0 #5 
act3pin2 = 0 #12
act3PWM = 0
basePin1 = 0 #21 
basePin2 = 0 #20
basePWM = 0
clawPin1 = 22 #27 
clawPin2 = 27 #22
clawPWM = 0
wristPin1 = 23 #6 
wristPin2 = 24 #13
wristPWM = 0

#Arm - Functions
def act1Forward ():
    GPIO.output (act1pin1, 1)
    GPIO.output (act1pin2, 0)
    GPIO.output (act1PWM, pwmValue)
def act1Backward ():
    GPIO.output (act1pin1, 0)
    GPIO.output (act1pin2, 1)
    GPIO.output (act1PWM, pwmValue)
def act2Forward ():
    GPIO.output (act2pin1, 1)
    GPIO.output (act2pin2, 0)
    GPIO.output (act2PWM, pwmValue)
def act2Backward ():
    GPIO.output (act2pin1, 0)
    GPIO.output (act2pin2, 1)
    GPIO.output (act2PWM, pwmValue)
def act3Forward ():
    GPIO.output (act3pin1, 1)
    GPIO.output (act3pin2, 0)
    GPIO.output (act3PWM, pwmValue)
def act3Backward ():
    GPIO.output (act3pin1, 0)
    GPIO.output (act3pin2, 1)
    GPIO.output (act3PWM, pwmValue)
def baseClockwise():
    GPIO.output (basePin1, 1)
    GPIO.output (basePin2, 0)
    GPIO.output (basePWM, pwmValue)
def baseCounterclockwise ():
    GPIO.output (basePin1, 0)
    GPIO.output (basePin2, 1)
    GPIO.output (basePWM, pwmValue)
def clawOpen ():
    GPIO.output (clawPin1, 1)
    GPIO.output (clawPin2, 0)
    GPIO.output (clawPWM, pwmValue)
def clawClose ():
    GPIO.output (clawPin1, 0)
    GPIO.output (clawPin2, 1)
    GPIO.output (clawPWM, pwmValue)
def wristClockwise ():
    GPIO.output (wristPin1, 1)
    GPIO.output (wristPin2, 0)
    GPIO.output (wristPWM, pwmValue)
def wristCounterclockwise():
    GPIO.output (wristPin1, 0)
    GPIO.output (wristPin2, 1)
    GPIO.output (wristPWM, pwmValue)


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
    else:
        #Arm
        GPIO.output(act1pin1, 0)
        GPIO.output(act1pin2, 0)
        GPIO.output(act1PWM, 0)
        GPIO.output(act2pin1, 0)
        GPIO.output(act2pin2, 0)
        GPIO.output(act2PWM, 0)
        GPIO.output(act3pin1, 0)
        GPIO.output(act3pin2, 0)
        GPIO.output(act3PWM, 0)
        GPIO.output(basePin1, 0)
        GPIO.output(basePin2, 0)
        GPIO.output(basePWM, 0)
        GPIO.output(clawPin1, 0)
        GPIO.output(clawPin2, 0)
        GPIO.output(clawPWM, 0)
        GPIO.output(wristPin1, 0)
        GPIO.output(wristPin2, 0)
        GPIO.output(wristPWM, 0)
           
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
	GPIO.setup(act1PWM, GPIO.OUT)
	GPIO.setup(act2pin1, GPIO.OUT)
	GPIO.setup(act2pin2, GPIO.OUT)
	GPIO.setup(act2PWM, GPIO.OUT)
	GPIO.setup(act3pin1, GPIO.OUT)
	GPIO.setup(act3pin2, GPIO.OUT)
	GPIO.setup(act3PWM, GPIO.OUT)	
	GPIO.setup(basePin1, GPIO.OUT)
	GPIO.setup(basePin2, GPIO.OUT)
	GPIO.setup(basePWM, GPIO.OUT)
	GPIO.setup(clawPin1, GPIO.OUT)
	GPIO.setup(clawPin2, GPIO.OUT)
	GPIO.setup(clawPWM, GPIO.OUT)
	GPIO.setup(wristPin1, GPIO.OUT)
	GPIO.setup(wristPin2, GPIO.OUT)
	GPIO.setup(wristPWM, GPIO.OUT)
	GPIO.output(act1pin1, 0)
	GPIO.output(act1pin2, 0)
	GPIO.output(act1PWM, 0)
	GPIO.output(act2pin1, 0)
	GPIO.output(act2pin2, 0)
	GPIO.output(act2PWM, 0)
	GPIO.setup(act3pin1, 0)
	GPIO.setup(act3pin2, 0)
	GPIO.output(act3PWM, 0)
	GPIO.setup(basePin1, 0)
	GPIO.setup(basePin2, 0)
	GPIO.output(basePWM, 0)
	GPIO.setup(clawPin1, 0)
	GPIO.setup(clawPin2, 0)
	GPIO.output(clawPWM, 0)
	GPIO.setup(wristPin1, 0)
	GPIO.setup(wristPin2, 0)
	GPIO.output(wristPWM, 0)
	listener()
