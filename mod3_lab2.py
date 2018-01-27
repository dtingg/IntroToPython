"""Module 3 - Lab 2
Guess that Animal!
Make a word guess game of your favorite animals.

Create a list of animals.
A user gets a number of guesses equal to 3 plus:
   length of the unique letters in the longest animal name
Use a while loop to get user input until they run out of guesses
Use a list comprehension to output the currently matching letters of the animal
"""

#make a variable with an animal name
animal="cat"
#find the unique letters
aset = set(animal)
#give the user letters + 3 guesses
num_guess = len(aset) + 3
#store the guesses
guessed_letters = set()

#get user input
counter = 0
while counter < num_guess:
    guess = input("You have {} guesses remanining. What is your next letter?".format(num_guess))
    if guess in guessed_letters:
        guess = input("You already guessed that! Try again!")
    guessed_letters.add(guess)

# print out the matches
for letter in animal:
    if letter in guessed_letters:
        print(letter)
    else:
        print("-")

#compare each guess to the unique letters

counter = counter +1

union