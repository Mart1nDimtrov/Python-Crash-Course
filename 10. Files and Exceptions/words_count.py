def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		words = contents.split()
		words_count = len(words)
		print(f"The file {filename} has about {words_count} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
file_folder = 'text_files\\'

for file_name in filenames:
	count_words(file_folder+file_name)