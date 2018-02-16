"""
Let's do some text analysis of Project Gutenberg's The Land That Time Forgot, by Edgar Rice Burroughs.
"""
# open file
with open("./land_time_forgot.txt") as f:

# read the file into a list
  infile = f.readlines()

# calculate the total number of lines in the file
  total_lines = len(infile)

# calculate the lines that are in 1/3 of the file
  one_third = int(total_lines / 3)

# store the middle third of the book's lines in a list
  middle_third_text = infile[(one_third):(one_third * 2)]

# print the number of lines in the file and the number of lines in the middle third of the book
  a = ("There are " + str(total_lines) + " total lines in the file and " + str(one_third) + " lines in the middle third of the book.")
  print(a)

# print the line that is 1/3 of hte way through the book and the line that is 2/3 of the way through the book
  b = (middle_third_text [0])
  print(b)

  c = (middle_third_text [-1])
  print(c)

# write the lines you printed above to a file
with open("output.txt", "w") as f:
  f.writelines([a, "\n", b, c])
