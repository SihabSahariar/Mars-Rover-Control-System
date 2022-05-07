#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
import pynput.keyboard as Keyboard
import sys
pub = rospy.Publisher('chatter', UInt8, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)

#ARM
def act1Forward():
    rospy.loginfo("Atc1 FORWARD")
    pub.publish(1)
def act1Backward():
    rospy.loginfo("Atc1 Backward")
    pub.publish(2)
def act2Forward():
    rospy.loginfo("Act2 FORWARD")
    pub.publish(3)
def act2Backward():
    rospy.loginfo("Act2 Backward")
    pub.publish(4)
def act3Forward():
    rospy.loginfo("Act3 Forward")
    pub.publish(5)
def act3Backward():
    rospy.loginfo("Act3 Backward")
    pub.publish(6)
def clawOpen():
    rospy.loginfo("Claw Open")
    pub.publish(7)
def clawClose():
    rospy.loginfo("Claw Close")
    pub.publish(8)
def baseClockwise():
    rospy.loginfo("Base Clockwise")
    pub.publish(9)
def baseCounterclockwise():
    rospy.loginfo("Base Counterclockwise")
    pub.publish(10)
def wristClockwise():
    rospy.loginfo("Wrist Clockwise")
    pub.publish(11)
def wristCounterclockwise():
    rospy.loginfo("Wrist Counterclockwise")
    pub.publish(12)
def stop():
    rospy.loginfo("You're Stopped")
    pub.publish(0)

#NAV
def forward():
    rospy.loginfo("You're moving FORWARD")
    pub.publish(13)
def forward_left():
    rospy.loginfo("You're moving FORWARD_LEFT")
    pub.publish(21)
def forward_right():
    rospy.loginfo("You're moving FORWARD_RIGHT")
    pub.publish(22)
def left():
    rospy.loginfo("You're moving LEFT")
    pub.publish(14)
def right():
    rospy.loginfo("You're moving RIGHT")
    pub.publish(15)
def backward():
    rospy.loginfo("You're moving BACK")
    pub.publish(16)
def backward_right():
    rospy.loginfo("You're moving BACKWARD_RIGHT")
    pub.publish(23)
def backward_left():
    rospy.loginfo("You're moving BACKWARD_LEFT")
    pub.publish(24)
def extend():
    rospy.loginfo("Extender Extending")
    pub.publish(17)
def shorten():
    rospy.loginfo("Extender Shortening")
    pub.publish(18)
def fpvFeed1():
    rospy.loginfo("FPV Feed 1")
    pub.publish(19)
def fpvFeed2():
    rospy.loginfo("FPV Feed 2")
    pub.publish(20)

if __name__ == "__main__":
    def on_press(key):
    	try:
	        #ARM
	        if key.char == '9':
	            stop()
	        elif key.char == 'r':
	            act1Forward()
	        elif key.char == 'f':
	            act1Backward()
	        elif key.char == 't':
	            act2Forward()
	        elif key.char == 'g':
	            act2Backward()
	        elif key.char == 'y':
	            act3Forward()
	        elif key.char == 'h':
	            act3Backward()
	        elif key.char == 'o':
	            clawOpen()
	        elif key.char == 'p':
	            clawClose()
	        elif key.char == 'm':
	            baseClockwise()
	        elif key.char == 'n':
	            baseCounterclockwise()
	        elif key.char == 'v':
	            wristClockwise()
	        elif key.char == 'b':
	            wristCounterclockwise()
	        #NAV
	        elif key.char == "q":
	            forward_left()
	        elif key.char == "w":
	            forward()
	        elif key.char == "e":
	            forward_right()
	        elif key.char == "a":
	            left()
	        elif key.char == "d":
	            right()
	        elif key.char == "z":
	             backward_left()
	        elif key.char == "c":
	             backward_right()
	        elif key.char == "s":
	            backward()
	        elif key.char == "k": 
	            extend()
	        elif key.char == "l":
	            shorten()
	        elif key.char == "o":
	            fpvFeed1()
	        elif key.char == "p":
	            fpvFeed2()
	        elif key.char == "x":
	            stop()
	    except:
	    	pass
        #print(key.char+" is pressed")
    def on_release(key):
        print("STOP")
        stop()
    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()