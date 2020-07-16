#import IceCreamStand from a module
from ice_cream_stand import IceCreamStand

#check to see if the IceCreamStand class still works
new_restaurant = IceCreamStand('Raffy','ice cream')
print(f'Restaurant - {new_restaurant.name.title()}')
print(f'Cuisine type - {new_restaurant.cuisine_type}')
new_restaurant.list_flavors()