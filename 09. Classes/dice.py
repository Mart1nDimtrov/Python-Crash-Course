#9-13. Dice:Make a class Die with one attribute called sides, which has a default 
#value of 6. Write a method called roll_die() that prints a random number 
#between 1 and the number of sides the die has. Make a 6-sided die and roll it 
#10 times.
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.

#import the randint function from random module
from random import randint

class Die:
	"""A class that models a die and it's actions."""
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		print(randint(1,self.sides))

	def roll_die_times(self, times):
		for i in range(times):
			self.roll_die()
		print()

die_6 = Die(6)

die_6.roll_die_times(6)

die_10 = Die(10)

die_10.roll_die_times(10)

die_20 = Die(20)

die_20.roll_die_times(20)