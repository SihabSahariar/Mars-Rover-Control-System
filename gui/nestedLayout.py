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
        self.setWindowTitle("GUI")
        self.window_w = 1000
        self.window_h = 800

        # creating layouts
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.bottom_left_layout = QVBoxLayout()
        self.bottom_middle_layout = QVBoxLayout()
        self.timer_button_layout = QGridLayout()
        self.bottom_right_layout = QVBoxLayout()
        self.gps_layout = QVBoxLayout()
        self.lat_lng_layout = QHBoxLayout()


        #nest layouts

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.bottom_layout.addLayout(self.bottom_left_layout)
        self.bottom_layout.addLayout(self.bottom_middle_layout)
        self.bottom_layout.addLayout(self.bottom_right_layout)
              #self.bottom_middle_layout.addLayout(self.timer_button_layout)
        self.bottom_right_layout.addLayout(self.gps_layout)
        self.bottom_right_layout.addLayout(self.lat_lng_layout)


         # add to gps_layout

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        self._create_slider()
        self._create_gps_buttons()
        self._create_video_feeds()
        self._create_gps()
        self._create_modes()
        self._create_timer()
        self._create_timer_buttons()
        self.create_timer()

    def _create_video_feeds(self):
        self.vid1 = QLabel(self) #realsense
        self.vid2 = QLabel(self)
        self.vid1.setStyleSheet("border: 3px solid orange")
        self.vid2.setStyleSheet("border: 3px solid orange")
        self.top_layout.addWidget(self.vid1)
        self.top_layout.addWidget(self.vid2)

    def _create_timer(self):
        self.label = QLabel("//TIMER//", self)
        self.label.setStyleSheet("border : 3px solid black")
        self.label.setFont(QFont('Times', 15))
        self.bottom_middle_layout.addWidget(self.label)
        self.bottom_middle_layout.addLayout(self.timer_button_layout)

    def _create_timer_buttons(self):
         # creating push button to get time in seconds
         self.button = QPushButton("Set time", self)
         self.button.clicked.connect(self.get_seconds)
         #self.button.clicked.connect(self.get_seconds)
         # creating start button
         self.start_button = QPushButton("Start", self)
         self.start_button.clicked.connect(self.start_action)
         #self.start_button.clicked.connect(self.start_action)
         # creating pause button
         self.pause_button = QPushButton("Pause", self)
         self.pause_button.clicked.connect(self.pause_action)
         #self.pause_button.clicked.connect(self.pause_action)
         # creating reset button
         self.reset_button = QPushButton("Reset", self)
         self.reset_button.clicked.connect(self.reset_action)
         #self.reset_button.clicked.connect(self.reset_action)
         self.timer_button_layout.addWidget((self.button), 0,0)
         self.timer_button_layout.addWidget((self.start_button), 0,1)
         self.timer_button_layout.addWidget((self.pause_button), 1,0)
         self.timer_button_layout.addWidget((self.reset_button), 1,1)

    def _create_gps_buttons(self):
        #creating latitude input text box
        latitudeButton = QPushButton("Set Latitude", self)
        latitudeButton.clicked.connect(self.getLatitude)
        latitudeButton.setFont(QFont('Times', 11))

        #creating longitude input text box
        longitudeButton = QPushButton("Set Longitude", self)
        longitudeButton.clicked.connect(self.getLongitude)
        longitudeButton.setFont(QFont('Times', 11))

        self.lat_lng_layout.addWidget(latitudeButton)
        self.lat_lng_layout.addWidget(longitudeButton)

    def _create_slider(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(24)
        self.slider.setValue(12)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        # self.slider.setGeometry(700, 600, 200, 50)
        #self.slider.valueChanged.connect(self.sliderValueChanged)
        self.slider.valueChanged.connect(self.sliderValueChanged)
        self.bottom_right_layout.addWidget(self.slider)

    def _create_gps(self):
        # label3 = QLabel("GPS", self)
        # label3.setStyleSheet("border: 3px solid orange")
        # label3.setFont(QFont('Times', 15))
        # label3.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("GPS", self)
        # self.label3.setGeometry(700, 400, 200,200)
        # GPSpixmap = QPixmap('googlemap.png')
        #label3.setPixmap(GPSpixmap)
        self.label3.setStyleSheet("border: 3px solid orange")
        self.label3.setFont(QFont('Times', 15))
        self.label3.setAlignment(Qt.AlignCenter)
        #self.gps_layout.addWidget(self.label3)
        self.gps_layout.addWidget(self.label3)


    def getMapImage(self, lat, lng, zoom):
        urlbase = "http://maps.google.com/maps/api/staticmap?"
        GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
        args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
        args = args + "&key=" + GOOGLEAPIKEY
        mapURL = urlbase+args
        urlretrieve(mapURL, 'googlemap.png')
        img = QPixmap('googlemap.png')
        return img

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

            self.label.setText(str(hrs)+":"+str(mins)+":"+str(second))


    def create_timer(self):
        timer = QTimer(self)
        self.start = False
        timer.timeout.connect(self.showTime)
		# update the timer every tenth second
        timer.start(100)


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


    def _create_modes(self):
        self.stopButton = QPushButton("STOP ROVER", self)

        # stopButton.clicked.connect(self.stop_action)

        # creating auto mode button
        self.autoButton = QPushButton("AUTO MODE", self)

        # autoButton.clicked.connect(self.auto_action)

        # creating manual mode button
        self.manualButton = QPushButton("MANUAL MODE", self)

        # manualButton.clicked.connect(self.manual_action)

        #adding buttons to layout
        self.bottom_left_layout.addWidget(self.stopButton)
        self.bottom_left_layout.addWidget(self.autoButton)
        self.bottom_left_layout.addWidget(self.manualButton)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
