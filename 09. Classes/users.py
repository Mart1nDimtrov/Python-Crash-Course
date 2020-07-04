#9-3. Users:Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored 
#in a user profile. Make a method called describe_user() that prints a summary 
#of the user’s information. Make another method called greet_user() that prints 
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods 
#for each user.

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


user_1 = User('nina', 'amis', 'naoya@yahoo.com')
user_2 = User('ull', 'man', 'ullman@yahoo.com')
user_3 = User('dave', 'miller', 'dmiller@yahoo.com')

user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()
print()
user_3.describe_user()
user_3.greet_user()
