#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
#import rospy
#from std_msgs.msg import UInt8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout
from PyQt5.Qt import Qt

'''
pub = rospy.Publisher('chatter', UInt8, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Control Rover
        QShortcut(Qt.Key_W, MainWindow, self.forward)
        QShortcut(Qt.Key_Q, MainWindow, self.forward_left)
        QShortcut(Qt.Key_E, MainWindow, self.forward_right)
        QShortcut(Qt.Key_S, MainWindow, self.backward)
        QShortcut(Qt.Key_Z, MainWindow, self.backward_left)
        QShortcut(Qt.Key_C, MainWindow, self.backward_right)
        QShortcut(Qt.Key_A, MainWindow, self.left)
        QShortcut(Qt.Key_D, MainWindow, self.right)
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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        MainWindow.setMinimumSize(QtCore.QSize(650, 400))
        MainWindow.setStyleSheet("QWidget{\n"
"background-color:rgb(2,4,40);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgba(155,155,155,200);\n"
"}\n"
"QPushButton:Hover{\n"
"background-color:rgb(155,155,155);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(300, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setStyleSheet("color:white;\n"
"background-color:orange;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_f = QtWidgets.QPushButton(self.centralwidget)
        self.btn_f.setObjectName("btn_f")
        self.gridLayout.addWidget(self.btn_f, 1, 1, 1, 1)
        self.btn_rf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rf.setObjectName("btn_rf")
        self.gridLayout.addWidget(self.btn_rf, 1, 2, 1, 1)
        self.btn_r = QtWidgets.QPushButton(self.centralwidget)
        self.btn_r.setObjectName("btn_r")
        self.gridLayout.addWidget(self.btn_r, 2, 2, 1, 1)
        self.btn_lb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lb.setObjectName("btn_lb")
        self.gridLayout.addWidget(self.btn_lb, 3, 0, 1, 1)
        self.btn_rb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rb.setObjectName("btn_rb")
        self.gridLayout.addWidget(self.btn_rb, 3, 2, 1, 1)
        self.btn_b = QtWidgets.QPushButton(self.centralwidget)
        self.btn_b.setObjectName("btn_b")
        self.gridLayout.addWidget(self.btn_b, 3, 1, 1, 1)
        self.btn_lf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lf.setObjectName("btn_lf")
        self.gridLayout.addWidget(self.btn_lf, 1, 0, 1, 1)
        self.btn_s = QtWidgets.QPushButton(self.centralwidget)
        self.btn_s.setObjectName("btn_s")
        self.gridLayout.addWidget(self.btn_s, 2, 1, 1, 1)
        self.btn_l = QtWidgets.QPushButton(self.centralwidget)
        self.btn_l.setObjectName("btn_l")
        self.gridLayout.addWidget(self.btn_l, 2, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 2, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(300, 20))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setStyleSheet("color:white;\n"
"background-color:orange;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.logs = QtWidgets.QTextEdit(self.centralwidget)
        self.logs.setReadOnly(True)
        self.logs.setObjectName("logs")
        self.logs.setStyleSheet("color:white")
        self.verticalLayout_2.addWidget(self.logs)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 3, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(300, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("color:white;\n"
"background-color:orange;color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.speed = QtWidgets.QSlider(self.centralwidget)
        self.speed.setMaximum(255)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setObjectName("speed")
        self.verticalLayout.addWidget(self.speed)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(300, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setStyleSheet("color:white;\n"
"background-color:orange;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(31)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.arm1 = QtWidgets.QSlider(self.centralwidget)
        self.arm1.setMaximum(255)
        self.arm1.setOrientation(QtCore.Qt.Vertical)
        self.arm1.setObjectName("arm1")
        self.horizontalLayout.addWidget(self.arm1)
        self.arm2 = QtWidgets.QSlider(self.centralwidget)
        self.arm2.setMaximum(255)
        self.arm2.setOrientation(QtCore.Qt.Vertical)
        self.arm2.setObjectName("arm2")
        self.horizontalLayout.addWidget(self.arm2)
        self.arm3 = QtWidgets.QSlider(self.centralwidget)
        self.arm3.setMaximum(255)
        self.arm3.setOrientation(QtCore.Qt.Vertical)
        self.arm3.setObjectName("arm3")
        self.horizontalLayout.addWidget(self.arm3)
        self.arm4 = QtWidgets.QSlider(self.centralwidget)
        self.arm4.setMaximum(255)
        self.arm4.setOrientation(QtCore.Qt.Vertical)
        self.arm4.setObjectName("arm4")
        self.horizontalLayout.addWidget(self.arm4)
        self.arm5 = QtWidgets.QSlider(self.centralwidget)
        self.arm5.setMaximum(255)
        self.arm5.setOrientation(QtCore.Qt.Vertical)
        self.arm5.setObjectName("arm5")
        self.horizontalLayout.addWidget(self.arm5)
        self.arm6 = QtWidgets.QSlider(self.centralwidget)
        self.arm6.setOrientation(QtCore.Qt.Vertical)
        self.arm6.setObjectName("arm6")
        self.arm6.setMaximum(255)
        self.horizontalLayout.addWidget(self.arm6)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mongoltori Control Panel - 2021"))
        self.label.setText(_translate("MainWindow", "ROVER CONTROLLER"))
        self.label_4.setText(_translate("MainWindow", "WHEEL CONTROL :"))
        self.btn_f.setText(_translate("MainWindow", "Forward"))
        self.btn_rf.setText(_translate("MainWindow", "R. Forward"))
        self.btn_r.setText(_translate("MainWindow", "Right"))
        self.btn_lb.setText(_translate("MainWindow", "L. Backward"))
        self.btn_rb.setText(_translate("MainWindow", "R. Backward"))
        self.btn_b.setText(_translate("MainWindow", "Back"))
        self.btn_lf.setText(_translate("MainWindow", "L. Forward"))
        self.btn_s.setText(_translate("MainWindow", "Stop"))
        self.btn_l.setText(_translate("MainWindow", "Left"))
        self.label_5.setText(_translate("MainWindow", "LOGS :"))
        self.label_2.setText(_translate("MainWindow", "SPEED CONTROL :"))
        self.label_3.setText(_translate("MainWindow", "ARM CONTROL :"))

# Rover Control
    def forward(self):
        print("Forward")
        '''
        rospy.loginfo("Forward")
        pub.publish(1)
        '''
        self.logs.setText(self.logs.toPlainText()+"Forward\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def forward_left(self):
        print("Forward Left")
        '''
        rospy.loginfo("Forward Left")
        pub.publish(2)
        '''
        self.logs.setText(self.logs.toPlainText()+"Left Forward\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def forward_right(self):
        print("Forward Right")
        '''
        rospy.loginfo("Forward Right")
        pub.publish(3)
        '''
        self.logs.setText(self.logs.toPlainText()+"Right Forward\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def left(self):
        print("Left")
        '''
        rospy.loginfo("Left")
        pub.publish(4)
        '''
        self.logs.setText(self.logs.toPlainText()+"Left\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def right(self):
        print("Right")
        '''
        rospy.loginfo("Right")
        pub.publish(5)
        '''
        self.logs.setText(self.logs.toPlainText()+"Right\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def backward(self):
        print("Backward")
        '''
        rospy.loginfo("Backward")
        pub.publish(6)
        '''
        self.logs.setText(self.logs.toPlainText()+"Backward\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def backward_right(self):
        print("Backward Right")
        '''
        rospy.loginfo("Backward Right")
        pub.publish(7)
        '''
        self.logs.setText(self.logs.toPlainText()+"Right Backward\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def backward_left(self):
        print("Backward Left")
        '''
        rospy.loginfo("Backward Left")
        pub.publish(8)
        '''
        self.logs.setText(self.logs.toPlainText()+"Left Backward\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm1Front(self):
        self.arm1.setValue(self.arm1.value() + 1)
        print("Arm1 Up")
        '''
        rospy.loginfo("Arm1 Up")
        pub.publish(9)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm1 Up\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())

    def Arm1Back(self):
        self.arm1.setValue(self.arm1.value() - 1)
        print("Arm1 Down")
        '''
        rospy.loginfo("Arm1 Down")
        pub.publish(10)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm1 Down\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm2Front(self):
        self.arm2.setValue(self.arm2.value() + 1)
        print("Arm2 Up")
        '''
        rospy.loginfo("Arm2 Up")
        pub.publish(11)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm2 Up\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm2Back(self):
        self.arm2.setValue(self.arm2.value() - 1)
        print("Arm2 Down")
        '''
        rospy.loginfo("Arm2 Down")
        pub.publish(12)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm2 Down\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm3Front(self):
        self.arm3.setValue(self.arm3.value() + 1)
        print("Arm3 Up")
        '''
        rospy.loginfo("Arm3 Up")
        pub.publish(13)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm3 Up\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm3Back(self):
        self.arm3.setValue(self.arm3.value() - 1)
        print("Arm3 Down")
        '''
        rospy.loginfo("Arm3 Down")
        pub.publish(14)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm3 Down\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm4Front(self):
        self.arm4.setValue(self.arm4.value() + 1)
        print("Arm4 Up")
        '''
        rospy.loginfo("Arm4 Up")
        pub.publish(15)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm4 Up\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm4Back(self):
        self.arm4.setValue(self.arm4.value() - 1)
        print("Arm4 Down")
        '''
        rospy.loginfo("Arm4 Down")
        pub.publish(16)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm4 Down\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm5Front(self):
        self.arm5.setValue(self.arm5.value() + 1)
        print("Arm5 Up")
        '''
        rospy.loginfo("Arm5 Up")
        pub.publish(17)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm5 Up\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm5Back(self):
        self.arm5.setValue(self.arm5.value() - 1)
        print("Arm5 Down")
        '''
        rospy.loginfo("Arm5 Down")
        pub.publish(18)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm5 Down\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm6Front(self):
        self.arm6.setValue(self.arm6.value() + 1)
        print("Arm6 Up")
        '''
        rospy.loginfo("Arm6 Up")
        pub.publish(19)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm6 Up\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())
    def Arm6Back(self):
        self.arm6.setValue(self.arm6.value() - 1)
        print("Arm6 Down")
        '''
        rospy.loginfo("Arm6 Down")
        pub.publish(20)
        '''
        self.logs.setText(self.logs.toPlainText()+"Arm6 Down\n")
        x = self.logs.verticalScrollBar()
        x.setValue(x.maximum())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

