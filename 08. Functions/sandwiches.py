#8-12. Sandwiches:Write a function that accepts a list of items a person wants 
#on a sandwich. The function should have one parameter that collects as many 
#items as the function call provides, and it should print a summary of 
#the sandwich that’s being ordered. Call the function three times,
#using a different number of arguments each time.

def prepare_sandwich(*ingredients):
	'''A function that takes ingredients and makes a sandwich'''
	print('Making a sandwich with:')
	print(', '.join(ingredients))


prepare_sandwich('salami','pastrami','chips')
prepare_sandwich('salami','pastrami')
prepare_sandwich('salami','pastrami','chips','lettuce')

