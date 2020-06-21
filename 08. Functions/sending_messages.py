#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#Write a function called send_messages() that prints each text message and 
#moves each message to a new list called sent_messages as it’s printed. After 
#calling the function, print both of your lists to make sure the messages were 
#moved correctly.

def show_messages(messages,sent_messages):
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)

messages = ['This is a message.','This is also a message.','Hey, another message!']
sent_messages = []
show_messages(messages,sent_messages)

print(messages)
print(sent_messages)