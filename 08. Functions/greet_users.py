
def greet_users(usernames):
	for user_name in usernames:
		message = f'Hello, {user_name.title()}!'
		print(message)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)