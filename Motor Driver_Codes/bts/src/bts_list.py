#!/usr/bin/env python
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import UInt8

#len_1 = 5
#ren_1 = 6
lpwm_1 = 13
rpwm_1 = 12

#len_2 = 1

#ren_2 = 2
lpwm_2 = 21
rpwm_2 = 20


def forward():
#     GPIO.output(len_1, 1)
#     GPIO.output(ren_1, 1)
#    GPIO.output(lpwm_1, 0)
    GPIO.output(rpwm_1, 255)
    #GPIO.output(lpwm_2, 0)
    GPIO.output(rpwm_2, 255)

def backward():
#     GPIO.output(len_1, 1)
#     GPIO.output(ren_1, 1)
    GPIO.output(lpwm_1, 255)
#    GPIO.output(rpwm_1, 0)
    GPIO.output(lpwm_2, 255)
    #GPIO.output(rpwm_2, 0)

def right():
#     GPIO.output(len_1, 1)
#     GPIO.output(ren_1, 1)
#    GPIO.output(lpwm_1, 0)
    GPIO.output(rpwm_1, 255)
    #GPIO.output(lpwm_2, 255)
    #GPIO.output(rpwm_2, 0)

def left():
#     GPIO.output(len_1, 1)
#     GPIO.output(ren_1, 1)
    GPIO.output(lpwm_1, 255)
#     GPIO.output(rpwm_1, 0)
    #GPIO.output(lpwm_2, 0)
    GPIO.output(rpwm_2, 255)

def stop():
#     GPIO.output(len_1, 0)
#     GPIO.output(ren_1, 0)
    GPIO.output(lpwm_1, 0)
    GPIO.output(rpwm_1, 0)
    GPIO.output(lpwm_2, 0)
    GPIO.output(rpwm_2, 0)
    

def callback(message):
    if message.data == 1:
        forward()
    elif message.data == 3:
        right()
    elif message.data == 2:
        left()
    elif message.data == 4:
        backward()
    else:
        stop()
    rospy.loginfo("Received data %s", message.data)
def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("chatter", UInt8, callback)
    rospy.spin()

if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(lpwm_1, GPIO.OUT)
    GPIO.setup(rpwm_1, GPIO.OUT)
#     GPIO.setup(len_1, GPIO.OUT)
#     GPISO.setup(ren_1, GPIO.OUT)
    GPIO.setup(lpwm_2, GPIO.OUT)
    GPIO.setup(rpwm_2, GPIO.OUT)
#     GPIO.output(len_1, 0)
#     GPIO.output(ren_1, 0)
    GPIO.output(lpwm_1,0)
    GPIO.output(rpwm_1, 0)
    GPIO.output(lpwm_2, 0)
    GPIO.output(rpwm_2, 0)
    listener()