"""
Create variables to store user input for:
User name
User phone number
Favorite cheese
Average monthly amount spent on their favorite cheese
Calculate the daily amount this user spends on cheese and store this value as a variable
Use the string split() method to store the last four digits of the user's phone number as a variable
Use the string slicing method to store the first three letters of the user's name as a variable
Combine the phone number and username variables to create an account ID
Use the replace() method to replace the first letter of your User ID with a Z and store that value as the final user ID
Print out a string telling the user what their account ID is, and letting them know what their daily cheese spending habits look like.
Feel free to add as much snark as you want.
Make sure your script runs, and upload the python script here.
"""

# Create variables to store user input for user name, user phone number, fav cheese, avg monthly amount spent on cheese
user_name = input("What is your name? ")
user_phone_number = input("What is your phone number? ")
favorite_cheese = input("What is your favorite cheese? ")
avg_monthly_cost = float(input("On average, how much do you spend per month on your favorite cheese? $"))

# Calculate daily amount spent on favorite cheese
avg_daily_amt = float(avg_monthly_cost)/30


# Store last four digits of the user's phone number
user_phone_number_pieces = user_phone_number.split("-")
user_phone_number_last_four = user_phone_number_pieces[2]

# Store the first three letters of the user's name
user_name_first_three = user_name[0:3]

# Combine the phone number and username to create an account id
account_id = user_phone_number_last_four + user_name_first_three.upper()

# Replace first letter of user id with a Z and store as final user ID
final_account_id = account_id.replace(account_id[0], "Z")

# Tell user what their account id is and let them know what their daily cheese spending habits look like.
print("Hi " + user_name + ". Your account id is " + final_account_id + ". You spend about $" + "%.2f" % avg_daily_amt\
      + " per day on " + favorite_cheese + "!")