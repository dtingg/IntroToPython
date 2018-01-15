# Useless Trivia
# Gets personal information from the user
# and prints true but uselss information about them

# Getting the user input
name = input("Hi. What is your name? ")

age = int(input("How old are you? "))

weight = int(input("Ok, last question. How many pounds do you weigh? "))

# Print lowercase and uppercase versions of name
print("\nIf poet ee cummings were to e-mail you, he'd address you as", name.lower())
print("But if ee were mad, he'd call you", name.upper())

# Printing name five times
called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

# Calculating seconds
seconds = age * 365 *24 * 60 * 60
print("\nYou're over", seconds, "seconds old.")

# Calculating moon weight and sun weight
moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only", moon_weight, "pounds?")
sun_weight = weight * 27.1
print("On the sun, you'd weigh", sun_weight, "(But, ah...not for long).")