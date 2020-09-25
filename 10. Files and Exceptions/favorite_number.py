#10-12. Favorite Number Remembered: Combine the two programs from 
#Exercise 10-11 into one file. If the number is already stored, report the favorite 
#number to the user. If not, prompt for the user’s favorite number and store it in a 
#file. Run the program twice to see that it works.

import json


def get_stored_favorite_number(filename):
	'''Get stored favorite number if available.'''
	try:
		with open(filename) as f:
			favorite_number = json.load(f)	
	except:
		return None
	else:
		return favorite_number	

def get_new_favorite_number(filename):
	'''Prompt for a new favorite number.'''
	favorite_number = input('What is your favorite number? ')
	with open(filename, 'w') as f:
		json.dump(favorite_number, f)

filename = 'json_files\\favorite_number.json'
favorite_number = get_stored_favorite_number(filename)
if favorite_number:
	print(f'I know your favorite number! It’s {favorite_number}.')
else:
	get_new_favorite_number(filename)