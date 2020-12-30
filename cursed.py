import mouse
import utils
import pyautogui 
import numpy as np 
import random 
from time import time, sleep

crossing_path = "Combat/crossing.png"
prayer_path = "Combat/prayer.png"
attack_icon_path = "Combat/attack_icon.png"

potion_key = 'y'
silverhawk_key = '0'
ritual_key = 'z'

def five_minute_extension():
	print("Starting to perform 5 minute duties")
	utils.spamPress(potion_key, times=2)
	sleep(utils.getSleep(2.1, 0.3))

	utils.spamPress(silverhawk_key)
	sleep(utils.getSleep(1.7, 0.3))

	utils.spamPress(ritual_key)
	sleep(utils.getSleep(1.0, 0.4))
	print("Performed 5 minute duties")

def check_prayer(prayer_loc):
	while not pyautogui.locateOnScreen(prayer_path, confidence=0.9, grayscale=True):
		print("Detected prayers not active...activating...")
		(x, y, xT, yT) = prayer_loc
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()
		sleep(utils.getSleep(2, 0.3))
		mouse.moveCenter()
	else:
		print("Detected prayers active...")

def check_in_combat(emergency_loc):
	start_time = time() 
	while not pyautogui.locateOnScreen(attack_icon_path, confidence=0.9, grayscale=True):
		sleep_duration = utils.getSleep(1, 0.3)
		print(f"Detected not in combat...waiting {sleep_duration} seconds")
		sleep(sleep_duration)
		if time() > start_time + 60:
			print("Not in combat for 60 seconds, teleporting...")
			teleport_out(emergency_loc)

	print("Detected in combat...")

def note_keys(notepaper_loc):
	crossing_loc = pyautogui.locateOnScreen(crossing_path, confidence=0.9, grayscale=True)
	while crossing_loc:
		print("Detected key of crossing in inventory...")
		(x, y, xT, yT) = notepaper_loc
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()
		sleep(utils.getSleep(2.5, 1))

		(x, y, xT, yT) = utils.convert_pyautogui_to_mouse(crossing_loc)
		mouse.moveRect(x, y, xT, yT)
		pyautogui.click()
		print("Noted keys of crossing...")
		sleep(utils.getSleep(2, 1))
		mouse.moveCenter()

		crossing_loc = pyautogui.locateOnScreen(crossing_path, confidence=0.9, grayscale=True)

	else: 
		print("Detected no keys of crossing in inventory...")

def teleport_out(emergency_loc):
	(x, y, xT, yT) = emergency_loc
	mouse.moveRect(x, y, xT, yT)
	pyautogui.click()
	print("Exiting...")
	exit(1)	

def run_bot():
	notepaper_loc = utils.getBoundingRectangle()
	prayer_loc = utils.getBoundingRectangle()
	emergency_loc = utils.getBoundingRectangle()

	start_time = time() 
	last_pot_time = -1
	while time() - start_time < 8 * 3600: 
		# Drink pots if necessary
		if time() - last_pot_time > 5 * 60:
			five_minute_extension()
			last_pot_time = time() 

		# Assert prayers are active
		check_prayer(prayer_loc)

		# Note keys to crossing
		note_keys(notepaper_loc)

		# Assert still in combat
		check_in_combat(emergency_loc)

		# Avoid time-out 10% of time
		if random.randint(1, 100) < 10: 
			utils.avoidTimeout()

		sleep(utils.getSleep(5, 0.2))

	teleport_out(emergency_loc)

if __name__ == "__main__":
	sleep(2)
	run_bot()
