"""
Longmire actors and ages

User enters an actor's name from the Longmire TV show in order to find out what their age is.
These ages were calculated using year 2017.

"""
# Introduce the game
print('Welcome to the "Longmire" Actor Age Database! \n')

# Define two lists, make sure the values match up
actors = ["Walt", "Vic", "Henry", "Cady", "Ferg", "Ruby", "Branch", "Jacob", "Mathias", "Travis", "Malachi", "Zach", "Barlow", "Donna", "Meg", "Lucian", "David", "Hector", "Shane", "Ed"]

year_born = ["1963", "1980", "1962", "1982", "1979", "1939", "1972", "1948", "1966", "1976", "1952", "1981", "1947", "1961", "1985", "1947", "1962", "1963", "1965"]

age = []

for x in year_born:
  x = 2017 - int(x)
  age.append(x)

# Use the zip function to merge these lists, then add to a dictionary
longmire_tuples = list(zip(actors, age))
longmire_dict = dict(longmire_tuples)

# Ask the user to input a name
name_counter = 0

# Use a while loop to keep asking for a name until they find someone in the dictionary
# Give them up to five tries by using a counter outside the while loop
# Return the person's age
while name_counter < 5:
  entered_name = input('Please enter a "Longmire" character\'s first name to find out their age: ')
  entered_name = entered_name.title()
  if entered_name in longmire_dict:
    print("\n" + entered_name + " is " + str(longmire_dict[entered_name]) + " years old. \n")
    break
  else:
    print("\nThere is nobody here named " + entered_name + ", please try again. \n")
  name_counter += 1

print("Game Over")