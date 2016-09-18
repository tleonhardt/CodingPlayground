#!/usr/bin/env python
"""
Example looking at answering a few interesting questions using the SQLite database from the CIA
World Factbook:
    * Which countries will lose population over the next 35 years?
    * Which countries have the lowest/highest population density?
    * Which countries receive the most immigrants? Which countries lose the most emigrants?
"""
import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('../data/factbook.db')

# Read the facts table into a Pandas DataFrame
query = 'select * from facts;'
facts = pd.read_sql_query(query, conn)

# Which countries will lose population over the next 35 years?

# Sort by population growth and print
lose_pop = facts[facts['population_growth'] < 0]

print("There are {} countries that will lose population!".format(len(lose_pop)))

# If this is true, it is a staggering fact, that NO countries have a negative population growth


# Which countries have the lowest/highest population density?
# Assumption:  population density = population / land_area

# First we need to drop any countries with a NaN or 0 land area_land
facts = facts[facts['area_land'].notnull() & facts['area_land'] != 0]
facts['pop_density'] = facts['population'] / facts['area_land']
lowest_density = facts.sort_values(by='pop_density', ascending=True)
highest_density = facts.sort_values(by='pop_density', ascending=False)
cols = ['name', 'pop_density']
N = 5
print("\nThe countries with the lowest population density are:\n{}".format(lowest_density[cols].head(N)))
print("\nThe countries with the highest population density are:\n{}".format(highest_density[cols].head(N)))
