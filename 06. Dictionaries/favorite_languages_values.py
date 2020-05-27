favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

#return a distinct list of values
for language in set(favorite_languages.values()):
	print(f'{language.title()}')