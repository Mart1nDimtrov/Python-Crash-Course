#import the Car class from the car module
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#set the value of the odometer_reading attribute directly 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#set the value of the odometer_reading attribute through a method 
my_new_car.update_odometer(22)
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(-100)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()