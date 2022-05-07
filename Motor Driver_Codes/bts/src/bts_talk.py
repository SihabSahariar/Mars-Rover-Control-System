#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
import pynput.keyboard as Keyboard
import sys
pub = rospy.Publisher('chatter', UInt8, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)

def forward():
    rospy.loginfo("You're moving FORWARD")
    pub.publish(1)
def left():
    rospy.loginfo("You're moving LEFT")
    pub.publish(2)
def right():
    rospy.loginfo("You're moving RIGHT")
    pub.publish(3)
def backward():
    rospy.loginfo("You're moving BACK")
    pub.publish(4)
def stop():
    rospy.loginfo("You're Stopped")
    pub.publish(0)
    
if __name__ == "__main__":
    def on_press(key):
    	try:
	        if key.char == '9':
	            stop()
	        elif key.char == "w":
	            forward()
	        elif key.char == "a":
	            left()
	        elif key.char == "d":
	            right()
	        elif key.char == "s":
	            backward()
	        elif key.char == "x":
	            stop()
	    except:
	    	pass
            
        #print(key.char+ "is pressed")
    def on_release(key):
        print("STOP")
        stop()
    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()