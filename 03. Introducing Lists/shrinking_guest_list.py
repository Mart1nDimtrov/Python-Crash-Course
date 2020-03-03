# 3 - 7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests.
# 	Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
# 	Use pop()to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.
# 	Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
# 	Use delto remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program.

famous_people = ["brad pitt", "quentin tarantino", "deon cole"]

print("The dinner table has expanded!")

famous_people.insert(0, "Bradley Cooper")
famous_people.insert(int(len(famous_people) / 2), "Jennifer Lawrence")
famous_people.append("Hristo Stoichkov")

for x in famous_people:
    print(f"Hi, {x.title()}, I would like to invite you for dinner.")

print("I just found the dinner table won't arrive on time!")

# take the length of the list
people_length = len(famous_people) 

# iterate untill there are only two left
for x in range(2,people_length):
	person = famous_people.pop()
	print(f"{person.title()}, I'm sorry that there is no more room")

# check list
print(famous_people)

# print a message to the still invited
for x in famous_people:
    print(f"Hi, {x.title()}, you're still invited!")

# delete all
del famous_people[0:2]
# check list
print(famous_people)


