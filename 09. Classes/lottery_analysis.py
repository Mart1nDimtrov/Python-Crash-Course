#9-15. Lottery Analysis:You can use a loop to see how hard it might be to win 
#the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
#Write a loop that keeps pulling numbers until your ticket wins. Print a message 
#reporting how many times the loop had to run to give you a winning ticket.

from random import choice, randint

my_ticket = [5,'k',7,'g']
random_things = ['a',1,'d','j',5,'k',7,'g']

winning_combo = ['','','','']
guess_count = 0

while True:
	#assign a random element from random_things
	#on a rand position from the beginning to the end of winning_combo
	winning_combo[randint(0,3)] = choice(random_things)
	#check how close we are to the best guess
	print(winning_combo)
	guess_count += 1
	if winning_combo == my_ticket:
		break
	

print(f'The loop had to run: {guess_count} times to find a match.')