# Assignment 05 - Word Frequency
* [Browse to a free copy of "The Land That Time Forgot"](https://ia800301.us.archive.org/13/items/thelandthattimef00551gut/551.txt) (or a different book)  
* Right-click on your browser
* Select "save as"
* Save as a .txt file
* Read in the file and store in a list
* Convert the list of book lines into a list of the words (hint: use a for loop and list.extend)

For this homework:
* Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
* Calculate the word (Links to an external site.)Links to an external site. frequency (Links to an external site.)Links to an external site..  There are many ways to calculate this.  Here are two examples:
    * Option 1:  Using the list of all words in the text, use a dictionary to count the number of times each word occurs (hint: see the section "Counting with Dictionaries" from this lecture: https://canvas.uw.edu/courses/1157528/pages/dictionaries?module_item_id=7642690).  Then use another for loop to calculate the frequency (# of words / total number of words).
    * Option 2: using the word list, the word set, and a for loop with list.count (Links to an external site.)Links to an external site. and store it in a dictionary (hint: don't forget to use float)
* Calculate the word with the maximum frequency (hint: use max (Links to an external site.)Links to an external site.)
* Get the minimum frequency (hint: use values (Links to an external site.)Links to an external site.)
* Store all of the words that have the minimum frequency in a list (hint: use a for loop and items (Links to an external site.)Links to an external site.)
* Print a sentence of the minimum frequency and the number of words with that frequency
* Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)

**Stretch goals:** 
What are the trade offs between option 1 and option 2 for calculating the word frequency?

**List Comprehension**
Use a list comprehension to find the words that have the minimum frequency

**Expression Matching**
You can use python's built in re module to search through text to find strings that match a desired pattern (or word), called regular expressions.

https://www.youtube.com/watch?v=EppQdkv4G2w

Stretch Goal 1:
Find all lines that contain the word smoke using the following regular expression and print them to a file

> import re
> 
> text = open("land_time_forgot.txt", "r")
> 
> for line in text:
>     if re.match("(.*)(S|s)moke(.*)", line):
>         print(line)

This regular expression will match all lines that contain either Smoke or smoke.

Read the tutorial on python regular expressions:

https://docs.python.org/3/howto/regex.html 

Stretch Goal 2:
Add another regular expression to count the number of times the word 'now' is used in the book.  

Stretch Goal 3:
Add another regular expression to count the number of times there is dialogue in the book - words separated by double quotes.

 