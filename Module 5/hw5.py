"""
Text analysis of the book "The Land That Time Forgot," by Edgar Rice Burroughs
"Users/dtingg/PycharmProjects/IntroToPython/land_time_forgot.txt"

"""
# Mention the book I'm using
print('Text analysis of the book "The Land That Time Forgot," by Edgar Rice Burroughs.')

# Read in the file and store it in a list
with open("./land_time_forgot.txt") as b:
    lines = b.readlines()

# Convert the list of book lines into a list of the words (Use a for loop and list.extend)
words = []
for l in lines:
    strip_line = l.strip().lower()
    no_punct = strip_line.replace('"', '').replace("  ", " ").replace(". ", " ").replace("!", "").replace("--",
                                                                                                          " ").replace(
        "; ", " ").replace("?", "").replace(", ", " ").replace(": ", " ").replace("(", "").replace(")", "")
    words.extend(no_punct.split(" "))

# Print a sentence using format with the total number of words and the unique number of words (use a set)
unique = set(words)
total_words = len(words)
unique_words = len(unique)

print("This book has {} total words and {} unique words.".format(total_words, unique_words))

# Calculate the word frequency. Use the list of all words and make a dictionary to count the number of times each word occurs.
word_dict = {}

for w in words:
    if w in word_dict:
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1

# Calculate the word with the maximum frequency (use max)
max_word = max(word_dict, key=word_dict.get)

print("The word \"{}\" has the maximum frequency. It appears {} times in this text.".format(max_word, word_dict[max_word]))

# Get the minimum frequency (use values)
min_freq = min(word_dict.values())

# Store all of the words that have the minimum frequency in a list(use a for loop and items)
min_words = []
for w, k in word_dict.items():
    if k == min_freq:
        min_words.append(w)

# Print a sentence of the minimum frequency and the number of words with that frequency
print("The minimum word frequency is {} and there are {} words with that frequency.".format(min_freq, len(min_words)))

# Print a sentence of the percentage of words that are unique in the book (use :.1f in your format)
unique_percent = float(len(unique)) / float(len(words)) * 100

print("The percentage of unique words in this book is {:.1f} percent.".format(unique_percent))
