"""
Module 7 - Lab 1

list1 = [ [1,2,3], ['a','b'] ]
print(list1)
list2 = list1
print(list2)

Q1. What does list1 and list2 contain?
They both contain: [[1, 2, 3], ['a', 'b']]

Q2. What space in memory have list1 and list2 been assigned to? Are they the same?
They are both stored at: 2199833186952
print(id(list1))
print(id(list2))

setting an element to a new value
list1[0] = [5,6,7]

Q3. Now what do list1 and list2 contain? What happened?
print(list1)
print(list2)

They both contain: [[5, 6, 7], ['a', 'b']] since list 2 was only pointing to list 1

Let's properly copy the list, using slicing syntax:
list2 = list1[:]

Q4. What does [:] in the above statement mean?
[:} means make a copy of list1 from beginning to end

Now we'll update a mutable element of list1:
list1[0] = [2,4,6]

Q5. What do list1 and list2 contain now? Why? (Hint, check the memory space each item has been assigned to).
print(list1)
print(id(list1))

print(list2)
print(id(list2))

List1 is [[2, 4, 6], ['a', 'b']] and stored at 1247286170248
List2 is [[5, 6, 7], ['a', 'b']] and stored at 1247286172104

But what happens if we update the list itself?
list1[1].append('c')

Q6. What do list1 and list2 contain now? Why?
print(list1)
print(id(list1))
print(list2)
print(id(list2))

List1 is [[2, 4, 6], ['a', 'b', 'c']]
List 2 is [[5, 6, 7], ['a', 'b', 'c']]
This probably happened because it was only a shallow copy?
"""

# Q7. Post your code for the following steps:
# Following the instructions from the lecture, make list2 a deep copy of list1.
from copy import deepcopy
list1 = [ [1,2,3], ['a','b'] ]
list2 = deepcopy(list1)

# Append the letter "x" to list1
list1.append("x")

print(list1)
print(list2)

# Report what list1 and list2 now contain
# List 1: [[1, 2, 3], ['a', 'b'], 'x']
# List 2: [[1, 2, 3], ['a', 'b']]






