#Sihab Sahariar - Control & Software Team (Mongoltori)
# pip install pyembedded
# pip install pynput

import socket
import serial
import pynput.keyboard as Keyboard
from csv import writer
from pyembedded.gps_module.gps import GPS 
import time

arduinoData=serial.Serial('COM9',9600) #Set Arduino COM Port

#CSV File Write
def data (sx, sy, osx, osy):
    diffx = osx - sx
    diffy = osy - sy
    ls = [sx, sy, osx, osy]
    with open('CSVFILE.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(ls)  
        f_object.close()

#Manual Functions
def Forward():
    print('FORWARD')
    arduinoData.write(b'w')
def Backward():
    print('BACKWARD')
    arduinoData.write(b's')
def Left():
    print('LEFT')
    arduinoData.write(b'a')
def Right():
    print('RIGHT')
    arduinoData.write(b'd')
def Stop():
    print('STOP')
    arduinoData.write(b'x')
'''
#KEYLOGGER
def on_press(key):
    try:
        if key.char == "w": #Forward
            Forward()
        elif key.char == "s": #Backward
            Backward()
        elif key.char == "a": #Left
            Left()
        elif key.char == "d": #Right
            Right()
        elif key.char == "x": #Stop
            Stop()
    except:
        pass
def on_release(key):
    print("STOP")
    Stop()
with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
'''

#GPS CONTROLLER
gps = GPS(port='COM3', baud_rate=9600) #Set GPS Device COM Port
ex = 23.472035 #Destination lat
ey = 90.218501 #Destination Long
osx = 0
osy = 0
while True:
    #print(gps.get_lat_long())
    try:
        t = gps.get_lat_long()
        sx = t[0] #Current Lat
        sy = t[1] #Current Long
        print (sx, sy) #Print Current GPS Position
        data (sx, sy, osx, osy) #Write Current GPS Position
        osx = sx
        osy = oy
        
        if (sx<ex and sy<ey):
            #print ("Moving Forward")
            Forward()
        else:
            print ("Reached Destination")
            break

    except:
        print("No Signal")
    #time.sleep(2)