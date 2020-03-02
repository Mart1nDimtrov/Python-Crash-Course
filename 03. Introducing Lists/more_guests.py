# 3-6. More Guests: You just found a bigger dinner table,
# so now more space is available.
# Think of three more guests to invite to dinner. 
# Start with your program from Exercise 3-4 or Exercise 3-5.
# Add a print() call to the end of your program informing people
# that you found a bigger dinner table. 
# Use insert() to add one new guest to the beginning of your list. 
# Use insert() to add one new guest to the middle of your list. 
# Use append() to add one new guest to the end of your list. 
# Print a new set of invitation messages, one for each person in your list.

famous_people = ["brad pitt", "quentin tarantino", "deon cole"]

print("The dinner table has expanded!")

famous_people.insert(0, "Bradley Cooper")
famous_people.insert(int(len(famous_people) / 2), "Jennifer Lawrence")
famous_people.append("Hristo Stoichkov")

for x in famous_people:
    print(f"Hi, {x.title()}, I would like to invite you for dinner.")
    
