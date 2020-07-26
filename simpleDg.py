import utils
import pyautogui
import mouse
import detectImage
import numpy as np
from random import randint
from time import sleep

conPath = "/Users/kunaalsharma/Desktop/bot/Construction/boat/vals.txt"
xpPath = "/Users/kunaalsharma/Desktop/bot/Dungeoneering/dgxp.png"

def runBot():
	sleep(2)

	def foo():
		if randint(0,100) % 2 == 0:
			utils.spamPress('left')
		else:
			utils.spamPress('right')

	xpLoc = utils.Location()

	while True:

		succ = utils.performAction(foo, utils.makeSuccess(xpLoc, xpPath, False))
		if not succ:
			print("Failed, quitting")
			return

		sleep(1)

		if np.random.uniform(low=0, high = 10) < 2:
			utils.checkXP(xpPath)
			print("Checked xp")

		sleepDuration = np.random.normal(180, 20)
		while sleepDuration > 270 or sleepDuration < 0:
			sleepDuration = np.random.normal(180, 20)

		print(f"Sleeping {sleepDuration} seconds")

		sleep(sleepDuration)

if __name__ == "__main__":
	runBot()