#9-3. Users:Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored 
#in a user profile. Make a method called describe_user() that prints a summary 
#of the user’s information. Make another method called greet_user() that prints 
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods 
#for each user.

#import the user class
from user import User


user_1 = User('nina', 'amis', 'naoya@yahoo.com')
user_2 = User('ull', 'man', 'ullman@yahoo.com')
user_3 = User('dave', 'miller', 'dmiller@yahoo.com')

user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()
print()
user_3.describe_user()
user_3.greet_user()
