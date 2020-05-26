favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

friends = ['phil', 'sarah']

for name,language in sorted(favorite_languages.items()):
	print(f"{name.title()}'s favorite language is {language.title()}.")
	#check if the person is a friend
	if name in friends:
		print(f'{name.title()}, I see you love {language.title()}!')

#check if Erin is in the poll
if 'erin' not in favorite_languages.keys(): #.keys() returns a list
	print("Erin, please take our poll!")