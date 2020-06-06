#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
#pizza toppings until they enter a 'quit'value. As they enter each topping, 
#print a message saying you’ll add that topping to their pizza.

prompt = 'Write the toppings one by one followed by enter.'
prompt += '\nType "quit" to stop. '

print(prompt)
active = True
while active:
	topping = input()
	if topping == 'quit':
		active = False
	else:
		print("I'll add {topping} to your pizza.")
	
	


