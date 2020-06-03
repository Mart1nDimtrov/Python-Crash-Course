#7-3. Multiples of Ten:Ask the user for a number, and then report whether the 
#number is a multiple of 10 or not.

number = int(input('Please enter a number: '))

if number % 10 == 0:
	print('The number is a multiple of ten.')
else:
	print('The number is not a multiple of ten.')