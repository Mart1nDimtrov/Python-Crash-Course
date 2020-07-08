#9-4. Number Served:Start with your program from Exercise 9-1 (page 162). 
#Add an attribute called number_served with a default value of 0. Create an 
#instance called restaurantfrom this class. Print the number of customers the 
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number 
#of customers that have been served. Call this method with a new number and 
#print the value again.
#Add a method called increment_number_served() that lets you increment 
#the number of customers who’ve been served. 
#Call this method with any number you like that could represent 
#how many customers were served in, say, a 
#day of business.

class Restaurant:
	"""A simple attempt to model a restaurant.""" 
	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine_type attributes."""
		self.name = name
		self.cuisine_type = cuisine_type
		self.numbers_served = 0

	def describe_restaurant(self):
		print(f'This is the {self.name.title()} restaurant!')
		print(f'It serves {self.cuisine_type} food.')

	def open_restaurant(self):
		print('The restaurant is open!')

	def set_number_served(self, numbers_served):
		'''Set the number of served customers.'''
		self.numbers_served = numbers_served

	def increment_number_served(self, number):
		'''Increment the number of served customers.'''
		self.numbers_served += number

#set an instance
restaurant = Restaurant('Michelline','gourme')
print(f'Restaurant - {restaurant.name.title()}')
print(f'Cuisine type - {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#set directly 
restaurant.numbers_served = 5
print(f'Customers served: {restaurant.numbers_served}')
#set thought a method
restaurant.set_number_served(10)
print(f'Customers served: {restaurant.numbers_served}')
#increment thought a method
restaurant.increment_number_served(5)
print(f'Customers served: {restaurant.numbers_served}')
