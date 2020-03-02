motorcycles = ["yamaha", "honda", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("yamaha")
print(motorcycles)

motorcycles.insert(2, "bmw")
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove("suzuki")
print(motorcycles)




