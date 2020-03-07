# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30.
# Use a for loop to print the numbers in your list.

multiples_3 = [x for x in range(1, 31) if x % 3 == 0]

for multiple in multiples_3:
    print(multiple)
