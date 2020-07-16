"""A set of classes that can be used to represent electric cars."""

from car import Car
from battery import Battery

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()

