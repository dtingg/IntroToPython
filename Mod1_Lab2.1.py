# ask the user to enter their name
user_name = input("What is your name? ")
user_name = user_name.title()

# ask the user to enter their favorite color
user_fav_color = input("What is your favorite color? ")
user_fav_color = user_fav_color.lower()

# print their name is xxx and their favorite color is xxx
print("Your name is " + user_name + " and your favorite color is " + user_fav_color + ".")

# tell them what my name is
print("My name is Dianna.")

# tell them what my favorite color is
print("My favorite color is green.")

# tell them that my favorite color is better than theirs or tell them we have the same favorite color
if user_fav_color == "green":
  print("We have the same favorite color!")
else:
  print("Green is better than " + user_fav_color + "!")