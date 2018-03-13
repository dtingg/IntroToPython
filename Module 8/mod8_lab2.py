"""Module 8 - Lab 2
When you try to open a file that doesn't exist on your file system the open function raises a nice error called FileNotFoundError
"""

# Open a non-existant file location
# open ("unicorn.txt", "r")

# use try/except to handle the FileNotFoundError and output a nicer message for the user about what happened

try:
   file = open("unicorn.txt", "r")
except FileNotFoundError:
   print("Sorry, this file does not exist.")

# Let's say some other type of error happens but we don't know the specifc name of it. How can our try/except handle this?
except Exception as e:
    print("Sorry, a {} error occurred.".format(e))
    raise SystemExit
