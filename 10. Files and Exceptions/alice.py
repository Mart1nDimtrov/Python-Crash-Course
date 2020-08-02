filename = 'text_files\\alice.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	words_count = len(contents.split())
	print(f"The file {filename} has about {words_count} words.")