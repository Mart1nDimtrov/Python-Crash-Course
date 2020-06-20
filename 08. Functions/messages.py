#8-9. Messages:Make a list containing a series of short text messages. Pass the 
#list to a function called show_messages(), which prints each text message.

def show_messages(messages):
	for message in messages:
		print(message)

messages = ['This is a message.','This is also a message.','Hey, another message!']
show_messages(messages)