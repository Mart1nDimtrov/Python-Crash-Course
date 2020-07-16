#9-2. Three Restaurants:Start with your class from Exercise 9-1. Create three 
#different instances from the class, and call describe_restaurant() for each 
#instance.

#call the restaurant class from a module
from restaurant import Restaurant

restaurant_1 = Restaurant('La Pergola','italian')
restaurant_2 = Restaurant('Sushi Ueda','sushi')
restaurant_3 = Restaurant('Azurmendi','mediterranean')

restaurant_1.describe_restaurant()
print()
restaurant_2.describe_restaurant()
print()
restaurant_3.describe_restaurant()
