"""
Module 5 - Lab 3
Let's do some analysis of the Seattle Wage Data CSV file
"""

# read in the CSV file using csv.reader
import csv

with open("./City_of_Seattle_Wage_Data.csv") as f:
    reader = csv.reader(f)

    # store the header line in a variable using next
    header = next(reader)

    # create a dictionary to store the list of "Hourly Rate" by job title
    salary_dict = dict()

    for row in reader:
        if row[3] in salary_dict and row[4] not in salary_dict[row[3]]:
            salary_dict[row[3]].append(row[4])
        elif row[3] in salary_dict and row[4] in salary_dict[row[3]]:
            continue
        else:
            salary_dict[row[3]] = [row[4]]

# write the dictionary to a file

with open("salary_dict.txt", "w") as outfile:
    for job, salary in salary_dict.items():
        outfile.writelines("{}:{}".format(job, salary))
        outfile.write("\n")