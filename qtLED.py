import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QSlider, QPushButton, QGridLayout, QSizePolicy, QLabel
from PyQt5.QtCore import Qt
import logging, logging.handlers

# Setup the Main logging
logger = logging.getLogger('mainLog')
logger.setLevel(logging.DEBUG)
sformatter = logging.Formatter('%(asctime)-23s - %(name)-9s - [%(levelname)-8s] - %(message)s')
eformatter = logging.Formatter('%(asctime)-23s - %(filename)-20s - %(lineno)-4s - [%(levelname)-8s] - %(message)s')
fh1 = logging.handlers.RotatingFileHandler('log.log', maxBytes=(10*1024*1024), backupCount=10)
fh1.setLevel(logging.DEBUG)
err = logging.handlers.RotatingFileHandler('errorlog.log', maxBytes=(5*1024*1024), backupCount=10)
err.setLevel(logging.WARNING)
sh1 = logging.StreamHandler()
sh1.setLevel(logging.DEBUG)
fh1.setFormatter(sformatter)
err.setFormatter(eformatter)
sh1.setFormatter(sformatter)
logger.addHandler(fh1)
logger.addHandler(sh1)
logger.addHandler(err)


### Base GUI 
class baseGUI(QWidget):
	def __init__(self):
		super().__init__() # Initialize the QWidget object
		
		# Variables to hold the states of the LEDs
		self.led1state = False
		self.led2state = False
		self.led3state = False
		
		# setup the GUI
		self.initUI()
		
	# Setup the GUI
	def initUI(self):	
		# Set layout
		self.grid = QGridLayout()
		self.setLayout(self.grid)
	
		### Set window properties
		self.setGeometry(300, 300, 800, 480)		
		self.setWindowTitle('TP-Link Bulb Control')	
		
		### LED Controls
		## On and Off
		# On button
		self.onBtn = QPushButton('On', self)
		self.onBtn.setMinimumSize(0, 75)
		self.onBtn.resize(self.onBtn.sizeHint())
		self.onBtn.clicked.connect(self.allOn)
		self.onBtn.setStyleSheet('background-color:#84c17f')
		self.grid.addWidget(self.onBtn, 0, 0, 1, 3)
		
		# Off button
		self.offBtn = QPushButton('Off', self)
		self.offBtn.setMinimumSize(0, 75)
		self.offBtn.resize(self.offBtn.sizeHint())
		self.offBtn.clicked.connect(self.allOff)
		self.offBtn.setStyleSheet('background-color:#e28888')
		self.grid.addWidget(self.offBtn, 0, 3, 1, 3)
		
		
		## Individual LED on/off
		# LED 1 
		self.led1Btn = QPushButton('LED 1', self)
		self.led1Btn.setMinimumSize(0, 75)
		self.led1Btn.resize(self.led1Btn.sizeHint())
		self.led1Btn.clicked.connect(self.led1toggle)
		self.led1Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
		self.grid.addWidget(self.led1Btn, 1, 0, 1, 2)
		
		# LED 2
		self.led2Btn = QPushButton('LED 2', self)
		self.led2Btn.setMinimumSize(0, 75)
		self.led2Btn.resize(self.led2Btn.sizeHint())
		self.led2Btn.clicked.connect(self.led2toggle)
		self.led2Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
		self.grid.addWidget(self.led2Btn, 1, 2, 1, 2)
		
		# LED 3
		self.led3Btn = QPushButton('LED 3', self)
		self.led3Btn.setMinimumSize(0, 75)
		self.led3Btn.resize(self.led3Btn.sizeHint())
		self.led3Btn.clicked.connect(self.led3toggle)
		self.led3Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
		self.grid.addWidget(self.led3Btn, 1, 4, 1, 2)
		
		
		## Scenes
		#
		self.a = QLabel('')
		self.b = QLabel('')
		self.c = QLabel('')
		self.d = QLabel('')
		self.grid.addWidget(self.a, 2, 0, 1, 6)
		self.grid.addWidget(self.b, 3, 0, 1, 6)
		self.grid.addWidget(self.c, 4, 0, 1, 6)
		self.grid.addWidget(self.d, 5, 0, 1, 6)
		
		## Brightness
		# Slider for brightness
		self.slider = QSlider(Qt.Horizontal, self)
		self.slider.setFocusPolicy(Qt.NoFocus)
		self.slider.setGeometry(10, 0, 780, 30)
		self.slider.valueChanged[int].connect(self.changeValue)
		self.grid.addWidget(self.slider, 6, 0, 1, 6)
		
		self.show()
		
	# When the slider value is changed
	def changeValue(self, value):
		logger.debug('New slider value ' + str(value))
		
	# When the on button is pressed
	def allOn(self):
		logger.debug('All on')
		self.led1Btn.setStyleSheet('background-color: rgb(159, 177, 206, 255)')
		self.led2Btn.setStyleSheet('background-color: rgb(159, 177, 206, 255)')
		self.led3Btn.setStyleSheet('background-color: rgb(159, 177, 206, 255)')
	
	# When the off button is pressed
	def allOff(self):
		logger.debug('All off')
		self.led1Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
		self.led2Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
		self.led3Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
	
	# Toggle LED 1
	def led1toggle(self):
		self.led1state = not self.led1state
		logger.info('LED 1 ' + str(self.led1state))
		if(self.led1state):
			self.led1Btn.setStyleSheet('background-color: rgb(159, 177, 206, 255)')
		else:
			self.led1Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
			
	# Toggle LED 2
	def led2toggle(self):
		self.led2state = not self.led2state
		logger.info('LED 2 ' + str(self.led2state))
		if(self.led2state):
			self.led2Btn.setStyleSheet('background-color: rgb(159, 177, 206, 255)')
		else:
			self.led2Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
	
	# Toggle LED 3
	def led3toggle(self):
		self.led3state = not self.led3state
		logger.info('LED 3 ' + str(self.led3state))
		if(self.led3state):
			self.led3Btn.setStyleSheet('background-color: rgb(159, 177, 206, 255)')
		else:
			self.led3Btn.setStyleSheet('background-color: rgb(159, 177, 206, 100)')
		
		
	# Before exiting make sure user wants to
	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message',
			"Are you sure to quit?", QMessageBox.Yes | 
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
			

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = baseGUI()
	sys.exit(app.exec_())