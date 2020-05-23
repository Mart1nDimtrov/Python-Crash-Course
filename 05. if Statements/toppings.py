available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'french fries']
#requested_toppings = [] check else condition

if requested_toppings:
	for topping in requested_toppings:
		if topping in available_toppings:
			print(f"Adding {topping}.")
		else:
			print(f"Sorry, we don't have {topping}.")

	print("\nFinished making your pizza!")
else:
	print('Are you sure you want a plain pizza?')



