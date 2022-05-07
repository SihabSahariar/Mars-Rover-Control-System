 
#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
import pynput.keyboard as Keyboard
import sys
pub = rospy.Publisher('chatter', UInt8, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)

def runForward():
    rospy.loginfo("Running FORWARD")
    pub.publish(3)

def runBackward():
    rospy.loginfo("Running BACKWARD")
    pub.publish(4)

def moveRight():
    rospy.loginfo("Moving RIGHT")
    pub.publish(2)
    
def moveLeft():
    rospy.loginfo("Moving LEFT")
    pub.publish(1)    

def stopWheels():
    rospy.loginfo("Stopped")
    pub.publish(0)

if __name__ == "__main__":
    def on_press(key):
    	try:
	        if key.char == "w":
	            runForward()
	        if key.char == "s":
	            runBackward()
	        if key.char == "d":
	            moveRight()
	        if key.char == "a":
	            moveLeft()
	    except:
	    	pass
        
        #print(key.char+" is pressed")
    def on_release(key):
        print("STOP")
        stopWheels()
    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()