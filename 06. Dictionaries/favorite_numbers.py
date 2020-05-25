#6-2. Favorite Numbers:Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. Think of a favorite 
#number for each person, and store each as a value in your dictionary. Print 
#each person’s name and their favorite number. For even more fun, poll a few 
#friends and get some actual data for your program.
['bob','jeremiah','linda','tom','jerry']
favorite_numbers = {
	'bob':15,
	'jeremiah':13,
	'linda':12,
	'tom':11,
	'jerry':10,
}

for name in favorite_numbers:
	number = favorite_numbers[name]
	print(f"{name.title()}'s favorite number is: {number}")