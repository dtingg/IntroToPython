"""
Ask the user to enter a starting and ending number
The user must not enter a starting number less than 1
The user must enter an ending number at least 5 times greater than the starting number
Create checks and error messages for the above
Create a list of integers in the range of the user's starting and ending numbers
Print out the number and index of each item in the list that is even
Sum all the odd numbers in the list using a for loop ( hint: append odd numbers to a list and then sum() that list )
Print out the cumulative sum calculated above

"""

# Ask the user to enter a starting number (make sure it is not less than 1)
start_num = 0

while start_num < 1:
  start_num = input("Pick a starting number (Integer, 1 or higher): ")
  start_num = int(start_num)

# Ask the user to enter an ending number (at least 5x greater than starting number)
end_num = 0

while end_num < 5 * start_num:
    end_num = input("Pick an ending number at least 5x your starting number : ")
    end_num = int(end_num)

# Create a list of integers in the range of the user's starting and ending numbers
numbers = list(range(int(start_num), int(end_num)))

# For even numbers, print out the number and index of each item in the list
print("\nEven numbers in your list:")

for index, x in enumerate(numbers):
  if x % 2 == 0:
    print ("{} is at index {}".format(str(x), str(index)))

# For the odd numbers, find the sum using a for loop (append odd numbers to a list and then sum () that list
odd_numbers = []
for x in numbers:
  if x % 2 != 0:
    odd_numbers.append(x)

sum_odd_numbers = sum(odd_numbers)

print("\nThe sum of the odd numbers in your list: " + str(sum_odd_numbers))

# Print the cumulative sum (sum of entire number list)
print("\nThe cumulative sum of all the numbers in your list: " + str(sum(numbers)))

# Add fizzbuzz!
print("\nFizzbuzz test!")
for x in numbers:
  if x % 3 == 0 and x % 5 == 0:
    print(str(x) + " = Fizzbuzz")
  elif x % 3 == 0:
    print(str(x) + " = Fizz")
  elif x % 5 == 0:
    print(str(x) + " = Buzz")
  else:
    print(str(x) + " = Not divisible by 3 or 5")

