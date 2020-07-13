#9-6. Ice Cream Stand:An ice cream stand is a specific kind of restaurant. Write 
#a class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
#the class will work; just pick the one you like better. Add an attribute called 
#flavors that stores a list of ice cream flavors. Write a method that displays 
#these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
	"""A simple attempt to model a restaurant.""" 
	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine_type attributes."""
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'This is the {self.name.title()} restaurant!')
		print(f'It serves {self.cuisine_type} food.')

	def open_restaurant(self):
		print('The restaurant is open!')

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

new_restaurant = IceCreamStand('Raffy','ice cream')
print(f'Restaurant - {new_restaurant.name.title()}')
print(f'Cuisine type - {new_restaurant.cuisine_type}')
new_restaurant.list_flavors()

