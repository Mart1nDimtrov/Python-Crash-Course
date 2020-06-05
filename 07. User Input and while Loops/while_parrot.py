message = "Tell me something, and I will repeat it back to you:"
message += "\nType 'quit' if you want to exit. "

active = True
while active:
	word = input(message)
	if word != 'quit':
		print(word)
	else:
		active = False
