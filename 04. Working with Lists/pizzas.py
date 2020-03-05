# 4-1. Pizzas:Think of at least three kinds of your favorite pizza. Store these 
# pizza names in a list, and then use a forloop to print the name of each pizza.
# 	 Modify your forloop to print a sentence using the name of the pizza 
# instead of printing just the name of the pizza. For each pizza you should 
# have one line of output containing a simple statement likeI like pepperoni 
# pizza.
#	 Add a line at the end of your program, outside the forloop, that states 
# how much you like pizza. The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence, such as 
# I really love pizza!

pizzas = ["pepperoni", "margherita", "quattro formaggi"]

for pizza in pizzas:
	print(pizza)

print("\n")

for pizza in pizzas:
	print(f"I like {pizza}.")

print("\nI really love pizza!")