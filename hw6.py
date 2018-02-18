"""
Assignment 06 - Pizza Functions
Taking what we learned about functions, create a python script that will calculate the cost of pizza for movie night.
"""
# Introduce the program
print("Welcome to Dianna's Pizza Program!")

# Get user input for the number of people who want pizza and avg number of slices per person
people = int(input("How many people want pizza? "))
avg_slices = int(input("What is the average number of slices per person? "))

# Create static variables for pizza cost, slices per pizza, delivery fee, tax rate, and tip rate
pizza_cost = 14.99
slices_per_pizza = 8
delivery_fee = 3.00
tax_rate = .101
tip_rate = .20

# Write a function to calculate how many pizzas to order based on number of people and avg slices
def pizza_order (people, avg_slices):
    slices_needed = people * avg_slices
    if slices_needed % 8 == 0:
        pizzas_needed = int(slices_needed / 8)
    else:
        pizzas_needed = (slices_needed // 8) + 1
    return pizzas_needed

pizzas = pizza_order(people, avg_slices)

print("Large pizzas cost ${} and have {} slices, so you need to order {} pizzas.".format(pizza_cost, slices_per_pizza, pizzas))

# Write a function to determine total pizza cost including delivery fee, tax, and tip
def total_pizza_cost (pizzas):
    pizza_price = pizzas * pizza_cost
    pizza_price += delivery_fee
    pizza_price += (pizza_price * tax_rate)
    pizza_price += (pizza_price * tip_rate)
    return pizza_price

total_price = total_pizza_cost(pizzas)

print("The total pizza price (including ${} delivery fee, {}% sales tax, and a {}% tip) is: ${}.".format("%.2f" % delivery_fee, "%.1f" % (tax_rate*100), "%.1f" % (tip_rate*100), "%.2f" % total_price))

# Write a function to determine the cost per person.
def price_per_person (total_price, people):
   price_per_person = total_price / people
   return price_per_person
each_person = "%.2f" % price_per_person(total_price, people)

if float(each_person) * int(people) < total_price:
    each_person = float(each_person) + .01

print ("Each person owes ${}.".format(each_person))
