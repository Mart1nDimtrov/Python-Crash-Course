#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
#up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When 
#you’re sure that your loop works, add five more Python terms to your glossary. 
#When you run your program again, these new words and meanings should 
#automatically be included in the output.

glossary = {
	'dictionary':'Python dictionaries are written with curly brackets, and they have keys and values.',
	'list':'List is a collection which is ordered and changeable.',
	'variable':'Variables are containers for storing data values.',
	'operator':'Operators are used to perform operations on variables and values.',
	'tuple':'A tuple is a collection which is ordered and unchangeable.'
}

glossary['set'] = 'A set is a collection which is unordered and unindexed.'
glossary['sort'] = 'The sort() method sorts the list ascending by default.'
glossary['items'] = "The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs."
glossary['loop'] = 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).'
glossary['string'] = 'In Python, a string is a sequence of Unicode characters.'

for term, description in glossary.items():
	print(f'{term.title()}:')
	print(description + '\n')