import RPi.GPIO as GPIO           
import rospy
from std_msgs.msg import UInt8
 
int clockwise = 0
int counterClockwise = 1 
 
pwmLeft = 20
dirLeft = 21
pwmRight = 16
dirRight = 12

def runForward ():
  rightForward ()
  leftBackward ()

def runBackward():
  rightBackward ()
  leftBackward ()

def moveRight ():
  leftForward ()
  rightStop ()

def moveLeft():
  rightForward ()
  leftStop()
 
def stopWheels ():
  rightStop ()
  leftStop ()

def rightStop():
  GPIO.output (pwmRight, 0)

def rightForward ():
  GPIO.output (pwmRight, 1)
  GPIO.output (dirRight, counterClockwise)

def leftStop():
  GPIO.output (pwmLeft, 0)

def leftForward():
  GPIO.output (pwmLeft, 1)
  GPIO.output (dirLeft, clockwise)

def rightBackward ():
  GPIO.output (pwmRight, 1)
  GPIO.output (dirRight, clockwise)

def leftBackward ():  
  GPIO.output (pwmLeft, 1)
  GPIO.output (dirLeft, counterClockwise)

def callback (message):
    if message.data == 1:
        moveLeft()
    elif message.data == 2:
        moveRight ()
    elif message.data == 3:
        runForward ()
    elif message.data == 4:
        runBackward ()
    elif message.data == 0:
        stopWheels ()
    else:
        GPIO.output(pwmLeft, 0)
        GPIO.output(dirLeft, 0)
        GPIO.output(pwmRight, 0)
        GPIO.output(dirRight , 0)
    
    rospy.loginfo("Received data %s", message.data)

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("chatter", UInt8, callback)
    rospy.spin()


if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(pwmLeft, GPIO.OUT)
    GPIO.setup(pwmRight, GPIO.OUT)
    GPIO.setup(dirLeft, GPIO.OUT)
    GPIO.setup(dirRIght, GPIO.OUT)
    GPIO.output(pwmLeft, 0)
    GPIO.output(pwmRight, 0)
    GPIO.output(dirLeft, 0)
    GPIO.output(dirRight, 0)

    listener()
