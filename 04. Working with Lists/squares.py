squares = []

for x in range(1,11):
	squares.append(x**2)

print(squares)

# use list comprehensions
squares_2 = [x**2 for x in range(1,11)]
print(squares_2)
