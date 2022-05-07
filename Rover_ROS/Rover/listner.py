#!/usr/bin/env python
import RPi.GPIO as GPIO           # import RPi.GPIO module   
import rospy
from std_msgs.msg import UInt8

pwm_forward_left = 1
dir_forward_left = 2
pwm_forward_right = 1
dir_forward_right = 2
pwm_backward_left = 1
dir_backward_left = 2
pwm_backward_right = 1
dir_backward_right = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_forward_left, GPIO.OUT)
GPIO.setup(dir_forward_left, GPIO.OUT)
GPIO.setup(pwm_forward_right, GPIO.OUT)
GPIO.setup(dir_forward_right, GPIO.OUT)
GPIO.setup(pwm_backward_left, GPIO.OUT)
GPIO.setup(dir_backward_left, GPIO.OUT)
GPIO.setup(pwm_backward_right, GPIO.OUT)
GPIO.setup(dir_backward_right, GPIO.OUT)

def move_forward():
	GPIO.output(pwm_forward_right, 1)
	GPIO.output(dir_forward_right, 1)
	GPIO.output(pwm_backward_right, 1)
	GPIO.output(dir_backward_right, 1)

	GPIO.output(pwm_forward_left, 1)
	GPIO.output(dir_forward_left, 0)
	GPIO.output(pwm_backward_left, 1)
	GPIO.output(dir_backward_left, 0)

def move_backward():
	GPIO.output(pwm_forward_right, 1)
	GPIO.output(dir_forward_right, 0)
	GPIO.output(pwm_backward_right, 1)
	GPIO.output(dir_backward_right, 0)

	GPIO.output(pwm_forward_left, 1)
	GPIO.output(dir_forward_left, 1)
	GPIO.output(pwm_backward_left, 1)
	GPIO.output(dir_backward_left, 1)

def move_right():
	GPIO.output(pwm_forward_right, 1)
	GPIO.output(dir_forward_right, 1)
	GPIO.output(pwm_backward_right, 1)
	GPIO.output(dir_backward_right, 1)

	GPIO.output(pwm_forward_left, 1)
	GPIO.output(dir_forward_left, 1)
	GPIO.output(pwm_backward_left, 1)
	GPIO.output(dir_backward_left, 1)

def move_left():
	GPIO.output(pwm_forward_right, 1)
	GPIO.output(dir_forward_right, 0)
	GPIO.output(pwm_backward_right, 1)
	GPIO.output(dir_backward_right, 0)

	GPIO.output(pwm_forward_left, 1)
	GPIO.output(dir_forward_left, 0)
	GPIO.output(pwm_backward_left, 1)
	GPIO.output(dir_backward_left, 0)

def callback(message):
	if message == 1:
		move_forward()
	elif message == 2:
		move_left()
	elif message == 3:
		move_right()
	elif message == 4:
		move_backward()
	
	rospy.loginfo("Received data %s", message.data)

def listener():
	rospy.init_node("listener", anonymous=True)
	rospy.Subscriber("chatter", UInt8, callback)
	rospy.spin()

if __name__=='__main__':
	listener()