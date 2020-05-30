#6 - 7. People:Start with the program you wrote for Exercise 6-1 (page 99). 
#Make two new dictionaries representing different people, and store all three 
#dictionaries in a list called people. Loop through your list of people. As you 
#loop through the list, print everything you know about each person.

people = {
	'stoyan_24': {
		'first_name':'stoyan',
		'last_name':'filipov',
		'age':25,
		'city':'Varna',
	},
	'maria_1': {
		'first_name':'maria',
		'last_name':'filipova',
		'age':27,
		'city':'Varna',
	},
	'gloria_9': {
		'first_name':'gloria',
		'last_name':'stafanova',
		'age':27,
		'city':'Varna',
	},
}

for name, person in people.items():
	print(f'\nUsername: {name.title()}')
	print(f'First name: {person["first_name"].title()}.')
	print(f'Last name: {person["last_name"].title()}.')
	print(f'Age: {person["age"]}.')
	print(f'City: {person["city"]}.')