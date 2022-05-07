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
        Form.setStyleSheet("\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-color: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/dark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: silver;\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon    : url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon    : url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon    : url(:/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-color: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/dark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: silver;\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon    : url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon    : url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon    : url(:/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("background-color:rgb(38,61,95);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 190, 281, 621))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.v1_3 = QtWidgets.QLabel(self.tab)
        self.v1_3.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_3.setFont(font)
        self.v1_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_3.setObjectName("v1_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.v1_4 = QtWidgets.QLabel(self.tab)
        self.v1_4.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_4.setFont(font)
        self.v1_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_4.setObjectName("v1_4")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_3.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.v1_5 = QtWidgets.QLabel(self.tab)
        self.v1_5.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_5.setFont(font)
        self.v1_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_5.setObjectName("v1_5")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_4.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.v1_6 = QtWidgets.QLabel(self.tab)
        self.v1_6.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_6.setFont(font)
        self.v1_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_6.setObjectName("v1_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_5.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_6.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.v1_7 = QtWidgets.QLabel(self.tab_2)
        self.v1_7.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_7.setFont(font)
        self.v1_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_7.setObjectName("v1_7")
        self.v1_8 = QtWidgets.QLabel(self.tab_2)
        self.v1_8.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_8.setFont(font)
        self.v1_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_8.setObjectName("v1_8")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_7.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_8.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.v1_9 = QtWidgets.QLabel(self.tab_2)
        self.v1_9.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_9.setFont(font)
        self.v1_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_9.setObjectName("v1_9")
        self.v1_10 = QtWidgets.QLabel(self.tab_2)
        self.v1_10.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_10.setFont(font)
        self.v1_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_10.setObjectName("v1_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.Sensor3 = QtWidgets.QWidget()
        self.Sensor3.setObjectName("Sensor3")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.Sensor3)
        self.lcdNumber_9.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.Sensor3)
        self.lcdNumber_10.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.v1_11 = QtWidgets.QLabel(self.Sensor3)
        self.v1_11.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_11.setFont(font)
        self.v1_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_11.setObjectName("v1_11")
        self.v1_12 = QtWidgets.QLabel(self.Sensor3)
        self.v1_12.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_12.setFont(font)
        self.v1_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_12.setObjectName("v1_12")
        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.Sensor3)
        self.lcdNumber_11.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.Sensor3)
        self.lcdNumber_12.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.v1_13 = QtWidgets.QLabel(self.Sensor3)
        self.v1_13.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_13.setFont(font)
        self.v1_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_13.setObjectName("v1_13")
        self.v1_14 = QtWidgets.QLabel(self.Sensor3)
        self.v1_14.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_14.setFont(font)
        self.v1_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_14.setObjectName("v1_14")
        self.tabWidget.addTab(self.Sensor3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber_13.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.lcdNumber_14 = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber_14.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.v1_15 = QtWidgets.QLabel(self.tab_4)
        self.v1_15.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_15.setFont(font)
        self.v1_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_15.setObjectName("v1_15")
        self.v1_16 = QtWidgets.QLabel(self.tab_4)
        self.v1_16.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_16.setFont(font)
        self.v1_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_16.setObjectName("v1_16")
        self.lcdNumber_15 = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber_15.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.lcdNumber_16 = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber_16.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_16.setObjectName("lcdNumber_16")
        self.v1_17 = QtWidgets.QLabel(self.tab_4)
        self.v1_17.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_17.setFont(font)
        self.v1_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_17.setObjectName("v1_17")
        self.v1_18 = QtWidgets.QLabel(self.tab_4)
        self.v1_18.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_18.setFont(font)
        self.v1_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_18.setObjectName("v1_18")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lcdNumber_17 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_17.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_17.setObjectName("lcdNumber_17")
        self.lcdNumber_18 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_18.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_18.setObjectName("lcdNumber_18")
        self.v1_19 = QtWidgets.QLabel(self.tab_5)
        self.v1_19.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_19.setFont(font)
        self.v1_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_19.setObjectName("v1_19")
        self.v1_20 = QtWidgets.QLabel(self.tab_5)
        self.v1_20.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_20.setFont(font)
        self.v1_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_20.setObjectName("v1_20")
        self.lcdNumber_19 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_19.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_19.setObjectName("lcdNumber_19")
        self.lcdNumber_20 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_20.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_20.setObjectName("lcdNumber_20")
        self.v1_21 = QtWidgets.QLabel(self.tab_5)
        self.v1_21.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_21.setFont(font)
        self.v1_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_21.setObjectName("v1_21")
        self.v1_22 = QtWidgets.QLabel(self.tab_5)
        self.v1_22.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_22.setFont(font)
        self.v1_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_22.setObjectName("v1_22")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.lcdNumber_21 = QtWidgets.QLCDNumber(self.tab_6)
        self.lcdNumber_21.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_21.setObjectName("lcdNumber_21")
        self.lcdNumber_22 = QtWidgets.QLCDNumber(self.tab_6)
        self.lcdNumber_22.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_22.setObjectName("lcdNumber_22")
        self.v1_23 = QtWidgets.QLabel(self.tab_6)
        self.v1_23.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_23.setFont(font)
        self.v1_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_23.setObjectName("v1_23")
        self.v1_24 = QtWidgets.QLabel(self.tab_6)
        self.v1_24.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_24.setFont(font)
        self.v1_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_24.setObjectName("v1_24")
        self.lcdNumber_23 = QtWidgets.QLCDNumber(self.tab_6)
        self.lcdNumber_23.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_23.setObjectName("lcdNumber_23")
        self.lcdNumber_24 = QtWidgets.QLCDNumber(self.tab_6)
        self.lcdNumber_24.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_24.setObjectName("lcdNumber_24")
        self.v1_25 = QtWidgets.QLabel(self.tab_6)
        self.v1_25.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_25.setFont(font)
        self.v1_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_25.setObjectName("v1_25")
        self.v1_26 = QtWidgets.QLabel(self.tab_6)
        self.v1_26.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_26.setFont(font)
        self.v1_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_26.setObjectName("v1_26")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.lcdNumber_25 = QtWidgets.QLCDNumber(self.tab_7)
        self.lcdNumber_25.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_25.setObjectName("lcdNumber_25")
        self.lcdNumber_26 = QtWidgets.QLCDNumber(self.tab_7)
        self.lcdNumber_26.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_26.setObjectName("lcdNumber_26")
        self.v1_27 = QtWidgets.QLabel(self.tab_7)
        self.v1_27.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_27.setFont(font)
        self.v1_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_27.setObjectName("v1_27")
        self.v1_28 = QtWidgets.QLabel(self.tab_7)
        self.v1_28.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_28.setFont(font)
        self.v1_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_28.setObjectName("v1_28")
        self.lcdNumber_27 = QtWidgets.QLCDNumber(self.tab_7)
        self.lcdNumber_27.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_27.setObjectName("lcdNumber_27")
        self.lcdNumber_28 = QtWidgets.QLCDNumber(self.tab_7)
        self.lcdNumber_28.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_28.setObjectName("lcdNumber_28")
        self.v1_29 = QtWidgets.QLabel(self.tab_7)
        self.v1_29.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_29.setFont(font)
        self.v1_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_29.setObjectName("v1_29")
        self.v1_30 = QtWidgets.QLabel(self.tab_7)
        self.v1_30.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_30.setFont(font)
        self.v1_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_30.setObjectName("v1_30")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.lcdNumber_29 = QtWidgets.QLCDNumber(self.tab_8)
        self.lcdNumber_29.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_29.setObjectName("lcdNumber_29")
        self.lcdNumber_30 = QtWidgets.QLCDNumber(self.tab_8)
        self.lcdNumber_30.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_30.setObjectName("lcdNumber_30")
        self.v1_31 = QtWidgets.QLabel(self.tab_8)
        self.v1_31.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_31.setFont(font)
        self.v1_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_31.setObjectName("v1_31")
        self.v1_32 = QtWidgets.QLabel(self.tab_8)
        self.v1_32.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_32.setFont(font)
        self.v1_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_32.setObjectName("v1_32")
        self.lcdNumber_31 = QtWidgets.QLCDNumber(self.tab_8)
        self.lcdNumber_31.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_31.setObjectName("lcdNumber_31")
        self.lcdNumber_32 = QtWidgets.QLCDNumber(self.tab_8)
        self.lcdNumber_32.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_32.setObjectName("lcdNumber_32")
        self.v1_33 = QtWidgets.QLabel(self.tab_8)
        self.v1_33.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_33.setFont(font)
        self.v1_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_33.setObjectName("v1_33")
        self.v1_34 = QtWidgets.QLabel(self.tab_8)
        self.v1_34.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_34.setFont(font)
        self.v1_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_34.setObjectName("v1_34")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.lcdNumber_33 = QtWidgets.QLCDNumber(self.tab_9)
        self.lcdNumber_33.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_33.setObjectName("lcdNumber_33")
        self.lcdNumber_34 = QtWidgets.QLCDNumber(self.tab_9)
        self.lcdNumber_34.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_34.setObjectName("lcdNumber_34")
        self.v1_35 = QtWidgets.QLabel(self.tab_9)
        self.v1_35.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_35.setFont(font)
        self.v1_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_35.setObjectName("v1_35")
        self.v1_36 = QtWidgets.QLabel(self.tab_9)
        self.v1_36.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_36.setFont(font)
        self.v1_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_36.setObjectName("v1_36")
        self.lcdNumber_35 = QtWidgets.QLCDNumber(self.tab_9)
        self.lcdNumber_35.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_35.setObjectName("lcdNumber_35")
        self.lcdNumber_36 = QtWidgets.QLCDNumber(self.tab_9)
        self.lcdNumber_36.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_36.setObjectName("lcdNumber_36")
        self.v1_37 = QtWidgets.QLabel(self.tab_9)
        self.v1_37.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_37.setFont(font)
        self.v1_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_37.setObjectName("v1_37")
        self.v1_38 = QtWidgets.QLabel(self.tab_9)
        self.v1_38.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_38.setFont(font)
        self.v1_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_38.setObjectName("v1_38")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.lcdNumber_37 = QtWidgets.QLCDNumber(self.tab_10)
        self.lcdNumber_37.setGeometry(QtCore.QRect(0, 310, 241, 71))
        self.lcdNumber_37.setObjectName("lcdNumber_37")
        self.lcdNumber_38 = QtWidgets.QLCDNumber(self.tab_10)
        self.lcdNumber_38.setGeometry(QtCore.QRect(0, 50, 241, 71))
        self.lcdNumber_38.setObjectName("lcdNumber_38")
        self.v1_39 = QtWidgets.QLabel(self.tab_10)
        self.v1_39.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_39.setFont(font)
        self.v1_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_39.setObjectName("v1_39")
        self.v1_40 = QtWidgets.QLabel(self.tab_10)
        self.v1_40.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_40.setFont(font)
        self.v1_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_40.setObjectName("v1_40")
        self.lcdNumber_39 = QtWidgets.QLCDNumber(self.tab_10)
        self.lcdNumber_39.setGeometry(QtCore.QRect(0, 180, 241, 71))
        self.lcdNumber_39.setObjectName("lcdNumber_39")
        self.lcdNumber_40 = QtWidgets.QLCDNumber(self.tab_10)
        self.lcdNumber_40.setGeometry(QtCore.QRect(0, 430, 241, 71))
        self.lcdNumber_40.setObjectName("lcdNumber_40")
        self.v1_41 = QtWidgets.QLabel(self.tab_10)
        self.v1_41.setGeometry(QtCore.QRect(0, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_41.setFont(font)
        self.v1_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_41.setObjectName("v1_41")
        self.v1_42 = QtWidgets.QLabel(self.tab_10)
        self.v1_42.setGeometry(QtCore.QRect(0, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_42.setFont(font)
        self.v1_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.v1_42.setObjectName("v1_42")
        self.tabWidget.addTab(self.tab_10, "")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 281, 131))
        self.groupBox.setObjectName("groupBox")
        self.btnConnect = QtWidgets.QPushButton(self.groupBox)
        self.btnConnect.setGeometry(QtCore.QRect(180, 80, 93, 28))
        self.btnConnect.setObjectName("btnConnect")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label.setObjectName("label")
        self.v1_2 = QtWidgets.QLabel(self.frame)
        self.v1_2.setGeometry(QtCore.QRect(80, 140, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.v1_2.setFont(font)
        self.v1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.v1_2.setObjectName("v1_2")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("background-color:rgb(38,61,95);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("MT 6.0 SENSOR BOX")
        self.v1_3.setText(_translate("Form", "Min Value :"))
        self.v1_4.setText(_translate("Form", "Max Value :"))
        self.v1_5.setText(_translate("Form", "Avg Value :"))
        self.v1_6.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Sensor 1"))
        self.v1_7.setText(_translate("Form", "Min Value :"))
        self.v1_8.setText(_translate("Form", "Avg Value :"))
        self.v1_9.setText(_translate("Form", "Max Value :"))
        self.v1_10.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Sensor 2"))
        self.v1_11.setText(_translate("Form", "Min Value :"))
        self.v1_12.setText(_translate("Form", "Avg Value :"))
        self.v1_13.setText(_translate("Form", "Max Value :"))
        self.v1_14.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sensor3), _translate("Form", "Sensor 3"))
        self.v1_15.setText(_translate("Form", "Min Value :"))
        self.v1_16.setText(_translate("Form", "Avg Value :"))
        self.v1_17.setText(_translate("Form", "Max Value :"))
        self.v1_18.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Sensor 4"))
        self.v1_19.setText(_translate("Form", "Min Value :"))
        self.v1_20.setText(_translate("Form", "Avg Value :"))
        self.v1_21.setText(_translate("Form", "Max Value :"))
        self.v1_22.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Sensor 5"))
        self.v1_23.setText(_translate("Form", "Min Value :"))
        self.v1_24.setText(_translate("Form", "Avg Value :"))
        self.v1_25.setText(_translate("Form", "Max Value :"))
        self.v1_26.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Sensor 6"))
        self.v1_27.setText(_translate("Form", "Min Value :"))
        self.v1_28.setText(_translate("Form", "Avg Value :"))
        self.v1_29.setText(_translate("Form", "Max Value :"))
        self.v1_30.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Sensor 7"))
        self.v1_31.setText(_translate("Form", "Min Value :"))
        self.v1_32.setText(_translate("Form", "Avg Value :"))
        self.v1_33.setText(_translate("Form", "Max Value :"))
        self.v1_34.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Form", "Sensor 8"))
        self.v1_35.setText(_translate("Form", "Min Value :"))
        self.v1_36.setText(_translate("Form", "Avg Value :"))
        self.v1_37.setText(_translate("Form", "Max Value :"))
        self.v1_38.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Form", "Sensor 9"))
        self.v1_39.setText(_translate("Form", "Min Value :"))
        self.v1_40.setText(_translate("Form", "Avg Value :"))
        self.v1_41.setText(_translate("Form", "Max Value :"))
        self.v1_42.setText(_translate("Form", "Standard Value :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Form", "Sensor 10"))
        self.groupBox.setTitle(_translate("Form", "Connection Panel"))
        self.btnConnect.setText(_translate("Form", "Connect"))
        self.comboBox.setItemText(0, _translate("Form", "COM3"))
        self.comboBox.setItemText(1, _translate("Form", "COM4"))
        self.comboBox.setItemText(2, _translate("Form", "COM5"))
        self.comboBox.setItemText(3, _translate("Form", "COM6"))
        self.comboBox.setItemText(4, _translate("Form", "COM7"))
        self.comboBox.setItemText(5, _translate("Form", "COM8"))
        self.comboBox.setItemText(6, _translate("Form", "COM9"))
        self.comboBox.setItemText(7, _translate("Form", "COM10"))
        self.comboBox.setItemText(8, _translate("Form", "COM11"))
        self.comboBox.setItemText(9, _translate("Form", "COM12"))
        self.label.setText(_translate("Form", "Com Port :"))
        self.v1_2.setText(_translate("Form", "Sensor Value"))
        global i
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data, i)
        self.timer.start()

    def update_plot_data(self):
        global i
        #getData=ser.readline()
        #data=int(getData)
        data = random.randint(0,20)
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

