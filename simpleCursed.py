import utils
import pyautogui
import detectImage
import mouse

import numpy as np

from time import sleep


divInterfacePath = "/Users/kunaalsharma/Desktop/bot/Divination/incandescent.png"
bankInterfacePath = "/Users/kunaalsharma/Desktop/bot/Fletching/Interface/Bank Interface.png"
extremeInterfacePath = "/Users/kunaalsharma/Desktop/bot/Divination/extreme.png"

size = detectImage.BOX_SIZE_SMALL
code = detectImage.IMAGE_FULL
PRESET_KEY = '2'


POT_KEY = 't'
ENERGY_KEY = 'y'

chestLocs = []

def findBank():
	global chestLocs
	print("Searching for bank")
	rawPoints = detectImage.getNLocations("Fletching/Bank Images/vals.txt", size, code, N = 5)
	cleanPoints = []

	for x, y in rawPoints:
		cleanPoints.append((x//4, y//4))

	chestLocs = cleanPoints
	print("Found bank")
	return

def openBankAction():
	ind = float('inf')
	while ind >= len(chestLocs):
		ind = np.random.geometric(0.2)
	x , y = chestLocs[ind]

	mouse.move(x, y, 50, teleportRandom = True)
	pyautogui.click()

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
		return not present if negative else present
	return success

def runBot():
	sleep(2)
	findBank()
	count = 0
	divLoc = utils.Location()
	extremeLoc = utils.Location()
	bankLoc = utils.Location()
	while True:
		if count % 2 == 0:
			print("Opening bank")
			succ = performAction(openBankAction, makeSuccess(bankLoc, bankInterfacePath, False)) 
			if not succ:
				print(f"Failed on iteration {count}")
				return
			sleep(1)

			print("Withdrawing energy")
			succ = performAction(makeKeyPressAction(PRESET_KEY), makeSuccess(bankLoc, bankInterfacePath, True))
			if not succ:
				print(f"Failed on iteration {count}")
				return
			sleep(1)

			print("Drinking potion")
			succ = performAction(makeKeyPressAction(POT_KEY), makeSuccess(extremeLoc, extremeInterfacePath, True))
			if not succ:
				print(f"Failed on iteration {count}")
				return
		sleep(1)
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
			sleepDuration = np.random.normal(144, 5)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

if __name__ == "__main__":
	runBot()