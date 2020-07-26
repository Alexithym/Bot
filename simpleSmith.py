import utils
import pyautogui
import detectImage
import mouse

import numpy as np

from time import sleep
 # 238.177m -> 255.657

interfacePath = "/Users/kunaalsharma/Desktop/bot/Smithing/interface.png"

def runBot():
	sleep(2)

	capeLoc = utils.Location()
	interfaceLoc = utils.Location()
	capeLoc.setLoc(pyautogui.locateOnScreen(capePath))
	print(f"Found cape loc at {capeLoc.getLoc()}")
	while True:

		def foo():
			x, y, _, _ = utils.convert(capeLoc.getLoc())
			mouse.move(x//4, y//4, 50, teleportRandom = True)
			pyautogui.click()

		succ = utils.performAction(foo, utils.makeSuccess(interfaceLoc, interfacePath, False))
		if not succ:
			print("Failed")
			return	
		print("Clicked on smelter")

		sleep(1)

		succ = utils.performAction(utils.makeKeyPressAction('space'), utils.makeSuccess(interfaceLoc, interfacePath, True))
		if not succ:
			print("Failed")
			return	
		print("Started smelting")

		sleepDuration = -1
		while sleepDuration < 0:
			sleepDuration = np.random.normal(105, 10)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

if __name__ == "__main__":
	runBot()