"""Coin Flipping Program
Flip a coin 100 times and print the number of heads and tails"""

# Import random module
import random

# Set starting values as 0
heads, tails, times_flipped = 0, 0, 0

# Use a while loop
while times_flipped < 100:
    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        heads += 1
    else:
        tails += 1
    times_flipped += 1

# Print the results
print("Out of 100 flips, " + str(heads) + " were heads and " + str(tails) + " were tails.")