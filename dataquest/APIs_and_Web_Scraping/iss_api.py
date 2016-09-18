#!/usr/bin/env python
"""
Application Program Interfaces (APIs) are used to dynamically query and retrieve data. They provide
a language whereby a client can retrieve information quickly and effectively. Reddit, Spotify,
Twitter, Facebook, and many other companies provide APIs that enable developers to access a wealth
of information stored on their servers.

Using APIs is more practical than using datasets in several circumstances:
* The data are changing quickly, such as stock price data
* You want a small piece of a much larger set of data, such as your own comments on Reddit
* There is repeated computation involved, such as using Spotify API to classify genre

In this mission, we'll be querying a simple API to retrieve data about the International Space
Station (ISS). Using an API will save us time and effort over doing all the computation ourselves.

APIs are hosted on web servers. When you type in www.google.com in your browser's address bar, your
computer is actually asking the www.google.com server for a webpage, which it then returns to your browser.

APIs work much the same way, except instead of your web browser asking for a webpage, your program
asks for data. This data is usually returned in json format.

In order to get the data, we make a request to the webserver that we want to get data from. The
server then replies with our data. In Python, we use the requests library to do this.

There are many different types of requests. The most commonly used one, a GET request, is used to
retrieve data. We'll get into the other types in later missions.

We can use a simple GET request to retrieve information on the International Space Station from the
OpenNotify API:  http://open-notify.org
"""
import datetime
import requests
import sys


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
if 200 != status_code:
    print("Error: status code = {}".format(status_code))
    sys.exit(1)

# Get the response data as a python dictionary
data = response.json()
iss_position = data['iss_position']
lat = iss_position['latitude']
lon = iss_position['longitude']
print("ISS latest position:  latitude={}  longitude={}".format(lat, lon))

# Finding the number of people currently in space
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
in_space_count = data['number']
print("Astronauts in space: {}".format(in_space_count))


# Passing parameters to an API
# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Getting JSON from a request
data = response.json()
first_pass = data['response'][0]
duration = first_pass['duration']
risetime = first_pass['risetime']
date_time = datetime.datetime.fromtimestamp(risetime)
str_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

# Print the content of the response (the data the server returned)
print("Next pass over NYC:  risetime={}  duration={}".format(str_time, duration))
