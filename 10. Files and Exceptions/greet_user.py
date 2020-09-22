import json

username = input('What is your name? ')

with open(filename) as f:
	username = json.load(f)
	print(f'Welcome back, {username}!')
