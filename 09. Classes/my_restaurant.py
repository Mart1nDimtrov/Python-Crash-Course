from restaurant import Restaurant

#check to see if the Restaurant class is still called correctly
new_restaurant = Restaurant('Michelline','gourme')
print(f'Restaurant - {new_restaurant.name.title()}')
print(f'Cuisine type - {new_restaurant.cuisine_type}')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()