#!/usr/bin/env python
"""
Example showing how to read the results of a SQL query directly into a Pandas DataFrame.

It also displays how to apply a function to a DataFrame which operates across multiple columns.
"""
import numpy as np
import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('../data/factbook.db')

# Read the facts table into a Pandas DataFrame
query = 'select * from facts;'
facts = pd.read_sql_query(query, conn)

# Filter out any rows with invalid data
facts = facts.dropna(axis=0)
facts = facts[facts['area_land'] != 0]

def projected_population(row):
    """ Compute projected population.

    @param rows : pd.Series - row from facts table
    @return int - projected population
    """
    # Get initial population
    n0 =row['population']

    # Get growth rate
    r = row['population_growth'] / 100.0

    # Set the time frame as 35 years from now
    t = 35

    # Compute projected population
    n = n0 * np.exp(r * t)
    return int(n)

# Compute the population in 2050
# Assumption:  Original data is for 2015
facts['2050_pop'] = facts.apply(projected_population, axis=1)

# Sort by projected 2050 population
facts.sort_values(by='2050_pop', ascending=False, inplace=True)

# Print the 10 countries with highest projected population
print("10 countries with highest projected population in 2050:")
print(facts[['name', 'population', '2050_pop']].head(10))
