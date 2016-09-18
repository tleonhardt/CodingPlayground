#!/usr/bin/env python
"""
There is a lot of data that doesn't exist in dataset or API form. A lot of this data is present on
the internet, in webpages we interact with. One way to access this data without waiting for the
provider to create an API is to use a technique called web scraping.

Web scraping allows us to load a webpage into Python, and extract the information we want. We can
then work with the data using normal data analysis tools, like pandas and numpy.

In order to perform web scraping, we need to understand the structure of the webpage that we're
working with, then find a way to extract parts of that structure in a sensible way.

As we learn about web scraping, we'll be heavily using the requests library, which enables us to
download a webpage, and the beautifulsoup library, which enables us to extract the relevant parts
 of a webpage.

Webpages are coded in HyperText Markup Language (HTML). HTML is not a programming language, like
Python, but it is a markup language, and has its own syntax and rules. When a web browser, like
Chrome or Firefox, downloads a webpage, it reads the HTML to know how to render the webpage and
display it to you.
"""
import requests
from bs4 import BeautifulSoup


# Make a GET request to get a very simple webpage
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content
print(content)


## Retrieving elements from a page
# Downloading the page is the easy part. Let's say that we want to get the text in the first
# paragraph. Now we need to parse the page and extract the information that we want.
#
# In order to parse the webpage with python, we'll use the BeautifulSoup library. This library
# allows us to extract tags from an HTML document.
#
# HTML documents can be thought of as trees due to how tags are nested, and BeautifulSoup works the same way.

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With beautifulsoup, we can access branches by simply using tag types as
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text of the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

# Get the text intside the title tag
head = parser.head
title_text = head.title.text
print("Title = '{}'".format(title_text))


## Using Find All
# While it's nice to use the tag type as a property, it doesn't always lead to a very robust way to
# parse a document. Usually, it's better to be more explicit and use the find_all method. find_all
# will find all occurences of a tag in the current element.
#
# find_all will return a list. If we want only the first occurence of an item, we'll need to index
# the list to get it. Other than that, it behaves the same way as passing the tag type as an attribute.

# Use the find_all method to get the text inside the title tage
head = parser.find_all("head")
title = head[0].find_all("title")
title_text = title[0].text


## Element Ids
# HTML allows elements to have ids. These ids are unique, and can be used to refer to a specific element.

# Get the page content and setup a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the id attribute to only get elements with a certain id.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

# Get the text of the 2nd paragraph
second_paragraph_text = parser.find_all("p", id="second")[0].text
print(second_paragraph_text)


## Element Classes
# HTML also enables elements to have classes. Classes aren't globally unique, and usually indicate
# that elements are linked. All elements with the same class usually share some kind of characteristic
# that leads the author of the page to group them into the same class. One element can have multiple classes.
#
# Classes and ids make pages easier to style with CSS.

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

# Get the texst of the second inner paragraph
second_inner_paragraph_text = parser.find_all("p", class_="inner-text")[1].text
print(second_inner_paragraph_text)

# Get the text of the first outer paragrpah
first_outer_paragraph_text = parser.find_all("p", class_="outer-text")[0].text
print(first_outer_paragraph_text)


## CSS Selectors
# Cascading Style Sheets, or CSS, is a way to add style to HTML pages. You may have noticed that our
# simple HTML pages in the past few screens didn't have any styling -- the paragraphs were all black
# in color, and the same font size. Most web pages don't only consist of black text. The way that
# webpages are styled is through CSS. CSS uses selectors that select elements and classes of elements
# to decide where to add certain stylistic touches, like color and font size changes.
#
# With BeautifulSoup, we can use CSS selectors very easily. We just use the .select method.
# Get the website that contains classes and ids
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all the elements with the first-item class
first_items = parser.select(".first-item")

# Print the text of the first paragraph (first element with the first-item class)
print(first_items[0].text)

# Select all the elements with the outer-text class
outer_items = parser.select(".outer-text")
first_outer_text = outer_items[0].text
print(first_outer_text)

# Select all othe elements with te second id
second_items = parser.select("#second")
second_text = second_items[0].text
print(second_text)


## Nesting CSS Selectors
# Just like how HTML has nested tags, we can also nest CSS Selectors to select items that are nested.
# So we could use CSS selectors to find all of the paragraphs inside the body tag, for instance.
# Nesting is a very powerful technique that enables us to use CSS to do complex web scraping tasks.
#
# This CSS Selector will select any paragraphs inside a div tag:
#    div p

# Get the super bowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers committed by the Seahawks.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print("Seahawks turnovers count = {}".format(seahawks_turnovers_count))

patriots_total_plays_count = parser.select("#total-plays td")[2].text
print("Total Plays for the New England Patriots = {}".format(patriots_total_plays_count))

# Fidn the Total Yards for the Seahawks
seahawks_total_yards_count = parser.select("#total-yards td")[1].text
print("Total Yards for the Seahawks = {}".format(seahawks_total_yards_count))
