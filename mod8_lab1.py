"""
Module 8 - Lab 1
For this lab we're going to create a calculator:
"""
# Create a class called "Calculate"
class Calculate():

# Instantiate the class and use each method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Your numbers are {} and {}.".format(x, y))

# Add methods to add, subtract, divide and multiply two numbers
    def add(self, x, y):
        num = x + y
        return num

    def subtract(self, x, y):
        num = x - y
        return num

    def divide(self, x, y):
        num = x / y
        return num

    def multiply(self, x, y):
        num = x * y
        return num

numbers = Calculate(2, 8)
print("Addition = {}.".format(numbers.add(2,8)))
print("Subtraction = {}.".format(numbers.subtract(2,8)))
print("Division = {}.".format(numbers.divide(2,8)))
print("Multiplication = {}.".format(numbers.multiply(2,8)))

"""
Alternative Method:
Module 8 - Lab 1
For this lab we're going to create a calculator:

# Create a class called "Calculate"
class Calculate():

# Instantiate the class and use each method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Your numbers are {} and {}.".format(x, y))

# Add methods to add, subtract, divide and multiply two numbers
    def add(self):
        num = self.x + self.y
        return num

    def subtract(self):
        num = self.x - self.y
        return num

    def divide(self):
        num = self.x / self.y
        return num

    def multiply(self):
        num = self.x * self.y
        return num

numbers = Calculate(2, 8)
print("Addition = {}.".format(numbers.add()))
print("Subtraction = {}.".format(numbers.subtract()))
print("Division = {}.".format(numbers.divide()))
print("Multiplication = {}.".format(numbers.multiply()))
"""