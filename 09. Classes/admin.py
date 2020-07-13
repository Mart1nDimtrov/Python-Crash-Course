#9 - 7. Admin:An administrator is a special kind of user. Write a class called 
#Adminthat inherits from the User class you wrote in Exercise 9-3 (page 162) 
#or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
#of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of 
#privileges. Create an instance of Admin, and call your method.

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

class Admin(User):
	"""Create a model for website's admin."""
	def __init__(self, first_name, last_name, email, sex='None'):
		super().__init__(first_name, last_name, email, sex)
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		'''List all the privileges an admin has.'''
		print(f'These are all the privileges {self.first_name.title()} has:')
		for privilege in self.privileges:
			print(privilege.title())

user_1 = Admin('nina', 'amis', 'naoya@yahoo.com')
user_1.describe_user()
user_1.show_privileges()
		