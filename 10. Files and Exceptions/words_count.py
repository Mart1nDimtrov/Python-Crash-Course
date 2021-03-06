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
		words = contents.split()
		words_count = len(words)
		print(f"The file {filename} has about {words_count} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'animal_farm.txt']


for file_name in filenames:
	count_words(file_name)