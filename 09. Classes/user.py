"""A class that represents a user."""
class User():
	"""Create a model for website user."""
	def __init__(self, first_name, last_name, email, sex='None'):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.sex = sex

	def describe_user(self):
		print(f"The user's names are : {self.first_name.title()} {self.last_name.title()}")
		print(f'His email is - {self.email}')
		print(f'His/Hers sex is - {self.sex}')

	def greet_user(self):
		print(f'Hello, {self.first_name.title()}!')