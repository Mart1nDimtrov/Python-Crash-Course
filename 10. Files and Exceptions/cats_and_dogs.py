#10-8. Cats and Dogs:Make two files, cats.txt and dogs.txt. Store at least three 
#names of cats in the first file and three names of dogs in the second file. Write 
#a program that tries to read these files and print the contents of the file to the 
#screen. Wrap your code in a try-except block to catch the FileNotFounderror, 
#and print a friendly message if a file is missing. 
#Move one of the files to a different location on your system,
#and make sure the code in the except block 
#executes properly.

def read_file(filename):
	"""Read the contents of a file"""
	#concatenate the file path
	file_folder = 'text_files\\'
	formatted_filename = file_folder + filename
	try:
		with open(formatted_filename, encoding='utf-8') as f:
				contents = f.read()
	except FileNotFoundError:
		print(f'The file <{filename}> is missing.')
	else:
		print(contents)	


files = ['dogs.txt', 'cats.txt']

for f in files:
	read_file(f)
	print()
