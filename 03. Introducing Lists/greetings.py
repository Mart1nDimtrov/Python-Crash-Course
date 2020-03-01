# 3-2. Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name. 
friends = ["Peter","John","Mary"]
message = f"Hi"
for x in friends:
    print(message + f" {x}! How have you been?")
