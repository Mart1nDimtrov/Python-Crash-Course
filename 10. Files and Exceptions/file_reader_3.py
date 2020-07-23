#use a variable for the path
file_path = 'text_files\\pi_digits.txt'

#store the lines as a list
with open(file_path) as file_object:
	lines = file_object.readlines()

#read the objects from the list one by one
for line in lines:
	print(line, end='')

print()