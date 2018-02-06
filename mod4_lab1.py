"""Given the following two sentences, determine:

The number of unique words in each sentence
The number of words that appear in both sentences
The number of words that are contained in either one sentence or the other, but not in both

For an extra challenge, can you figure out how to remove all the punctuation from the sentences before turning them into a set? See here (Links to an external site.)Links to an external site. for some help.
"""

# Sample sentences
s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons."
s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish."

# Determine number of unique words in each sentence
s1_unique_words = set(s1.split(" "))
print("Sentence 1 has " + str(len(s1_unique_words)) + " unique words in it.")

s2_unique_words = set (s2.split(" "))
print("Sentence 2 has " + str(len(s2_unique_words)) + " unique words in it.")

# Determine number of words that appear in both sentences
words_in_both = s1_unique_words.intersection(s2_unique_words)
print("There are " + str(len(words_in_both)) + " words that appear in both sentences.")

# Determine number of words that are contained in either one sentence or the other, but not both
words_in_either = s1_unique_words.symmetric_difference(s2_unique_words)
print("There are " + str(len(words_in_either)) + " words that appear in one sentence or the other, but not both.")