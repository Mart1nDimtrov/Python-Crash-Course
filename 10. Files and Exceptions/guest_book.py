#10-4. Guest Book:Write a whileloop that prompts users for their name. When 
#they enter their name, print a greeting to the screen and add a line recording 
#their visit in a file called guest_book.txt. Make sure each entry appears on a 
#new line in the file.

#use the absolute path
file_name = 'C:\\Users\\martin\\Desktop\\Python-Crash-Course\\10. Files and Exceptions\\text_files\\guest_book.txt'

while True:
	guest_name = input("Please enter a name or 'q' to quit: ")
	if guest_name == 'q':
		break
	else:
		with open(file_name, 'a') as file_object:
			file_object.write(guest_name + "\n")
