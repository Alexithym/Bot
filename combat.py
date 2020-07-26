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

def avoidTimeout():
	directions = ['left', 'right', 'up', 'down']
	direction = directions[int(np.random.normal(100, 20) % 4)]
	utils.spamPress(direction)


def extend(silverhawkCoordinates, overloadCoordinates, aggressionCoordinates):
	x, y, xT, yT = silverhawkCoordinates
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	sleep(getSleep(2, 0.3))

	x, y, xT, yT = overloadCoordinates
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	sleep(getSleep(2, 0.3))

	x, y, xT, yT = aggressionCoordinates
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	sleep(getSleep(2, 0.3))

	return True

def runBot():
	sleep(1)
	silverhawkCoordinates = utils.getBoundingRectangle()
	overloadCoordinates = utils.getBoundingRectangle()
	aggressionCoordinates = utils.getBoundingRectangle()

	currentTime = time()

	while True:
		if not extend(silverhawkCoordinates, overloadCoordinates, aggressionCoordinates):
			print("Failed")
			return
		sleepDuration = getSleep(5 * 60, 5)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration / 2)
		avoidTimeout()
		sleep(sleepDuration / 2)

if __name__ == "__main__":
	runBot()
	failureCause = pyautogui.screenshot()
	failureCause.save("/Users/kunaalsharma/Desktop/fuck.png")






