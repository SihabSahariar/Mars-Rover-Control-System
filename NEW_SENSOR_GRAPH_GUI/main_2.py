from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import serial
import random
# arduino_port='COM7'
# baud=9600
# ser=serial.Serial(arduino_port,baud)

i = 0
hour = []
temperature = []

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1019, 824)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("background-color:rgb(38,61,95);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

   		#GRAPH
        self.plot1 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot1, 0, 0, 1, 1)
        self.plot2 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot2, 0, 1, 1, 1)
        self.plot5 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot5, 2, 0, 1, 1)
        self.plot7 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot7, 3, 0, 1, 1)
        self.plot9 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot9, 4, 0, 1, 1)
        self.plot6 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot6, 2, 1, 1, 1)
        self.plot8 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot8, 3, 1, 1, 1)
        self.plot10 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot10, 4, 1, 1, 1)
        self.plot3 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot3, 1, 0, 1, 1)
        self.plot4 = pg.PlotWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.plot4, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        #GRAPH PLOT
        self.plot1.setTitle("Test Value 1")
        self.plot2.setTitle("Test Value 2")
        self.plot3.setTitle("Test Value 3")
        self.plot4.setTitle("Test Value 4")
        self.plot5.setTitle("Test Value 5")
        self.plot6.setTitle("Test Value 6")
        self.plot7.setTitle("Test Value 7")
        self.plot8.setTitle("Test Value 8")
        self.plot9.setTitle("Test Value 9")
        self.plot10.setTitle("Test Value 10")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("MT 6.0 SENSOR BOX")
        global i
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data, i)
        self.timer.start()

    def update_plot_data(self):
        global i
        #getData=ser.readline()
        #data=int(getData)
        data = random.randint(0,20) #RANDOM VALUES
        print(data)
        hour.append(i)
        i = i+1
        temperature.append(data)
        print(temperature)
        if(len(temperature)>6):
        	temperature.pop()
        	hour.pop()
        	
        #Clear Plot
        self.plot1.clear()
        self.plot2.clear()
        self.plot3.clear()
        self.plot4.clear()
        self.plot5.clear()
        self.plot6.clear()
        self.plot7.clear()
        self.plot8.clear()
        self.plot9.clear()
        self.plot10.clear()

        #RANDOM VALUES
        self.plot1.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot2.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot3.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot4.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot5.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot6.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot7.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot8.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot9.plot(hour, temperature)
        random.shuffle(temperature)
        self.plot10.plot(hour, temperature)

        #print(data)
        # self.x = self.x[1:]  # Remove the first y element.
        # self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        # self.y = self.y[1:]  # Remove the first
        # self.y.append( randint(0,100))  # Add a new random value.
        #self.data_line.setData(hour, temperature)  # Update the data.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

