#10-2. Learning C:You can use the replace() method to replace any word in a 
#string with a different word. Here’s a quick example showing how to replace 
#'dog'with 'cat'in a sentence:
#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
#'I really like cats.' 
#Read in each line from the file you just created, learning_python.txt, and 
#replace the word Pythonwith the name of another language, such as C. Print 
#each modified line to the screen.

filename = 'text_files\\learning_python.txt'
#read the file line by line
with open(filename) as file_object:
	for line in file_object:
		print(line.replace('Python', 'C#').strip())
print()