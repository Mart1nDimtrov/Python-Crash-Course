#10-3. Guest:Write a program that prompts the user for their name. When they 
#respond, write their name to a file called guest.txt.

#use the absolute path
file_name = 'C:\\Users\\martin\\Desktop\\Python-Crash-Course\\10. Files and Exceptions\\text_files\\guest.txt'

guest_name = input('Please enter a name: ')

with open(file_name, 'w') as file_object:
	file_object.write(guest_name)

