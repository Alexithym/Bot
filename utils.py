import pyautogui
import numpy as np
import detectImage
import mouse
from PIL import Image
from time import sleep
from pynput import mouse

'''
Checks on the screen for the mining icon.
'''
def iconPresent(icon):
	loc = pyautogui.locateOnScreen(icon)
	if loc==None:
		return False
	return True

'''
Gets a bounding rectangle
'''
def getBoundingRectangle(n = 2, clean = True):
	points = []

	def cleanPoints(array):
		(x, y) = array[0]
		(xT, yT) = array[1]
		return (int(x), int(y), int(xT), int(yT))

	def on_click(x, y, button, pressed, val = points):
		if not pressed:
			return
		points.append((x,y))
		return False

	for _ in range(n):
		listener = mouse.Listener(on_click = on_click)
		listener.start()
		listener.join()
	
	return cleanPoints(points) if clean else points



'''
Checks the current XP
'''
def checkXP(iconPath):
	x,y = pyautogui.locateCenterOnScreen(iconPath)
	mouse.move(x//4,y//4,10) #error size
	sleepDuration = -1
	while sleepDuration < 0:
		sleepDuration = np.random.normal(1,0.9)
	sleep(sleepDuration)
	mouse.moveCenter()

'''
Spam clicks on a key
'''
def spamPress(key):
	numPresses = np.random.normal(3, 1)
	if numPresses < 2:
		numPresses = 2
	elif numPresses > 4:
		numPresses = 4

	intervals = []
	low, high = 0, np.random.normal(0.3, 0.005)

	for _ in range(round(numPresses)):
		interval = np.random.uniform(low, high)
		intervals.append(interval)
		low = interval

	for interval in intervals:
		pyautogui.press(key)
		sleep(interval)
	return

def checkLocation(loc, target):
	if loc.isEmpty():
		loc.setLoc(pyautogui.locateOnScreen(target))
		return loc.getLoc()
	else:
		return pyautogui.locate(target, pyautogui.screenshot().crop(convert(loc.getLoc())))

def convert(region):
	x1,y1,x2,y2 = region
	return (x1, y1, x2 + x1, y2 + y1)

def performAction(action, success):
	action()
	for _ in range(5):
		if not success():
			sleep(0.2)
		else:
			print("Success")
			return True

	sleep(1)
	for _ in range(10): #reperform action and hope for success
		if not success():
			sleep(1)
			action()
		else:
			print("Success")
			return True
	print("Failure")
	return False

def makeKeyPressAction(key):
	def keyPressAction():
		spamPress(key)

	return keyPressAction

def makeSuccess(loc, target, negative):
	def success():
		present = checkLocation(loc, target)
		return not present if negative else present
	return success

def getDistribution(vals, size = detectImage.BOX_SIZE_SMALL, code = detectImage.IMAGE_FULL, N = 5):
	print("Searching...")
	rawPoints = detectImage.getNLocations(vals, size = size, code = code, N = N)
	cleanPoints = []

	for x, y in rawPoints:
		cleanPoints.append((x//4, y//4))

	def drawFromLocs():
		index = np.random.exponential(N/10)
		while index >= N:
			index = np.random.expoential(N/10)
		return cleanPoints[int(index)]

	return drawFromLocs

class Location:

	def __init__(self):
		self.loc = None

	def getLoc(self):
		return self.loc

	def setLoc(self, loc):
		self.loc = loc

	def isEmpty(self):
		return self.loc == None





