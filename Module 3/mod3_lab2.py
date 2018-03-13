"""Guess that Animal! Make a word guess game of your favorite animals.
Create a list of animals.
A user gets a number of guesses equal to 3 plus:
   length of the unique letters in the longest animal name
Use a while loop to get user input until they run out of guesses
Use a list comprehension to output the currently matching letters of the animal"""

# Select my favorite animal
fav_animal = "shark"

# Set guess counter to 0.
guess_counter = 0

# Change favorite animal into a set of unique letters
actual_letters = set(fav_animal)

# Create a set for guessed letters
guessed_letters = set()

# User gets number of guesses equal to 3 + number of unique letters in animal name
num_guesses = 3 + len(set(fav_animal))

# Introduce the name of the game
print("Guess my favorite animal!")

# Use a while loop to get user input until they run out of guesses
while guess_counter < num_guesses:
    user_guess = input("Pick a letter: ")
    guessed_letters.add(user_guess)
    if user_guess in actual_letters:
        print("Yes! "+ user_guess + " is in the name of my favorite animal.")
    else:
        print("Sorry!")
    print("Here are the correct letters so far: ", actual_letters.intersection(guessed_letters))
    guess_counter += 1
