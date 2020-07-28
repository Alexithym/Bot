import mouse
import utils
import pyautogui
import numpy as np

from time import sleep
from time import time

bankInterfacePath = "Fletching/Interface/Bank Interface.png"
clayInterfacePath = "Cooking/clayInterface.png"
cookInterfacePath = "Cooking/cookInterface.png"

portableKeyPath = "Cooking/portableKey.png"
portableClickInterfacePath = "Cooking/portableClickInterface.png"
extendInterfacePath = "Cooking/extendInterface.png"

PRESET_KEY = '1'
PORTABLE_PRESET = '2'
SILVERHAWK_KEY = 'q'

def runBot():
	bankLocation = utils.Location()
	clayInterfaceLocation = utils.Location()
	cookInterfaceLocation = utils.Location()

	rangeCoordinates = utils.getBoundingRectangle()
	bankCoordinates = utils.getBoundingRectangle()

	def openBank():
		x, y, xT, yT = bankCoordinates
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()

	def openRange():
		x, y, xT, yT = rangeCoordinates
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()

	startTime = time()

	while True:

		if time() - startTime > 16 * 3600:
			print("Returning after finishing")
			return

		succ = utils.performAction(openBank, 
		utils.makeSuccess(bankLocation, bankInterfacePath, False))
		print("Opened bank...")
		if not succ:
			print("Failed to open bank")
			return

		sleep(1)

		succ = utils.performAction(utils.makeKeyPressAction(PRESET_KEY), 
			utils.makeSuccess(bankLocation, bankInterfacePath, True))
		print("Withdrew food...")
		if not succ:
			print("Failed to withdraw food")
			return

		sleep(1)

		succ = utils.performAction(openRange, 
			utils.makeSuccess(clayInterfaceLocation, clayInterfacePath, False))
		print("Clicked on portable...")
		if not succ:
			print("Failed to click on portable")
			return

		sleep(1)

		succ = utils.performAction(utils.makeKeyPressAction('1'), 
			utils.makeSuccess(cookInterfaceLocation, cookInterfacePath, False))
		print("Selected shaping clay...")
		if not succ:
			print("Failed to select shaping clay")
			return

		succ = utils.performAction(utils.makeKeyPressAction('space'), 
			utils.makeSuccess(cookInterfaceLocation, cookInterfacePath, True))
		print("Started shaping clay...")
		if not succ:
			print("Failed to start shaping clay")
			return

		sleepDuration = -1
		while sleepDuration < 0:
			sleepDuration = np.random.normal(15.7, 0.6)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

		succ = utils.performAction(openRange, 
			utils.makeSuccess(clayInterfaceLocation, clayInterfacePath, False))
		print("Clicked on portable...")
		if not succ:
			print("Failed to click on portable")
			return

		sleep(1)

		succ = utils.performAction(utils.makeKeyPressAction('2'), 
			utils.makeSuccess(cookInterfaceLocation, cookInterfacePath, False))
		print("Selected firing clay...")
		if not succ:
			print("Failed to select shaping clay")
			return

		succ = utils.performAction(utils.makeKeyPressAction('space'), 
			utils.makeSuccess(cookInterfaceLocation, cookInterfacePath, True))
		print("Started firing clay...")
		if not succ:
			print("Failed to start shaping clay")
			return

		sleepDuration = -1
		while sleepDuration < 0:
			sleepDuration = np.random.normal(50, 1.2)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

if __name__ == "__main__":
	runBot()
	failureCause = pyautogui.screenshot()
	failureCause.save("/Users/kunaalsharma/Desktop/fuck.png")






