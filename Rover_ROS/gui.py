#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout
from PyQt5.Qt import Qt
from help import Ui_help

pub = rospy.Publisher('chatter', UInt8, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)

class Ui_MainWindow(object):
 
    pub = rospy.Publisher('chatter', UInt8, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_help()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        #Control Speed
            #Same as Arm Code (If need to implement)

        #Control Rover
        QShortcut(Qt.Key_W, MainWindow, self.forward)
        QShortcut(Qt.Key_Q, MainWindow, self.forward_left)
        QShortcut(Qt.Key_E, MainWindow, self.forward_right)
        QShortcut(Qt.Key_S, MainWindow, self.backward)
        QShortcut(Qt.Key_Z, MainWindow, self.backward_left)
        QShortcut(Qt.Key_C, MainWindow, self.backward_right)
        QShortcut(Qt.Key_A, MainWindow, self.left)
        QShortcut(Qt.Key_D, MainWindow, self.right)

        '''
        QShortcut(Qt.Key_Escape, MainWindow, self.stop) #No need anymore but still kept.(removed "STOP" Button)
        '''
        #Control Arms
        QShortcut(Qt.Key_R, MainWindow, self.Arm1Front)
        QShortcut(Qt.Key_F, MainWindow, self.Arm1Back)

        QShortcut(Qt.Key_T, MainWindow, self.Arm2Front)
        QShortcut(Qt.Key_G, MainWindow, self.Arm2Back)

        QShortcut(Qt.Key_Y, MainWindow, self.Arm3Front)
        QShortcut(Qt.Key_H, MainWindow, self.Arm3Back)

        QShortcut(Qt.Key_U, MainWindow, self.Arm4Front)
        QShortcut(Qt.Key_J, MainWindow, self.Arm4Back)

        QShortcut(Qt.Key_I, MainWindow, self.Arm5Front)
        QShortcut(Qt.Key_K, MainWindow, self.Arm5Back)

        QShortcut(Qt.Key_O, MainWindow, self.Arm6Front)
        QShortcut(Qt.Key_L, MainWindow, self.Arm6Back)
        #Cam Control
        QShortcut(Qt.Key_V, MainWindow, self.Cam1) #Overlapping with backward_left(Solved)
        QShortcut(Qt.Key_B, MainWindow, self.Cam2)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1447, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1451, 811))
        self.label.setStyleSheet("background-image: url(:/newPrefix/main.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(110, 240, 321, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(50, 479, 22, 121))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(120, 480, 22, 121))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(200, 480, 22, 121))
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setGeometry(QtCore.QRect(270, 480, 22, 121))
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_5.setGeometry(QtCore.QRect(340, 480, 22, 121))
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_6.setGeometry(QtCore.QRect(420, 480, 22, 121))
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 480, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(830, 480, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(510, 520, 431, 241))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 480, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 130, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 130, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 130, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 200, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(650, 200, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(800, 200, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 270, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 270, 121, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(800, 270, 121, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 700, 161, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(260, 700, 161, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(1130, 680, 151, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_14.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Camera Control
    def Cam1(event):
        #print("Ant/Box")
        rospy.loginfo("Ant/Box")
        pub.publish(21)
        rate.sleep()
    def Cam2(event):
        #print("Bot/Arm")
        rospy.loginfo("Bot/Arm")
        pub.publish(22)
        rate.sleep()

# Rover Control
    def forward(event):
        #print("Forward")
        rospy.loginfo("Forward")
        pub.publish(1)
        rate.sleep()


    def forward_left(event):
        #print("Forward Left")
        rospy.loginfo("Forward Left")
        pub.publish(2)
        rate.sleep()

    def forward_right(event):
        #print("Forward Right")
        rospy.loginfo("Forward Right")
        pub.publish(3)
        rate.sleep()

    def left(event):
        #print("Left")
        rospy.loginfo("Left")
        pub.publish(8)
        rate.sleep()

    def right(event):
        #print("Right")
        rospy.loginfo("Right")
        pub.publish(7)
        rate.sleep()

    def backward(event):
        #print("Backward")
        rospy.loginfo("Backward")
        pub.publish(4)
        rate.sleep()

    def backward_right(event):
        #print("Backward Right")
        rospy.loginfo("Backward Right")
        pub.publish(6)
        rate.sleep()

    def backward_left(event):
        # print("")
        rospy.loginfo("Backward Left")
        pub.publish(5)
        rate.sleep()

    def Arm1Front(self):
        if self.verticalSlider.value() <= 97:
            self.verticalSlider.setValue(self.verticalSlider.value() + 2)
            #print("Arm1 Up")
            rospy.loginfo("Arm1 Up")
            pub.publish(9)
            rate.sleep()
        else:
            print("Can't go Up more")

    def Arm1Back(self):
        if self.verticalSlider.value() != 0:
            self.verticalSlider.setValue(self.verticalSlider.value() - 2)
            #print("Arm1 Down")
            rospy.loginfo("Arm1 Down")
            pub.publish(10)
            rate.sleep()
        else:
            print("Can't go down more")

    def Arm2Front(self):
        if self.verticalSlider_2.value() <= 97:
            self.verticalSlider_2.setValue(self.verticalSlider_2.value() + 2)
            #print("Arm2 Up")
            rospy.loginfo("Arm2 Up")
            pub.publish(11)
            rate.sleep()
        else:
            print("Can't go Up more")

    def Arm2Back(self):
        if self.verticalSlider_2.value() != 0:
            self.verticalSlider_2.setValue(self.verticalSlider_2.value() - 2)
            #print("Arm2 Down")
            rospy.loginfo("Arm2 Down")
            pub.publish(12)
            rate.sleep()
        else:
            print("Can't go down more")

    def Arm3Front(self):
        if self.verticalSlider_3.value() <= 97:
            self.verticalSlider_3.setValue(self.verticalSlider_3.value() + 2)
            #print("Arm3 Up")
            rospy.loginfo("Arm3 Up")
            pub.publish(13)
            rate.sleep()
        else:
            print("Can't go Up more")

    def Arm3Back(self):
        if self.verticalSlider_3.value() != 0:
            self.verticalSlider_3.setValue(self.verticalSlider_3.value() - 2)
            print("Arm3 Down")
            rospy.loginfo("Arm3 Down")
            pub.publish(14)
            rate.sleep()
        else:
            print("Can't go down more")

    def Arm4Front(self):
        if self.verticalSlider_4.value() <= 97:
            self.verticalSlider_4.setValue(self.verticalSlider_4.value() + 2)
            #print("Arm4 Up")
            rospy.loginfo("Arm4 Up")
            pub.publish(15)
            rate.sleep()
        else:
            print("Can't go Up more")

    def Arm4Back(self):
        if self.verticalSlider_4.value()!=0:
            self.verticalSlider_4.setValue(self.verticalSlider_4.value() - 2)
            #print("Arm4 Down")
            rospy.loginfo("Arm4 Down")
            pub.publish(16)
            rate.sleep()
        else:
            print("Can't go down more")

    def Arm5Front(self):
        if self.verticalSlider_5.value() <= 97:
            self.verticalSlider_5.setValue(self.verticalSlider_5.value() + 2)
            #print("Arm5 Up")
            rospy.loginfo("Arm5 Up")
            pub.publish(17)
            rate.sleep()
        else:
            print("Can't go Up more")

    def Arm5Back(self):
        if self.verticalSlider_5.value() != 0:
            self.verticalSlider_5.setValue(self.verticalSlider_5.value() - 2)
            #print("Arm5 Down")
            rospy.loginfo("Arm5 Down")
            pub.publish(18)
            rate.sleep()
        else:
            print("Can't go down more")

    def Arm6Front(self):
        if self.verticalSlider_6.value() <= 97:
            self.verticalSlider_6.setValue(self.verticalSlider_6.value() + 2)
            #print("Arm6 Up")
            rospy.loginfo("Arm6 Up")
            pub.publish(19)
            rate.sleep()
        else:
            print("Can't go Up more")

    def Arm6Back(self):
        if self.verticalSlider_6.value()!=0:
            self.verticalSlider_6.setValue(self.verticalSlider_6.value() - 2)
            #print("Arm6 Down")
            rospy.loginfo("Arm6 Down")
            pub.publish(20)
            rate.sleep()
        else:
            print("Can't go down more")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mongoltori Control Panel - 2021"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.radioButton.setText(_translate("MainWindow", "KEYBOARD"))
        self.pushButton_2.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_3.setText(_translate("MainWindow", "Left Forward"))
        self.pushButton_4.setText(_translate("MainWindow", "Forward"))
        self.pushButton_5.setText(_translate("MainWindow", "Right Forward"))
        self.pushButton_6.setText(_translate("MainWindow", "Left"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_8.setText(_translate("MainWindow", "Right"))
        self.pushButton_9.setText(_translate("MainWindow", "Left Backward"))
        self.pushButton_10.setText(_translate("MainWindow", "Back"))
        self.pushButton_11.setText(_translate("MainWindow", "Right Backward"))
        self.pushButton_12.setText(_translate("MainWindow", "Ant/Box"))
        self.pushButton_13.setText(_translate("MainWindow", "Bot/Arm"))
        self.pushButton_14.setText(_translate("MainWindow", "HELP"))
    
import ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    