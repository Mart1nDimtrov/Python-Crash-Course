#use a variable for the path
file_path = 'text_files\\pi_digits.txt'

#read line by line
with open(file_path) as file_object:
	for line in file_object:
		print(line, end='') #use the end option
print()