"""Fortune Cookie Program
Display 5 unique fortunes, at random, each time program is run"""

# Introduce program
print("Welcome to the Virtual Fortune Cookie!")
print("\nYour fortune is: ")

# Get a random number between 1 and 5
import random


# Use a while loop to give out fortunes
go_again = "Yes"

while go_again == "Yes":
    number = random.randint(1, 6)

    if number == 1:
        print("The fortune you seek is in another cookie.")

    elif number == 2:
        print("You love Chinese food.")

    elif number == 3:
        print("Help! I am being held prisoner in a fortune cookie factory.")

    elif number == 4:
        print("This cookie contains 117 calories.")

    elif number == 5:
        print("You will be hungry again in one hour.")

    go_again = input("\nDo you want to try again? Yes or No: ")

