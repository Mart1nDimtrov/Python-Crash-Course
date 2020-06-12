#8-5. Cities:Write a function called describe_city() that accepts the name of 
#a city and its country. The function should print a simple sentence, such as 
#Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the 
#default country.

def describe_city(city,country='brazil'):
	'''Prints a city and it's country.'''
	print(f'{city.title()} is in {country.title()}.')

#first one is wrong, using only the first param
describe_city('mexico')
describe_city('mexico','mexico')
describe_city('salvador')
describe_city('rio de janeiro')
describe_city('sao paulo')