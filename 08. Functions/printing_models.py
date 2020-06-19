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

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)