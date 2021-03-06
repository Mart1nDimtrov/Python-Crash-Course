#5-1. Conditional Tests:Write a series of conditional tests. Print a statement 
#describing each test and your prediction for the results of each test. Your code 
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#•	 Look closely at your results, and make sure you understand why each line 
#evaluates to True or False.
#•	 Create at least ten tests. Have at least five tests evaluate to True and 
#another five tests evaluate to False.
#5-2. More Conditional Tests:You don’t have to limit the number of tests you 
#create to ten. If you want to try more comparisons, write more tests and add 
#them to conditional_tests.py. Have at least one Trueand one False result for 
#each of the following:
#•	 Tests for equality and inequality with strings
#•	 Tests using the lower()method
#•	 Numerical tests involving equality and inequality, greater than and 
#less than, greater than or equal to, and less than or equal to
#•	 Tests using the and keyword and the or keyword
#•	 Test whether an item is in a list
#•	 Test whether an item is not in a list

tv = 'on'
print("Is tv on? I predict True.")
print(tv == 'on')
print("\nIs tv off? I predict False.")
print(tv == 'off')

tv = 1
print("\nIs tv on? I predict True.")
print(tv == 1)
print("\nIs tv off? I predict False.")
print(tv == 0)

tv = True
print("\nIs tv on? I predict True.")
print(tv == 1)
print("\nIs tv off? I predict False.")
print(tv == 0)

tv = False
print("\nIs tv on? I predict False.")
print(tv == True)
print("\nIs tv off? I predict True.")
print(tv == False)

site_online = 0
print("\nIs site online? I predict False.")
print(site_online == 1)
print("\nIs site offline? I predict True.")
print(site_online == 0)

channel = 'amc'
print("\nIs channel AMC? I predict True.")
print(channel.lower() == 'amc')
print("\nIs channel NBC? I predict False.")
print(channel.lower() == 'nbc')

lucky_num = 7
print("\nIs your lucky number 6 or 7? I predict True.")
print(lucky_num == 7 or lucky_num == 6)
print("\nIs your lucky number 8 or 9? I predict False.")
print(lucky_num == 9 or lucky_num == 9)

foods = ['burger','pizza','spaghetti']
print("\nIs spaghetti in the list of foods? I predict True.")
print('spaghetti' in foods)
print("\nIs pastrami in the list of foods? I predict False.")
print('pastrami' in foods)




