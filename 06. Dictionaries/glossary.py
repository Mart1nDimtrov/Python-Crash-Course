#6-3. Glossary:A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#•	 Think of five programming words you’ve learned about in the previous 
#chapters. Use these words as the keys in your glossary, and store their 
#meanings as values.
#•	 Print each word and its meaning as neatly formatted output. You might 
#print the word followed by a colon and then its meaning, or print the word 
#on one line and then print its meaning indented on a second line. Use the 
#newline character (\n) to insert a blank line between each word-meaning 
#pair in your output.

glossary = {
	'dictionary':'Python dictionaries are written with curly brackets, and they have keys and values.',
	'list':'List is a collection which is ordered and changeable.',
	'variable':'Variables are containers for storing data values.',
	'operator':'Operators are used to perform operations on variables and values.',
	'tuple':'A tuple is a collection which is ordered and unchangeable.'
}

for term in glossary:
	print(f'{term.title()}:')
	print(glossary[term] + '\n')