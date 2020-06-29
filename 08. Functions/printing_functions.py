#8-15. Printing Models:Put the functions for the example printing_models.py in a 
#separate file called printing_functions.py. Write an importstatement at the top 
#of printing_models.py, and modify the file to use the imported functions.
def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print('The following models have been printed:')
	for model in completed_models:
		print(model)

def print_models(unprinted_designs,completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		model = unprinted_designs.pop()
		print(f'Printing model: {model}')
		completed_models.append(model)