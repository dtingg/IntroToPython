"""Module 6 - Lab 1 - Update a script to use functions
Taking what we learned about functions, take the following code and update it to use functions.
"""
# Create function that reads in the file and returns contents as a list
def file_list (file):
  with open(file) as f:
    lines = f.readlines()
  return lines

# Create a function that converts lines to a list of words
def line_words (list_of_lines):
  word_list = []
  for line in list_of_lines:
    word_list.extend(line.split(" "))
  return word_list

# Create a function to calculate the word count by using the word list and return the dictionary
def list_to_count(word_list):
  word_freq = {}
  for word in word_list:
    if word in word_freq:
      word_freq[word] = word_freq[word] + 1
    else:
      word_freq[word] = 1
  return word_freq

# Create function that calculates the min word freq and gets list of words from dictionary
def get_min_word(word_freq):
  min_word_freq = min(word_freq.values())
  min_words = []
  for word, fr in word_freq.items():
    if fr == min_word_freq:
      min_words.append(word)
  return min_word_freq, min_words

# Add main section
# call the functions file_list and line_words
if __name__ == '__main__':
  my_lines = file_list("./land_time_forgot.txt")
  my_list = line_words(my_lines)

# Create word set and print the sentence about unique words
word_set = set(my_list)
print("There are {} words in the book and {} of them are unique.".format(len(my_list), len(word_set)))

# call the function that calculates word count and find the word with max count
my_freq = list_to_count(my_list)
max_word = max(my_freq, key=my_freq.get)

print("Most frequent word is '{}' with frequency {}.".format(max_word, my_freq[max_word]))

# Call the min word function and print the results
mw_freq, mw_list = get_min_word(my_freq)
print("The lowest word frequency is {} and there are {} words in the book with that word frequency.".format(mw_freq, len(mw_list)))
