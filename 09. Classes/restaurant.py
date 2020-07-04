#9-1. Restaurant:Make a class called Restaurant. The __init__() method for 
#Restaurant should store two attributes: a restaurant_nameand a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of 
#information, and a method called open_restaurant() that prints a message 
#indicating that the restaurant is open.
#Make an instance called restaurant from your class. 
#Print the two attributes individually, and then call both methods.

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

new_restaurant = Restaurant('Michelline','gourme')
print(f'Restaurant - {new_restaurant.name.title()}')
print(f'Cuisine type - {new_restaurant.cuisine_type}')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()