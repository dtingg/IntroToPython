# Car Salesman program
# user enters the base price of a car
# add on extra fees (tax, license, dealer prep, destination charge
# tax and license are a percentage of the base price
# display the actual price of the car with all of the fees added

base_price = float(input("What is the base price for the car? "))
tax = round(base_price * .104, 2)
license = round(base_price * .05, 2)
dealer_prep = 150.00
dest_charge = 500.00
total_car = base_price + tax + license + dealer_prep + dest_charge

print("Base price", base_price)
print("Tax", tax)
print("License fee", license)
print("Dealer Prep Fee", dealer_prep)
print("Destination Charge", dest_charge)
print("Total", total_car)