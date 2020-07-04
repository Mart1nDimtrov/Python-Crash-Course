#9-2. Three Restaurants:Start with your class from Exercise 9-1. Create three 
#different instances from the class, and call describe_restaurant() for each 
#instance.

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

restaurant_1 = Restaurant('La Pergola','italian')
restaurant_2 = Restaurant('Sushi Ueda','sushi')
restaurant_3 = Restaurant('Azurmendi','mediterranean')

restaurant_1.describe_restaurant()
print()
restaurant_2.describe_restaurant()
print()
restaurant_3.describe_restaurant()
