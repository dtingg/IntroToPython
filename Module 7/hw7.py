"""
Assignment 7
Use the tutorial from Module 7 Lab 2.
Requires Requests and BeautifulSoup modules
"""

# Import libraries
import requests
from bs4 import BeautifulSoup

# Create a function that pulls out a specific tag from a url
def get_tags(url, tag):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    all_usertags = soup.find_all(tag)
    return all_usertags

# Create a function to format the output in a meaningful way
def format(output):
    list = []
    for tag in output:
        list.append("Tag attributes are: " + str(tag.attrs))
    return list

# Create a function to write the formatted results to a text file
def write_file(formatted):
    with open("web_output.txt", "w", encoding="utf-8") as f:
        for item in formatted:
            f.write(item + "\n")

# Create a main function that allows the script to be run on its own from the command line
if __name__ == "__main__":

    # Introduce the program
    print("Welcome to Dianna's Web Scraper Program!")

    # Ask the user to enter a URL
    url = input("Please enter a URL: ")

    # Ask the user to enter a type of HTML tag
    tag = input("Please enter a type of HTML tag to search for: ")

    output = get_tags(url, tag)

    while output == []:
        tag = input("There are no tags like that in your website. Please enter a different tag: ")
        output = get_tags(url, tag)

    formatted = format(output)
    file = write_file(formatted)

    # Tell the user where the output is
    # test url was "https://en.wikipedia.org/wiki/List_of_counties_in_Washington" and test tag was "a"
    print("Your output is listed in the file web_output.txt.")
