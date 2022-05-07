#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8

def callback(message):
	rospy.loginfo("%s", message.data)

def listener():
	rospy.init_node("listener", anonymous=True)
	rospy.Subscriber("chatter", UInt8, callback)
	rospy.spin()

if __name__=='__main__':
	listener()