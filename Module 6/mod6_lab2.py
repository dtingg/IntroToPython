"""
Mod 6 Lab 2
Practicing with Git Bash and Python

# Git Bash
mkdir testing
cd testing
touch test.txt
ls
>>
test.txt
echo "line1" >> test.txt
echo "line2" >> test.txt
echo "line3" >> test.txt
echo "line4" >> test.txt
echo "line5" >> test.txt
echo "line6" >> test.txt
echo "line7" >> test.txt
echo "line8" >> test.txt
echo "line9" >> test.txt
echo "line10" >> test.txt
head -n 3 test.txt
>>
line1
line2
line3
tail -n 5 test.txt
>>
line6
line7
line8
line9
line10
"""
# Practice with Python

import os

os.chdir("/Users/dtingg/Documents")

# Count number of word and pdf files in documents folder
for file in os.listdir():
    num_docs = []
    if file.endswith(".doc") or file.endswith(".pdf"):
        num_docs.append(file)
    else:
        continue

print("There are " + str(len(num_docs)) + " Word or PDF files in the documents folder.")

# count number of subdirectories in documents folder
directories = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        directories.append(os.path.join(root, name))

print(directories)
print("There are " + str(len(directories)) + " subdirectories in the documents folder.")
