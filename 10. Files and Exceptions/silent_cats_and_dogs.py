#10-9. Silent Cats and Dogs:Modify your except block in Exercise 10-8 to fail 
#silently if either file is missing.

def read_file(filename):
	"""Read the contents of a file"""
	#concatenate the file path
	file_folder = 'text_files\\'
	formatted_filename = file_folder + filename
	try:
		with open(formatted_filename, encoding='utf-8') as f:
				contents = f.read()
	except FileNotFoundError:
		pass #fail silently
	else:
		print(contents)	


files = ['dogs.txt', 'cats.txt']

for f in files:
	read_file(f)
	print()
