#10 - 7. Addition Calculator:Wrap your code from Exercise 10-6 in a while loop 
#so the user can continue entering numbers even if they make a mistake and 
#enter text instead of a number.



while True:
	print("Give me two numbers on seperate lines and I'll add them:")
	print("Type 'q' to exit.")
	try:
		number_1 = input("First number: ")
		if number_1 == 'q':
			break
		else:
			number_1 = int(number_1)
	except ValueError:
		print(f'Your first number is not in the right format.')
	else:
		try:
			number_2 = int(input("Second number: "))
			if number_2 == 'q':
				break
			else:
				number_2 = int(number_2)
		except ValueError:
			print(f'Your second number is not in the right format.')
		else:
			result = number_1 + number_2
			print(f"The result is: {result}")