import socket
import pynput.keyboard as Keyboard
import RPi.GPIO as GPIO
import sys


header=64
port=5050#Common port
format="utf-8"
dc="!disconnect"
server='192.168.0.189'#Need to be changed on different computer
ADDR=(server,port)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

#Defining PINS

leftPin1=6
leftPin2=13
rightPin1=19
rightPin2=26
rightExtenderPin1 = 16
rightExtenderPin2 = 12
leftExtenderPin1 = 7
leftExtenderPin2 = 8
fpvPin1 = 9
fpvPin2 = 11

def send(msg):
    message=msg.encode()
    msg_length=len(msg)
    send_length=str(msg_length).encode(format)
    send_length+=b' '*(header-len(send_length))
    client.send(send_length)
    client.send(message)

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
    leftExtend ()
def shorten ():
    rightShorten ()
    leftShorten ()
def rightForward ():
    GPIO.output(rightPin1, 1)
    GPIO.output(rightPin2, 0)
def rightBackward ():
    GPIO.output(rightPin1, 0)
    GPIO.output(rightPin2, 1)
def rightStop ():
    GPIO.output(rightPin1, 1)
    GPIO.output(rightPin2, 1)
def leftForward ():
    GPIO.output(leftPin1, 1)
    GPIO.output(leftPin2, 0)
def leftBackward ():
    GPIO.output(leftPin1, 0)
    GPIO.output(leftPin2, 1)
def leftStop ():
    GPIO.output(leftPin1, 1)
    GPIO.output(leftPin2, 1)

def rightExtend ():
    GPIO.output (rightExtenderPin1, 1)
    GPIO.output (rightExtenderPin2, 0)
def leftExtend ():
    GPIO.output(leftExtenderPin1, 1)
    GPIO.output(leftExtenderPin2, 0)
def rightShorten ():
    GPIO.output(rightExtenderPin1, 0)
    GPIO.output(leftExtenderPin2, 1)
def leftShorten ():
    GPIO.output(leftExtenderPin1, 0)
    GPIO.output(leftExtenderPin2, 1)
def fpvFeed1 ():
    GPIO.output(leftExtenderPin1, 0)
    GPIO.output(leftExtenderPin2, 1)
def fpvFeed2 ():
    GPIO.output(leftExtenderPin1, 1)
    GPIO.output(leftExtenderPin2, 0)
def stop():
    GPIO.output(rightPin1, 0)
    GPIO.output(rightPin2, 0)
    GPIO.output(leftPin1, 0)
    GPIO.output(leftPin2, 0)


    GPIO.output(rightExtenderPin1, 0)
    GPIO.output(rightExtenderPin2, 0)
    GPIO.output(leftExtenderPin1, 0)
    GPIO.output(leftExtenderPin2, 0)


if __name__ == "__main__":

    # Default Setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(leftPin1, GPIO.OUT)
    GPIO.setup(leftPin2, GPIO.OUT)
    GPIO.setup(rightPin1, GPIO.OUT)
    GPIO.setup(rightPin2, GPIO.OUT)
    GPIO.setup(rightExtenderPin1, GPIO.OUT)
    GPIO.setup(rightExtenderPin2, GPIO.OUT)
    GPIO.setup(leftExtenderPin1, GPIO.OUT)
    GPIO.setup(leftExtenderPin2, GPIO.OUT)
    GPIO.setup(fpvPin1, GPIO.OUT)
    GPIO.setup(fpvPin2, GPIO.OUT)
    GPIO.output(rightPin1, 0)
    GPIO.output(rightPin2, 0)
    GPIO.output(leftPin1, 0)
    GPIO.output(leftPin2, 0)
    GPIO.output(rightExtenderPin1, 0)
    GPIO.output(rightExtenderPin2, 0)
    GPIO.output(leftExtenderPin1, 0)
    GPIO.output(leftExtenderPin2, 0)
    GPIO.output(fpvPin1, 0)
    GPIO.output(fpvPin2, 0)

    def on_press(key):
        # Callback function whenever a key is pressed
        if key.char == '9':

            send(dc)
            # disconnect(key)
        elif key.char == "q":
            leftForward()
            send(key.char)

        #      led_on()
        # forward_left(key)
        elif key.char == "w":
            runForward()
            send(key.char)

            # led_off()
            # forward(key)
        elif key.char == "e":
            rightForward()
            send(key.char)
            # forward_right(key)
        elif key.char == "a":
            leftForward()
            send(key.char)
            # left(key)
        elif key.char == "d":
            rightForward()
            send(key.char)
            # right(key)
        elif key.char == "z":
            leftBackward()
            send(key.char)
            # backward_left(key)
        elif key.char == "c":
            rightBackward()
            send(key.char)
        # backward_right(key)
        elif key.char == "s":
            runBackward()
            send(key.char)
            # backward(key)
        elif key.char == "x":
            stop()
            send(key.char)
            # stop(key)
        # elif key.char == "r":
        #
        #     send(key.char)
        # elif key.char == "f":
        #
        #     send(key.char)
        # elif key.char == "t":
        #
        #     send(key.char)
        # elif key.char == "g":
        #
        #     send(key.char)
        # elif key.char == "y":
        #
        #     send(key.char)
        # elif key.char == "h":
        #
        #     send(key.char)
        # elif key.char == "u":
        #
        #     send(key.char)
        # elif key.char == "j":
        #
        #     send(key.char)
        # elif key.char == "o":
            fpvFeed1()
            send(key.char)
        elif key.char == "p":
            fpvFeed2()
            send(key.char)
        # elif key.char == "b":
        #
        #     send(key.char)
        elif key.char == "n":
            shorten()
            send(key.char)
        elif key.char == "m":
            extend()
            send(key.char)
        # elif key.char == 'i':
        #
        #     send(key.char)
        # elif key.char == 'k':
        #
        #     send(key.char)

        print(f"{key.char} is pressed")


    def on_release(key):
        # print(f'Key {key} released')

        print("Stop")
        send("Stop")
    # Stop the listener

    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



