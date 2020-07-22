#use a variable for the path
file_path = 'text_files\\pi_digits.txt'

#reading an entire file
with open(file_path) as file_object:
	contents = file_object.read()
print(contents)