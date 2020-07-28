import mouse
import utils
import pyautogui
import numpy as np

from time import sleep
from time import time

bankInterfacePath = "/Users/kunaalsharma/Desktop/bot/Fletching/Interface/Bank Interface.png"
clayInterfacePath = "/Users/kunaalsharma/Desktop/bot/Cooking/clayInterface.png"
cookInterfacePath = "/Users/kunaalsharma/Desktop/bot/Cooking/cookInterface.png"

portableKeyPath = "/Users/kunaalsharma/Desktop/bot/Cooking/portableKey.png"
portableClickInterfacePath = "/Users/kunaalsharma/Desktop/bot/Cooking/portableClickInterface.png"
extendInterfacePath = "/Users/kunaalsharma/Desktop/bot/Cooking/extendInterface.png"

PRESET_KEY = '1'
PORTABLE_PRESET = '2'
SILVERHAWK_KEY = 'q'

def extendPortable(portableKeyCoordinates, extendInterfaceLocation, tries = 0):
	(x, y, xT, yT) = portableKeyCoordinates
	(x, y, xT, yT) = (5 + x//2, 5 + y//2, -5 + xT//2, -5 + yT//2)

	if tries == 10:
		print("Failed to extend portable")
		return False
	
	def moveToPortableKey():
		mouse.moveRect(x, y, xT, yT)

		sleepDuration = -1
		while sleepDuration < 0:
			sleepDuration = np.random.normal(0.2, 0.01)
		sleep(sleepDuration)

		pyautogui.click(button='right')

	portableClickLocation = utils.Location()

	succ = utils.performAction(moveToPortableKey, 
		utils.makeSuccess(portableClickLocation, portableClickInterfacePath, False))
	if not succ:
		print("Failed to right click portable key, retrying")
		extendPortable(portableKeyCoordinates, extendInterfaceLocation, tries = tries + 1)
		

	sleep(3)

	(x, y, xT, yT) = utils.convert(portableClickLocation.getLoc())
	(x, y, xT, yT) = (x//2, y//2, xT//2, yT//2)
	mouse.moveRect(x, y, xT, yT, teleportRandom=False)
	pyautogui.click()
	
	sleep(3)

	if not utils.checkLocation(extendInterfaceLocation, extendInterfacePath):
		print("Failed to open extend interface, retrying")
		extendPortable(portableKeyCoordinates, extendInterfaceLocation, tries = tries + 1)

	sleepDuration = -1
	while sleepDuration < 0:
		sleepDuration = np.random.normal(0.2, 0.2)
	utils.spamPress('1')
	sleep(sleepDuration)
	utils.spamPress('enter')

	sleep(3)

	if utils.checkLocation(extendInterfaceLocation, extendInterfacePath):
		print("Failed to extend portable, retrying")
		extendPortable(portableKeyCoordinates, extendInterfaceLocation, tries = tries + 1)

	return True

def runBot():
	extendInterfaceLocation = utils.Location()
	bankLocation = utils.Location()
	clayInterfaceLocation = utils.Location()
	cookInterfaceLocation = utils.Location()
	silverhawkLocation = utils.Location()
	portableKeyCoordinates = None

	sleep(2)
	portableKeyCoordinates = utils.convert(pyautogui.locateOnScreen(portableKeyPath))
	print(portableKeyCoordinates)

	rangeCoordinates = utils.getBoundingRectangle()
	bankCoordinates = utils.getBoundingRectangle()
	silverhawkCoordinates = utils.getBoundingRectangle()

	def openBank():
		x, y, xT, yT = bankCoordinates
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()

	def openRange():
		x, y, xT, yT = rangeCoordinates
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()

	def extendSilverhawk():
		x, y, xT, yT = silverhawkCoordinates
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()

	succ = extendPortable(portableKeyCoordinates, extendInterfaceLocation)
	if not succ:
		return 
	sleep(2)
	utils.performAction(extendSilverhawk, lambda : True)
	sleep(2)

	portableTimer = time()
	startTime = time()

	while True:

		if time() - portableTimer > 50 * 60:
			succ = utils.performAction(openBank, 
			utils.makeSuccess(bankLocation, bankInterfacePath, False))
			if not succ:
				print("Failed to open bank")
				return False

			sleep(3)

			succ = utils.performAction(utils.makeKeyPressAction(PORTABLE_PRESET), 
				utils.makeSuccess(bankLocation, bankInterfacePath, True))
			if not succ:
				print("Failed to withdraw preset")
				return False

			succ = extendPortable(portableKeyCoordinates, extendInterfaceLocation)
			if not succ:
				return
			sleep(2)
			utils.performAction(extendSilverhawk, lambda : True)
			sleep(2)

			portableTimer = time() - 30

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
			sleepDuration = np.random.normal(15.5, 0.6)
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






