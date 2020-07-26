import utils
import pyautogui

import numpy as np
import mouse

from random import randint
from time import sleep
from time import time

divInterfacePath = "/Users/kunaalsharma/Desktop/bot/Fletching/Interface/Fletch Interface.png"
portablePath = "/Users/kunaalsharma/Desktop/bot/Fletching/portable.png"
optionPath = "/Users/kunaalsharma/Desktop/bot/Fletching/deploy.png"
promptPath = "/Users/kunaalsharma/Desktop/bot/Fletching/prompt.png"

ENERGY_KEY = '5'

def performAction(action, success):
	action()
	sleep(1)
	if success():
		print("Success")
		return True

	for _ in range(10): #reperform action and hope for success
		if not success():
			action()
			sleep(1)
		else:
			print("Success")
			return True
	print("Failure")
	return False


def makeKeyPressAction(key):
	def keyPressAction():
		utils.spamPress(key)

	return keyPressAction

def makeSuccess(loc, target, negative):
	def success():
		present = utils.checkLocation(loc, target)
		print(f"{present} at {loc.getLoc()}")
		return not present if negative else present
	return success

def portable(portableLoc, promptLoc):
	def foo():
		x1, y1, x2, y2 = utils.convert(portableLoc.getLoc())
		mouse.move(x1//4, y1//4, min((x2-x1)//4, (y2-y1)//4), teleportRandom=True)
		pyautogui.click(button="right")
		sleep(1)

		loc = pyautogui.locateOnScreen(optionPath)
		x1, y1, x2, y1 = utils.convert(loc)
		mouse.move(x1//4, y1//4, min((x2-x1)//4, (y2-y1)//4), teleportRandom=False)
		sleep(0.2)
		pyautogui.click()

	succ = performAction(foo, makeSuccess(promptLoc, promptPath, False))
	if not succ:
		print("Failed to open prompt")
		return False

	def vac():
		return True

	numToDeploy = randint(100, 1000)
	for ch in list(str(numToDeploy)):
		performAction(makeKeyPressAction(ch), vac)
		sleep(0.5)

	succ = performAction(makeKeyPressAction('enter'), makeSuccess(promptLoc, promptPath, True))
	if not succ:
		print("Failed to deploy portable")
		return False

	return True


def runBot():
	sleep(2)
	count = 0
	divLoc = utils.Location()
	portableLoc = utils.Location()
	portableLoc.setLoc(pyautogui.locateOnScreen(portablePath))
	promptLoc = utils.Location()
	start = time()
	lastAdditionTime = 0
	while True:
		succ = performAction(makeKeyPressAction(ENERGY_KEY), makeSuccess(divLoc, divInterfacePath, False))
		if not succ:
			print(f"Failed on iteration {count}")
			return
		sleep(1)
		succ = performAction(makeKeyPressAction('space'), makeSuccess(divLoc, divInterfacePath, True))
		if not succ:
			print(f"Failed on iteration {count}")
			return
		count += 1
		sleepDuration = -1
		while sleepDuration < 0:
			sleepDuration = np.random.normal(13, 1)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

		if randint(0, 100) == 10:
			sleepDuration = np.random.normal(100, 20)
			print(f"Random long sleep: {sleepDuration} seconds")
			sleep(sleepDuration)
		'''
		if time() + randint(600, 1200) - lastAdditionTime > 3600:
			print("Attempting to deploy portables")
			lastAdditionTime = time()
			succ = portable(portableLoc, promptLoc)
			if not succ:
				lastAdditionTime = 100000000000000000000000000000000000000000
			else:
				print(f"Deployed portables on iteration {count}")
		'''
		if time() - start > 3600 * 16:
			print("Finished running, quitting after 16 hours.")
			return 

if __name__ == "__main__":
	runBot()