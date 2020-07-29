#10-5. Programming Poll:Write a whileloop that asks people why they like 
#programming. Each time someone enters a reason, add their reason to a file 
#that stores all the responses.

#use the absolute path
file_name = 'C:\\Users\\martin\\Desktop\\Python-Crash-Course\\10. Files and Exceptions\\text_files\\programming_poll.txt'

while True:
	poll_answer = input("Please enter why you like programming or 'q' to quit: ")
	if poll_answer == 'q':
		break
	else:
		with open(file_name, 'a') as file_object:
			file_object.write(poll_answer + "\n")