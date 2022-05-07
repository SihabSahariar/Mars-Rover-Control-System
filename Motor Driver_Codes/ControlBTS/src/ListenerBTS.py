#!/usr/bin/env python
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import UInt8

#leftEnable1 = 9
#leftEnable2 = 25
leftPWM1 = 17
leftPWM2 = 12

#rightEnable1 = 10
#rightEnable2 = 18
rightPWM1 = 6
rightPWM2 = 13

def forward():
    #GPIO.output(leftEnable1, 1)
    #GPIO.output(leftEnable2, 1)
    #GPIO.output(rightEnable1, 1)
    #GPIO.output(rightEnable2, 1)
    
    #GPIO.output(leftPWM1, 0)
    GPIO.output(leftPWM2, 255)
    #GPIO.output(rightPWM1, 0)
    GPIO.output(rightPWM2, 255)

def backward():
    #GPIO.output(leftEnable1, 1)
    #GPIO.output(leftEnable2, 1)
    #GPIO.output(rightEnable1, 1)
    #GPIO.output(rightEnable2, 1)
    
    GPIO.output(leftPWM1, 255)
    #GPIO.output(leftPWM2, 0)
    GPIO.output(rightPWM1, 255)
    #GPIO.output(rightPWM2, 0)

def right():
    #GPIO.output(leftEnable1, 1)
    #GPIO.output(leftEnable2, 1)
    #GPIO.output(rightEnable1, 1)
    #GPIO.output(rightEnable2, 1)
    
    #GPIO.output(leftPWM1, 0)
    GPIO.output(leftPWM2, 255)
    GPIO.output(rightPWM1, 255)
    #GPIO.output(rightPWM2, 0)

def left():
    #GPIO.output(leftEnable1, 1)
    #GPIO.output(leftEnable2, 1)
    #GPIO.output(rightEnable1, 1)
    #GPIO.output(rightEnable2, 1)
    
    GPIO.output(leftPWM1, 255)
    #GPIO.output(leftPWM2, 0)
    #GPIO.output(rightPWM1, 0)
    GPIO.output(rightPWM2, 255)

def top():
    #GPIO.output(leftEnable1, 0)
    #GPIO.output(leftEnable2, 0)
    #GPIO.output(rightEnable1, 0)
    #GPIO.output(rightEnable2, 0)
    
    GPIO.output(leftPWM1, 0)
    GPIO.output(leftPWM2, 0)
    GPIO.output(rightPWM1, 0)
    GPIO.output(rightPWM2, 0)

def callback(message):
    if message.data == 13:
        forward()
    elif message.data == 14:
	    right()
    elif message.data == 15:
	    left()
    elif message.data == 16:
	    backward()
    rospy.loginfo("Received data %s", message.data)

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("chatter", UInt8, callback)
    rospy.spin()

if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #GPIO.setup(leftEnable1, GPIO.OUT)
    #GPIO.setup(leftEnable2, GPIO.OUT)
    GPIO.setup(leftPWM1, GPIO.OUT)
    GPIO.setup(leftPWM2, GPIO.OUT)
    #GPIO.setup(rightEnable1, GPIO.OUT)
    #GPIO.setup(rightEnable2, GPIO.OUT)
    GPIO.setup(rightPWM1, GPIO.OUT)
    GPIO.setup(rightPWM2, GPIO.OUT)
    #GPIO.output(leftEnable1,0)
    #GPIO.output(leftEnable2,0)
    GPIO.output(leftPWM1, 0)
    GPIO.output(leftPWM2, 0)
    #GPIO.output(rightEnable1, 0)
    #GPIO.output(rightEnable2, 0)
    GPIO.output(rightPWM1, 0)
    GPIO.output(rightPWM2, 0)
    listener()