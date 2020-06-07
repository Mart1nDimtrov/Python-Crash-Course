#7-9. No Pastrami:Using the list sandwich_ordersfrom Exercise 7-8, make sure 
#the sandwich 'pastrami'appears in the list at least three times. Add code 
#near the beginning of your program to print a message saying the deli has 
#run out of pastrami, and then use a whileloop to remove all occurrences of 
#'pastrami'from sandwich_orders. Make sure no pastrami sandwiches end up 
#in finished_sandwiches.


sandwich_orders = ['pastrami','tuna','roast beef','pastrami','club','pastrami']
finished_sandwiches = []

print('The restaurant has run out of pastrami.')
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f'I made your {sandwich} sandwich.')
	finished_sandwiches.append(sandwich)

print('Sandwiches made:')
for sandwich in finished_sandwiches:
	print(sandwich.title())