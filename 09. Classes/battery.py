#9-9. Battery Upgrade:Use the final version of electric_car.py from this section. 
#Add a method to the Battery class called upgrade_battery(). This method 
#should check the battery size and set the capacity to 100 if it isn’t already. 
#Make an electric car with a default battery size, call get_range() once, and 
#then call get_range() a second time after upgrading the battery. You should 
#see an increase in the car’s range.

"""A class that represents an electric car's battery."""


class Battery:
	"""Represents a battery of an electric car."""
	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 310

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		'''Upgrade the capacity of the battery.'''
		if self.battery_size != 100:
			self.battery_size = 100





		
