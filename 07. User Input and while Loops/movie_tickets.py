#7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
#a person’s age. If a person is under the age of 3, the ticket is free; if they are 
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
#$15. Write a loop in which you ask users their age, and then tell them the cost 
#of their movie ticket.

prompt = 'Tell me your age to find the price of your ticket.'
prompt += 'Type "quit" to exit. '

age = input(prompt)

while True:
	if age == 'quit':
		break
	else:
		age_2 = int(age)
		if age_2 < 3:
			print('Your ticket is free.')
		elif age_2 >= 3 and age_2 <= 12:
			print('Your ticket is 10$.')
		elif age_2 > 12:
			print('Your ticket is 12$.')
	age = input(prompt)

