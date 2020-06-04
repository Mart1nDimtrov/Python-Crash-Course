message = "Tell me something, and I will repeat it back to you:"
message += "\nType 'quit' if you want to exit. "

word = ''
while word != 'quit':
	word = input(message)
	if word != 'quit':
		print(word)
