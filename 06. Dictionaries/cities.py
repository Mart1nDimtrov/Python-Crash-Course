#6 -11. Cities:Make a dictionary called cities. Use the names of three cities as 
#keys in your dictionary. Create a dictionary of information about each city and 
#include the country that the city is in, its approximate population, and one fact 
#about that city. The keys for each city’s dictionary should be something like 
#country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.

cities = {
	'new york':	{
		'country':'USA',
		'population':8336817,
		'fact':('New York City has been described as the cultural, financial, '
				'and media capital of the world, significantly influencing commerce, '
				'entertainment, research, technology, education, politics, tourism, art, fashion, and sports.'
				),
	},
	'santa fe':	{
		'country':'USA',
		'population':84683,
		'fact':('It is considered one of the world''s great art cities, '
				'due to its many art galleries and installations, '
				'and is recognized by UNESCO''s Creative Cities Network.'),
	},
	'seattle':	{
		'country':'USA',
		'population':84683,
		'fact':('The Seattle area was inhabited by Native Americans '
				'for at least 4,000 years before the first permanent European settlers.'),
	},
}

for city_name, city_info in cities.items():
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']
	print(f'\n{city_name.title()}')
	print(f'{country.upper()}') #USA specific formatting
	print(f'Population: {population:,}')
	print(f'{fact}')

