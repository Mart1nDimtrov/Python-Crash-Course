# 3-10. Every Function: Think of something you could store in a list. For example, 
# you could make a list of mountains, rivers, countries, cities, languages, 
# or anything else you’d like. Write a program that creates a list containing these items 
# and then uses each function introduced in this chapter at least once

rivers = ["indus","nile","mississippi","amazon"]
print(rivers)

rivers.append("thames")
print(rivers)

rivers.insert(1,"bistritsa")
print(rivers)

print(rivers.pop())

del rivers[0]
print(rivers)

rivers.remove("mississippi")
print(rivers)

print(f"The count of rivers in the list is: {len(rivers)}")