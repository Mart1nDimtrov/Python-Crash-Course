# 4-13. Buffet:A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# •	 Use a forloop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the 
# change.
# •	 The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a forloop to print 
# each of the items on the revised menu.

buffet_menu = ("hamburgers","hot dogs","corn","chicken wings","donuts")

print("The buffet offers:")
for buffet_item in buffet_menu:
	print(buffet_item.title())

# try to assign a new value
# buffet_menu[4] = "apples"

buffet_menu = ("hamburgers","hot dogs","corn","ceaser's salad","apples")
print("\nThe buffet has changed:")
for buffet_item in buffet_menu:
	print(buffet_item.title())