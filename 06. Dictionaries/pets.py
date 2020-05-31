#6-8. Pets:Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as 
#you do, print everything you know about each pet.

dog = {'owner':'bob','name':'oscar','kind':'dog','age':7}
cat = {'owner':'jim','name':'lucy','kind':'cat','age':3}
lizard = {'owner':'tracy','name':'bronco','kind':'lizard','age':4}

pets = [dog,cat,lizard]

for pet in pets:
	owner_name = pet['owner']
	pet_name = pet['name']
	pet_kind = pet['kind']
	pet_age = pet['age']
	print(f"\n{owner_name.title()}'s pet's name is {pet_name.title()}.")
	print(f"It's a {pet_age} year old {pet_kind}.")