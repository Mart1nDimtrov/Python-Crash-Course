# 4-5. Summing a Million:
# Make a list of the numbers from one to one million, and then use min() and max()
# to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.

long_numbers = [x for x in range(1, 1000_001)]

print(f"Max number: {max(long_numbers)}")
print(f"Min number: {min(long_numbers)}")
print(f"Sum: {sum(long_numbers)}")
