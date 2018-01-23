"""
Using boolean logic and if statements as flow control, write a program that:

Assign a random number between 50 and 100 to a variable called test_num (read page 50-52 in your text)
If test_num is divisible by three, print "fizz"
If test_num is divisible by five, print "buzz"
if test_num is divisible by both three and five, print "fizzbuzz!"
"""

# Pick a random number between 50 and 100
import random
test_num = random.randint(50,100)
print(test_num)

# if test_num is divisible by both three and five, print "fizzbuzz!"
if test_num % 3 == 0 and test_num % 5 == 0:
    print("fizzbuzz")

elif test_num % 3 == 0:
    print("fizz")

elif test_num % 5 == 0:
    print("buzz")

else:
    print("Your number is not divisible by 3 or 5!")
