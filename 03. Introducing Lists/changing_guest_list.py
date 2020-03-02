# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite. 
# Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can’t make it. 
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

famous_people = ["brad pitt", "quentin tarantino", "deon cole"]

leaving_person = famous_people.pop(1)
print(f"{leaving_person.title()} won't make it.")

famous_people.insert(1, "Demi Moore")

for x in famous_people:
    print(f"Hi, {x.title()}, I would like to invite you for dinner.")
