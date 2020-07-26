import mouse
import utils
import pyautogui
import numpy as np

from time import sleep
from time import time

silverhawkPath = "/Users/kunaalsharma/Desktop/bot/Combat/silverhawk.png"
overloadPath = "/Users/kunaalsharma/Desktop/bot/Combat/ovl.png"

def getSleep(mean, variance):
	sleepDuration = -1;
	while sleepDuration < 0:
		sleepDuration = np.random.normal(mean, variance)
	return sleepDuration

def extend(silverhawkCoordinates, overloadCoordinates, aggressionCoordinates):
	x, y, xT, yT = silverhawkCoordinates
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	sleep(getSleep(1, 0.3))

	x, y, xT, yT = overloadCoordinates
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	sleep(getSleep(1, 0.3))

	x, y, xT, yT = aggressionCoordinates
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	sleep(getSleep(1, 0.3))

	for _ in range(10):
		ovlLoc = utils.Location()
		if utils.checkLocation(ovlLoc, overloadPath):
			return True

	return False

def runBot():
	silverhawkCoordinates = utils.convert(pyautogui.locateOnScreen(silverhawkPath))
	overloadCoordinates = utils.getBoundingRectangle()
	aggressionCoordinates = utils.getBoundingRectangle()
	print(silverhawkCoordinates)

	currentTime = time()

	while True:
		if not extend(silverhawkCoordinates, overloadCoordinates, aggressionCoordinates):
			print("Failed")
			return
		sleepDuration = getSleep(5 * 60, 5)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

if __name__ == "__main__":
	runBot()
	failureCause = pyautogui.screenshot()
	failureCause.save("/Users/kunaalsharma/Desktop/fuck.png")






