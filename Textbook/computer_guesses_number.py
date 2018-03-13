"""Computer Guesses My Number Game
Player enters a random number between 1 and 100 and the computer has to guess it"""

# Introduce the Game
print("Computer Guesses Your Number")

# User enters a number between 1 and 100
user_num = input("\nEnter a number between 1 and 100.  I won't peek! ")
user_num = int(user_num)

high = 100
low = 1
guess = 0

while guess != user_num:
  guess = (high + low)//2
  print("I guess " + str(guess))
  if guess > user_num:
    high = guess
  elif guess < user_num:
    low = guess
print("I guessed " + str(guess) + ". I win!")
