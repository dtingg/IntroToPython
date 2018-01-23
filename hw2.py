"""Assignment 2 by Dianna Tingg
Use math and string operations to create a Car Salesman program
"""

# Ask user for name, address, phone number (with hyphens), car make/model, purchase Price
user_first_name = input("What is your first name? ")
user_last_name = input("What is your last name? ")
user_address = input("What is your home address? ")
user_phone_number = input("What is your phone number? Enter as XXX-XXX-XXXX ")
car_make_model = input("What is the car make and model? ")
purchase_price = float(input("What is the purchase price? No commas or decimals: "))

# Add these values to the sale price: sales tax (% of sale price), licensing fee, dealer prep fee
sales_tax = .104 * purchase_price
licensing_fee = .03 * purchase_price
dealer_prep_fee = 150.00

# Calculate total cost (as a float)
total_price = float(purchase_price) + float(sales_tax) + float(licensing_fee) + float(dealer_prep_fee)

# Assign the car a unique ID (last four letters of user's last name + their area code, separated by _)
user_last_name_last_four = user_last_name[-4:]
user_area_code = user_phone_number.split("-")[0]
car_id = user_last_name_last_four.upper() + "_" + user_area_code

# Print out the information to the screen with the same line breaks as shown in the example

print("Hello " + user_first_name + " " + user_last_name + "!")
print("Thank you for your purchase of a " + car_make_model + ". Here is a breakdown of your total price:")
print("Sales Price: $" + "%.2f" % purchase_price)
print("Tax: $" + "%.2f" % sales_tax)
print("Licensing Fee: $" + "%.2f" % licensing_fee)
print("Dealer Prep Fee: $" + "%.2f" % dealer_prep_fee)
print("Total Price: $" + "%.2f" % total_price)
print("You have been assigned an ID number of " + car_id + ". Please reference this ID number if you have any questions.")

