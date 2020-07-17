#9-8. Privileges: Write a separate Privileges class. The class should have one 
#attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance 
#as an attribute in the Adminclass. Create a new instance of Admina nd use your 
#method to show its privileges.

from admin import Admin

user_1 = Admin('nina', 'amis', 'naoya@yahoo.com')
user_1.describe_user()
user_1.privileges.show_privileges()