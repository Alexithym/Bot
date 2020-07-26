from pyautogui import locate
from utils import Location



class Potion:

	def __init__(self, doses, path):
		self.location = Location()
		self.doses = doses
		self.path = path

	def setDoses(self, doses):
		self.doses = doses
		
	def getDoses(self):
		return self.doses

	def getPath(self):
		return self.path

	def getLocation(self):
		return self.location
