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




