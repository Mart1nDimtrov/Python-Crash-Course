#10-10. Common Words:Visit Project Gutenberg (https://gutenberg.org/ ) 
#and find a few texts you’d like to analyze. Download the text files for these 
#works, or copy the raw text from your browser into a text file on your 
#computer.
#You can use the count() method to find out how many times a word or 
#phrase appears in a string. For example, the following code counts the number 
#of times 'row' appears in a string:
#>>> line = "Row, row, row your boat" 
#>>> line.count('row') 
#2 
#>>> line.lower().count('row')
#3 
#Notice that converting the string to lowercase using lower() catches 
#all appearances of the word you’re looking for, regardless of how it’s 
#formatted.
#Write a program that reads the files you found at Project Gutenberg and 
#determines how many times the word 'the' appears in each text. This will be 
#an approximation because it will also count words such as 'then' and 'there'. 
#Try counting 'the ', with a space in the string, and see how much lower your 
#count is.

def count_words(filename):
	"""Count the approximate number of words in a file."""
	#store the missing files in a seperate file
	not_found_log = 'text_files\\missing_files.txt'
	#concatenate the file path
	file_folder = 'text_files\\'
	filename = file_folder + filename
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		with open(not_found_log, 'a') as file_object:
			file_object.write(filename + '\n')
	else:
		words_count = contents.lower().count('the ')
		print(f"The file {filename} has 'the' about {words_count} times.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'animal_farm.txt']


for file_name in filenames:
	count_words(file_name)