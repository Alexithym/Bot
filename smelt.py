import mouse
import utils
import pyautogui
import numpy as np

from time import sleep
from time import time

smithInterfacePath = "/Users/kunaalsharma/Desktop/bot/Smithing/interface.png"

def runBot():
	smithInterfaceLocation = utils.Location()
	furnaceLocation = utils.getBoundingRectangle()
	start = time()
	iteration = 0

	def clickOnFurnace():
		(x, y, xT, yT) = furnaceLocation
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()
	
	while time() - start < 16 * 3600:
		succ = utils.performAction(clickOnFurnace, 
			utils.makeSuccess(smithInterfaceLocation, smithInterfacePath, False))

		if not succ:
			print(f"Failed to click on furnace, quitting at iteration {iteration}.")
			return

		succ = utils.performAction(utils.makeKeyPressAction('space'), 
			utils.makeSuccess(smithInterfaceLocation, smithInterfacePath, True))

		if not succ:
			print(f"Failed to start smelting, quitting at iteration {iteration}.")
			return

		sleepDuration = -1
		while sleepDuration < 0:
			sleepDuration = np.random.normal(108, 2)
		print(f"Sleeping {sleepDuration} seconds")
		sleep(sleepDuration)

		iteration += 1


if __name__ == "__main__":
	runBot()
	failureCause = pyautogui.screenshot()
	failureCause.save("/Users/kunaalsharma/Desktop/fuck.png")






