#7-10. Dream Vacation:Write a program that polls users about their dream vacation. 
#Write a prompt similar to If you could visit one place in the world, where 
#would you go?Include a block of code that prints the results of the poll.

poll = {}

active = True
while  active:
	name = input('What is your name? ')
	vacation = input('If you could visit one place in the world, where would you go? ')

	poll[name] = vacation
	active_question = input('Would you like another person to take the poll? (yes/no) ')
	if active_question == 'no':
		active = False

for name, vacation in poll.items():
	print(f"{name.title()}'s dream vaction is {vacation.title()}.")