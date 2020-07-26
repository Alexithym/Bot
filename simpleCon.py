import utils
import pyautogui
import mouse
import detectImage
import numpy as np
from time import sleep
from time import time
from random import randint

xpPath = "/Users/kunaalsharma/Desktop/bot/Construction/conxp.png"

def runBot():
	sleep(2)

	interfaceLoc = utils.Location()
	startTime = time()
	while True:
		arrows = ["up", "down", "left", "right"]
		chosenArrow = arrows[randint(0,3)]
		utils.spamPress(chosenArrow)
		print(f"Spam pressed {chosenArrow}")

		if np.random.uniform(low=0, high = 10) < 2:
			try:
				utils.checkXP(xpPath)
				print("Checked xp")
			except:
				print("Xp was not present")

		sleepDuration = np.random.normal(180, 20)
		while sleepDuration > 270 or sleepDuration < 0:
			sleepDuration = np.random.normal(180, 20)

		print(f"Sleeping {sleepDuration} seconds")

		sleep(sleepDuration)
		if time() - startTime > 3600 * 16:
			print("Quitting after 16 hours")
			return


if __name__ == "__main__":
	runBot()