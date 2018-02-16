"""
Module 5 - Lab 2
Let's do more text analysis of the book: "The Land That Time Forgot."
"""
# open file and store contents in a list
with open("./land_time_forgot.txt") as f:
  lines = f.readlines()

# convert list of book lines into a list of words
  words = []

  for line in lines:
    x = line.split(" ")
    for word in x:
      words.append(word)

  total_words = len(words)

# print a sentence using format with the total number of words
print("This book contains a total of {} words.".format(total_words))

# use split to get the project_title and author from the first line
firstline = lines[0].strip()

# separate the projecttitle and author
projecttitle, author = firstline.split(", by ")

# separate the project and title
project, title = projecttitle.split("'s ")

# print the author, the title, and the project using format
print("The author is {}, the title is {}, and the project is {}.".format(author, title, project))