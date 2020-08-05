#10-6. Addition:One common problem when prompting for numerical input 
#occurs when people provide text instead of numbers. When you try to convert 
#the input to an int, you’ll get a ValueError. Write a program that prompts for 
#two numbers. Add them together and print the result. Catch the ValueError if 
#either input value is not a number, and print a friendly error message. Test your 
#program by entering two numbers and then by entering some text instead of a 
#number.

print("Give me two numbers on seperate lines and I'll add them:")
try:
	number_1 = int(input("First number: "))
	number_2 = int(input("Second number: "))
except ValueError:
	print('One of your numbers is not in the right format.')
else:
	result = number_1 + number_2
	print(f"The result is: {result}")