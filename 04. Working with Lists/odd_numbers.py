# 4-6. Odd Numbers: Use the third argument
# of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

odd_numbers = [x for x in range(1, 22, 2)]

for odd in odd_numbers:
    print(odd)
