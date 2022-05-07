# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from urllib.request import urlopen, urlretrieve
import sys

#commit comment
class Window(QMainWindow):

    def __init__(self):
    	super().__init__()

    	# setting title
    	self.setWindowTitle("Rover GUI")

    	# setting geometry
    	self.setGeometry(1000,1000,1000,800)

    	# calling method
    	self.UiComponents()

    	# showing all the widgets
    	self.show()

    #def valuechange(slider, self):
     #   sliderLabel = QLabel()
      #  sliderLabel.setGeometry(700, 650, 10, 10)
       # sliderLabel.setStyleSheet("border: 3px solid orange")
        #sliderLabel.setFont(QFont('Times', 15))
        #sliderLabel.setAlignment(Qt.AlignCenter)

    def getMapImage(self, lat, lng, zoom):
        urlbase = "http://maps.google.com/maps/api/staticmap?"
        GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
        args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
        args = args + "&key=" + GOOGLEAPIKEY
        mapURL = urlbase+args
        urlretrieve(mapURL, 'googlemap.png')
        img = QPixmap('googlemap.png')
        return img


    # method for widgets
    def UiComponents(self):

    	# variables
    	# count variable
        self.count = 0
        self.latitude = 23.707310
        self.longitude = 90.415482

    	# start flag
        self.start = False

        #creating label as camera feed placeholder
#        pic = QLabel(self)
#        pixmap = QPixmap("rover1.png")
#        smaller_pixmap = pixmap.scaled(400, 300, Qt.KeepAspectRatio, Qt.FastTransformation)
#        pic.setPixmap(smaller_pixmap)
#        pic.resize(400,300)
#        pic.move(50,50)
#        pic.show()

#        pic1 = QLabel(self)
#        pixmap2 = QPixmap("astronaut.png")
#        smaller_pixmap2 = pixmap2.scaled(400,300, Qt.KeepAspectRatio, Qt.FastTransformation)
#        pic1.setPixmap(smaller_pixmap2)
#        pic1.resize(400,300)
#        pic1.move(550,50)
#        pic1.show()

        label1 = QLabel("Camera Feed 1", self)
        label1.setGeometry(50, 50,400,300)
        label1.setStyleSheet("border: 3px solid orange")
        label1.setFont(QFont('Times', 15))
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel("Camera Feed 2", self)
        label2.setGeometry(550, 50, 400, 300)
        label2.setStyleSheet("border: 3px solid orange")
        label2.setFont(QFont('Times', 15))
        label2.setAlignment(Qt.AlignCenter)


        # GPS Container
        label3 = QLabel("GPS", self)
        label3.setGeometry(700, 400, 200,200)
        label3.setStyleSheet("border: 3px solid orange")
        label3.setFont(QFont('Times', 15))
        label3.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("GPS", self)
        self.label3.setGeometry(700, 400, 200,200)
        #GPSpixmap = QPixmap('googlemap.png')
        #label3.setPixmap(GPSpixmap)
        self.label3.setStyleSheet("border: 3px solid orange")
        self.label3.setFont(QFont('Times', 15))
        self.label3.setAlignment(Qt.AlignCenter)
        # gpsGeomoetry = self.geometry().bottomRight() - label3.geometry().bottomRight() - QPoint(100, 100)
        # label3.move(gpsGeomoetry)

    	# creating push button to get time in seconds
        button = QPushButton("Set time", self)
        button.setGeometry(325, 530, 150, 50)
        button.clicked.connect(self.get_seconds)

    	# creating label to show the seconds
        self.label = QLabel("//TIMER//", self)
        self.label.setGeometry(340, 470, 300, 50)
        self.label.setStyleSheet("border : 3px solid black")
        self.label.setFont(QFont('Times', 15))
        self.label.setAlignment(Qt.AlignCenter)

    	# creating start button
        start_button = QPushButton("Start", self)
        start_button.setGeometry(500, 530, 150, 50)
        start_button.clicked.connect(self.start_action)

        # creating pause button
        pause_button = QPushButton("Pause", self)
        pause_button.setGeometry(325, 600, 150, 50)
        pause_button.clicked.connect(self.pause_action)

    	# creating reset button
        reset_button = QPushButton("Reset", self)
        reset_button.setGeometry(500, 600, 150, 50)
        reset_button.clicked.connect(self.reset_action)

    	# creating a timer object
        timer = QTimer(self)
		# adding action to timer
        timer.timeout.connect(self.showTime)
		# update the timer every tenth second
        timer.start(100)

        # creating stop button
        stopButton = QPushButton("STOP ROVER", self)
        stopButton.setGeometry(50, 400, 200, 100)
        stopButton.clicked.connect(self.stop_action)

        # creating auto mode button
        autoButton = QPushButton("AUTO MODE", self)
        autoButton.setGeometry(50, 525, 200, 100)
        autoButton.clicked.connect(self.auto_action)

        # creating manual mode button
        manualButton = QPushButton("MANUAL MODE", self)
        manualButton.setGeometry(50, 650, 200, 100)
        manualButton.clicked.connect(self.manual_action)

        #creating latitude input text box
        latitudeButton = QPushButton("Set Latitude", self)
        latitudeButton.setGeometry(700, 650, 100, 50)
        latitudeButton.clicked.connect(self.getLatitude)
        latitudeButton.setFont(QFont('Times', 11))

        #creating longitude input text box
        longitudeButton = QPushButton("Set Longitude", self)
        longitudeButton.setGeometry(800, 650, 100, 50)
        longitudeButton.clicked.connect(self.getLongitude)
        longitudeButton.setFont(QFont('Times', 11))

        # Creating slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(24)
        self.slider.setValue(12)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setGeometry(700, 600, 200, 50)
        self.slider.valueChanged.connect(self.sliderValueChanged)



    # method called by stop button
    def stop_action(self):
        print("ROVER STOPPED")

    # method called by auto mode button
    def auto_action(self):
        print("ROVER IN AUTO MODE")

    # method called by manual mode button
    def manual_action(self):
        print("ROVER IN MANUAL MODE")

	# method called by timer
    def showTime(self):

		# checking if flag is true
        if self.start:
			# incrementing the counter
            self.count -= 1

			# timer is completed
            if self.count == 0:

				# making flag false
                self.start = False

				# setting text to the label
                self.label.setText("Completed !!!! ")

        if self.start:
			# getting text from count
            text = str(self.count / 10) + " s"

			# showing text
            self.label.setText(text)


	# method called by the push button
    def get_seconds(self):

		# making flag false
        self.start = False

		# getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

		# if flag is true
        if done:
			# changing the value of count
            self.count = second * 10

			# setting text to the label

            self.label.setText(str(second))

            # self.label.setText(str(hrs)+":"+str(mins)+":"+str(second))
            #self.label.setText(str(second))
     #method to get latitude
    def getLatitude(self):
        self.latitude, ok = QInputDialog.getDouble(self, "Latitude", "Enter Latitude", 0, -90, 90)
    #method to get longitude
    def getLongitude(self):
        self.longitude, ok = QInputDialog.getDouble(self, "Longitude", "Enter Longitude", 0, -180, 180)

    #slider value change method
    def sliderValueChanged(self):
        self.getMapImage(self.latitude, self.longitude, self.slider.value())
        self.label3.clear()
        GPSpixmap = QPixmap('googlemap.png')
        self.label3.setPixmap(GPSpixmap)

    def start_action(self):
		# making flag true
        self.start = True

		# count = 0
        if self.count == 0:
            self.start = False

    def pause_action(self):

		# making flag false
        self.start = False

    def reset_action(self):

		# making flag false
        self.start = False

		# setting count value to 0
        self.count = 0

		# setting label text
        self.label.setText("//TIMER//")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
