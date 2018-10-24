from phue import Bridge
import time

bridge = Bridge('10.0.0.28')

lights = bridge.get_light_objects()

def setBrightnessAll(value):
	# Make sure the value is in the acceptable range (0-254)
	if(value > 254):
		print("Max allowed value 254, you provided: " + str(value))
		value = 254
	elif(value < 0):
		print("Min allowed value 0, you provided: " + str(value))
		value = 0

	# Set all lights to that brightness value
	for light in lights:
		light.brightness = value


def setAllOn():
	for light in lights:
		light.on = True
		light.brightness = 0


def setHueAll(value):
	#  Make sure the value is in the acceptable range (0-65535)
	if(value > 65535):
		print("Max allowed value 65535, you provided: " + str(value))
		value = 65535
	elif(value < 0):
		print("Min allowed value 0, you provided: " + str(value))
		value = 0
	
	# Set the hue value
	for light in lights:
		light.hue = value


def setTransitionAll(value):
	# Value in seconds
	for light in lights:
		light.transitiontime = value * 10


def fadeSingleLoop(fullLoopTime, stepSize):
	delay = (fullLoopTime / (65000 / stepSize))
	for i in range(0, 65000, stepSize):
		setHueAll(i)
		time.sleep(delay)
		#print(i)


def alternativeSingleFade(fullLoopTime):
	delay = fullLoopTime / 4
	setTransitionAll(delay)
	setHueAll(0)
	time.sleep(delay)
	setHueAll(16250)
	time.sleep(delay)
	setHueAll(16250*2)
	time.sleep(delay)
	setHueAll(16250*3)
	time.sleep(delay)


def fourOffsetFade(fullLoopTime, stepSize):
	delay = (fullLoopTime / (65000 / stepSize))
	for i in range(0, 65000, stepSize):
		lights[0].hue = i % 65000
		lights[1].hue = (i+16250) % 65000
		lights[2].hue = (i+(16250*2)) % 65000
		lights[3].hue = (i+(16250*3)) % 65000
		#print(i)
		time.sleep(delay)


def twoOffsetFade(fullLoopTime, stepSize):
	delay = (fullLoopTime / (65000 / stepSize))
	for i in range(0, 65000, stepSize):
		lights[0].hue = i % 65000
		lights[1].hue = i % 65000
		lights[2].hue = (i+(16250*2)) % 65000
		lights[3].hue = (i+(16250*2)) % 65000
		#print(i)
		time.sleep(delay)	


def getNames():
	names = []
	for i in range(len(lights)):
		names.append(str(i) + ':' + str(lights[i].name))
	return names

if __name__ == '__main__':
	print('Found lights: ' + str(getNames()))
	setAllOn()
	setBrightnessAll(254)
	while(1):
		#fourOffsetFade(3, 4000)
		#alternativeSingleFade(8)
		fadeSingleLoop(4, 5000)
