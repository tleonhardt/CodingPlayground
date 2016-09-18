#!/usr/bin/env python
"""
Example showing how to use SQL SUM() function in a query.
"""
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('../data/factbook.db')
curr = conn.cursor()

# Query to get the total of the area_land column
query = 'SELECT SUM(area_land) FROM facts WHERE area_land != ""'
curr.execute(query)
area_land = curr.fetchone()[0]

# Query to get the total of the area_water column
query = 'SELECT SUM(area_water) FROM facts WHERE area_water != ""'
curr.execute(query)
area_water = curr.fetchone()[0]

ratio = area_land / area_water
print("Ratio of country land area to water area = {}".format(ratio))
