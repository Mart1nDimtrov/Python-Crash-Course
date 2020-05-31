#6-9. Favorite Places:Make a dictionary called favorite_places. Think of three 
#names to use as keys in the dictionary, and store one to three favorite places 
#for each person. To make this exercise a bit more interesting, ask some friends 
#to name a few of their favorite places. Loop through the dictionary, and print 
#each person’s name and their favorite places.

favorite_places = {
	'laurel':['Waterton National Park, Canada'],
	'erik':['Rio Amazonas, Peru','Teotihuacan pyramids, Mexico'],
	'dave':['Prague, Czech Republic','Chiang Mai, Thailand','Chinsta, South Africa'],
}

for person, favorite_places in favorite_places.items():
	if len(favorite_places) > 1:
		print(f"{person.title()}'s favorite places are:")
	else:
		print(f"{person.title()}'s favorite is:")
	for favorite_place in favorite_places:
		print(favorite_place) 
	print('\n')