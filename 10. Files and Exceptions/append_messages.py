file_name = 'text_files\\programming.txt'

#append to the existing file or create on if it doesn't exist
with open(file_name, 'a') as file_object:
	file_object.write("\nI also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

#open the file and check the content
with open(file_name) as file_object:
	content = file_object.read()
print(content)