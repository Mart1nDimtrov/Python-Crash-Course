'''A module that stores the special user class admin.'''
#import the user class
from user import User
from privileges import Privileges

class Admin(User):
	"""Create a model for website's admin."""
	def __init__(self, first_name, last_name, email, sex='None'):
		super().__init__(first_name, last_name, email, sex)
		self.privileges = Privileges('admin')


		