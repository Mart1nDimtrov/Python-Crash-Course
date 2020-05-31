#6-2. Favorite Numbers:Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. Think of a favorite 
#number for each person, and store each as a value in your dictionary. Print 
#each person’s name and their favorite number. For even more fun, poll a few 
#friends and get some actual data for your program.
['bob','jeremiah','linda','tom','jerry']
favorite_numbers = {
	'bob':[14,232,231,32],
	'jeremiah':[13,4,22],
	'linda':[12,9,15],
	'tom':[11,2],
	'jerry':[10],
}

for name, numbers in favorite_numbers.items():
	if len(numbers) > 1: 
		print(f"{name.title()}'s favorite numbers are:")
	else:
		print(f"{name.title()}'s favorite number is:")
	print(', '.join(str(n) for n in numbers))