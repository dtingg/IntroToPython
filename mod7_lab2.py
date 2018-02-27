"""Module 7 - Lab 2
We're going to practice installing, importing and using external python modules while learning out how to scrape web pages.
"""
# Import libraries
import requests
from bs4 import BeautifulSoup

# Scraping the web
# Set up our url as a string
url = "https://wiki.python.org/moin/IntroductoryBooks"

# Pull down all the html and store it in a page variable
response = requests.get(url)

# Returns a requests object
#print(response.headers)
content = response.content

# Parsing webpages
# Convert to beautifulsoup format
soup = BeautifulSoup(content, "html.parser")

# prettify to convert html to a more readable format
#print(soup.prettify())

# title tags
#print(soup.title)

# convert to a string
#print(soup.title.string)

# find all a tags
all_a = soup.find_all("a")

# use a for loop
#for x in all_a:
#    print(x)

# add a class argument to search within div tags
all_a_https = soup.find_all("a", "https")

#for x in all_a_https:
#    print(x)

# index this item like a list
print(all_a_https[0])

# loop through other metadata (attributes) that are nested inside the dev tag that we pulled out
for x in all_a_https:
    print(x.attrs["href"])

# use this info to make a dictionary of books and their links (Question)
data = {}
for a in all_a_https:
  title = a.string.strip()
  data[title] = a.attrs["href"]

print(data)

