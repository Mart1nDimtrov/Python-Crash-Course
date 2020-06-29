#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 
#function send_messages() with a copy of the list of messages. After calling the 
#function, print both of your lists to show that the original list has retained its 
#messages.

def show_messages(messages,sent_messages):
	'''Imitates sending messages by moving them
	from one list to another'''
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)

messages = ['This is a message.','This is also a message.','Hey, another message!']
sent_messages = []
#keep the original list 
show_messages(messages[:],sent_messages)

print(messages)
print(sent_messages)