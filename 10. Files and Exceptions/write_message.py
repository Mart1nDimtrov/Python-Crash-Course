file_name = 'text_files\\programming.py'

#create and write to the file
with open(file_name, 'w') as file_object:
	file_object.write('I love programming.')

#open the file and check the content
with open(file_name) as file_object:
	content = file_object.read()
print(content)

