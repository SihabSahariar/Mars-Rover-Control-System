#!/usr/bin/env python
#PySerial Code Base for IBT2      

import serial #pip install pyserial
import pynput.keyboard as Keyboard
import sys
arduino = serial.Serial(port='COM4', baudrate=9800, timeout=.1)

'''WHEEL MOVEMENT'''
def forward():
	print("ROVER IS GOING FORWARD")
	arduino.write(b'w')
def left():
	print("ROVER IS GOING LEFT")
	arduino.write(b'a')
def backward():
	print("ROVER IS GOING BACKWARD")
	arduino.write(b's')
def right():
	print("ROVER IS GOING RIGHT")
	arduino.write(b'd')

'''ARM MOVEMENT'''
def act1Forward():
    print("Act1 FORWARD")
    arduino.write(b'r')
def act1Backward():
    print("Act1 Backward")
    arduino.write(b'f')
def act2Forward():
    print("Act2 FORWARD")
    arduino.write(b't')
def act2Backward():
    print("Act2 Backward")
    arduino.write(b'g')
def act3Forward():
    print("Act3 Forward")
    arduino.write(b'y')
def act3Backward():
    print("Act3 Backward")
    arduino.write(b'h')
def baseClockwise():
    print("Base Clockwise")
    arduino.write(b'n')
def baseCounterclockwise():
    print("Base Counterclockwise")
    arduino.write(b'm')
def clawOpen():
    print("Claw Open")
    arduino.write(b'o')
def clawClose():
    print("Claw Close")
    arduino.write(b'p')
def wristClockwise():
    print("Wrist Clockwise")
    arduino.write(b'v')
def wristCounterclockwise():
    print("Wrist Counterclockwise")
    arduino.write(b'b')
def stop():
	arduino.write(b'x')

if __name__ == "__main__":
    def on_press(key):
    	try:
	        if key.char == '9':
	            stop()
	        elif key.char == 'w':
	            forward()
	        elif key.char == 's':
	            backward()
	        elif key.char == 'a':
	            left()
	        elif key.char == 'd':
	            right()
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
	        else:
	            stop()
    	except Exception as e:
	        print(f"Some Errors Occurred - {e}")

    def on_release(key):
        print("STOP")
        stop()

    with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()