"""
we're going to create a list of names to group by length, and then count how many names occur in each group.
Create the following name list and add in at least five female names (with repeats) to support women in tech!
names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl',
 'luke', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']
Create an empty dictionary to store your values
Create a for loop that iterates through the names to add each one to the dictionary along with a count
"""

# Create a name list and add at least 5 female names (with repeats)
names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl',
 'luke', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew',
'dianna', 'dana', 'heidi', 'dianna', 'quyen']

# Create an empty dictionary to store your values
name_dict = {}

# Create a for loop that iterates through the names to add each one to the dictionary along with a count
for name in names:
    if name in name_dict:
        name_dict[name] += 1
    else:
        name_dict[name] = 1

print(name_dict)


