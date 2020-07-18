#9-14. Lottery:Make a list or tuple containing a series of 10 numbers and 
#five letters. Randomly select four numbers or letters from the list and print a 
#message saying that any ticket matching these four numbers or letters wins a 
#prize.

from random import choice

random_things = ['a',1,'d','j',5,'k',7,'g']

winning_combo = ''
for i in range(4):
	winning_combo += str(choice(random_things))

print(f'Any ticket matching this: {winning_combo} is the winner.')
