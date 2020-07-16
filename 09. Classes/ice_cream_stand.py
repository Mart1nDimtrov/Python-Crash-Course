#9-6. Ice Cream Stand:An ice cream stand is a specific kind of restaurant. Write 
#a class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
#the class will work; just pick the one you like better. Add an attribute called 
#flavors that stores a list of ice cream flavors. Write a method that displays 
#these flavors. Create an instance of IceCreamStand, and call this method.

"""A module that stores the class to represent an ice cream stand."""

#call the Restaurant from a module
from restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""A simple attempt to model a restaurant."""
	def __init__(self, name, cuisine_type):
			"""Initialize attributes of the parent class."""
			super().__init__(name, cuisine_type)
			self.flavors = ['chocolate','strawberry','pineapple']

	def list_flavors(self):
		'''List all the chocolate flavors'''
		print('We have the following flavors:')
		for flavor in self.flavors:
			print(flavor.title())



