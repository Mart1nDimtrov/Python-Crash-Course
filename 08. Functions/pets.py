def describe_pet(pet_name,animal_type='dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

#rewriting using keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')

#equivalent to first one
describe_pet(pet_name='harry',animal_type='hamster')

#use the default value for animal_type
describe_pet('willie')