file_name = 'text_files\\programming.txt'

#create and write to the file
with open(file_name, 'w') as file_object:
	file_object.write('I love programming.\n')	#use a new line
	file_object.write('I love creating new games.')

#open the file and check the content
with open(file_name) as file_object:
	content = file_object.read()
print(content)

