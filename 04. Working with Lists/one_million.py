# 4-4. One Million: Make a list of the numbers from one to one million,
# and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

long_numbers = [x for x in range(1, 1000_001)]

for number in long_numbers:
    print(number)
