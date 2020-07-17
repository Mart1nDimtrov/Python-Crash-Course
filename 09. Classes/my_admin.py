#9 - 7. Admin:An administrator is a special kind of user. Write a class called 
#Adminthat inherits from the User class you wrote in Exercise 9-3 (page 162) 
#or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
#of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of 
#privileges. Create an instance of Admin, and call your method.

#import tha Admin class
from admin import Admin

user_1 = Admin('nina', 'amis', 'naoya@yahoo.com')
user_1.describe_user()
user_1.show_privileges()