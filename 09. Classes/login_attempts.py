#9-5. Login Attempts:Add an attribute called login_attempts to your User
#class from Exercise 9-3 (page 162). Write a method called increment_login
#_attempts() that increments the value of login_attempts by 1. Write another 
#method called reset_login_attempts()that resets the value of login_attempts
#to 0.
#Make an instance of the Userclass and call increment_login_attempts()
#several times. Print the value of login_attemptsto make sure it was incremented 
#properly, and then call reset_login_attempts(). Print login_attemptsagain to 
#make sure it was reset to 0.


class User():
	"""Create a model for website user."""
	def __init__(self, first_name, last_name, email, sex='None'):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.sex = sex
		self.login_attempts = 0

	def describe_user(self):
		print(f"The user's names are : {self.first_name.title()} {self.last_name.title()}")
		print(f'His email is - {self.email}')
		print(f'His/Hers sex is - {self.sex}')

	def greet_user(self):
		print(f'Hello, {self.first_name.title()}!')

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_1 = User('nina', 'amis', 'naoya@yahoo.com')
user_1.describe_user()
user_1.greet_user()
print()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"User's login attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"User's login attempts: {user_1.login_attempts}")