"""Guess My Number Game
User will try to guess my random number"""

# Introduce the game
print("Guess My Number!")

# Computer picks a random number
import random
number = random.randint(1,100)

# User tries to guess number
# Computer will keep track of number of guesses

guess_counter = 1
num_guess = ""

while guess_counter < 6:
    num_guess = input("\nGuess a number between 1 and 100. You have " + str(6-guess_counter) + " tries left: ")
    num_guess = int(num_guess)

    if num_guess == number:
        print("Wow! You guessed it! It took you " + str(guess_counter) + " tries.")
        break
    elif num_guess < number:
        print("No. My number is higher.")
    elif num_guess > number:
        print("No. My number is lower.")
    guess_counter += 1

print("\nMy number was " + str(number) + "\nGame Over")