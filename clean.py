from time import sleep
import pyautogui
import numpy as np 
import random

def spam(key='1', interval=0.3):
	while True:
		if (random.randint(0,100) % 2 == 0):
			pyautogui.press(key)
			sleep(interval + np.random.normal(0, 0.06))
		else:
			pyautogui.click()
			sleep(interval + np.random.normal(0, 0.06))


if __name__ == "__main__":
	sleep(1)
	spam()
