#9-8. Privileges: Write a separate Privileges class. The class should have one 
#attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance 
#as an attribute in the Adminclass. Create a new instance of Admina nd use your 
#method to show its privileges.

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

class Privileges():
	"""Create a model for privileges."""
	def __init__(self, role):
		self.privileges = ["can add post", "can delete post", "can ban user"]
		self.role = role
		
	def show_privileges(self):
		'''List all the privileges a role has.'''
		print(f'These are all the privileges an {self.role} has:')
		for privilege in self.privileges:
			print(privilege.title())

class Admin(User):
	"""Create a model for website's admin."""
	def __init__(self, first_name, last_name, email, sex='None'):
		super().__init__(first_name, last_name, email, sex)
		self.privileges = Privileges('admin')


user_1 = Admin('nina', 'amis', 'naoya@yahoo.com')
user_1.describe_user()
user_1.privileges.show_privileges()