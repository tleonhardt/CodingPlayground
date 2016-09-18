#!/usr/bin/env python
"""
In this script, we'll be working on computing summary statistics using SQL. There have been many
cases in the past few missions when we've needed to count the number of records that match a
particular SQL query. So far, we've been able to do this by:
    - Performing a SQL query with Python
    - Retrieving the results and storing into a list
    - Finding the length of the list
This approach works, but also requires quite a bit of code and is fairly slow. This example shows
how to count records and more using only SQL.

We'll be working with factbook.db, a SQLite database that contains information about each country in
the world. We'll use a table in the file called facts. Each row in facts represents a single country,
and contains several columns, including:
    * name -- the name of the country
    * area -- the total land and sea area of the country
    * population -- the population of the country
    * birth_rate -- the birth rate of the country
    * created_at -- the date the record was created
    * updated_at -- the date the record was updated
"""
import sqlite3
import numpy as np

# Initialize a connection to factbook.db
conn = sqlite3.connect('../data/factbook.db')
cur = conn.cursor()

# Fetch all the recors in the facts table
facts = cur.execute('select * from facts;').fetchall()

# Count the number of items in facts
facts_count = len(facts)
print("The 'facts' table has data on {} countries".format(facts_count))


## Counting In SQL
# Counting up the number of records in a table is a common operation, and it feels like it should be
# more efficient than the code we just wrote in the last screen. Thankfully, SQL includes the COUNT
# aggregation function, which allows us to count the number of records in a table. It's called an
# aggregation function because it works across many rows to compute an aggregate value. Here's an example:
#   SELECT COUNT(*) FROM facts;
# The query above will count the number of rows in the facts table of factbook.db. If we instead want
# to count the number of non-null values in a single column, we can use the following syntax:
#   SELECT COUNT(area_water) FROM facts;
# Note that the above query will only count the total number of non-null values in the area_water
# column, and so can return different counts than COUNT(*).
#
# Each of the queries above will return a list with a single tuple when executed in Python. It will
# look like this:  [(243,)]
# In order to get the integer count from the result, you'll need to extract the first element in the
# first tuple in the results.
#
# This style not only saves typing, it's also much faster for larger datasets, because we can do the
# counting inside the database, and not have to pull all the data into the Python environment first.

# Use the COUNT aggregation function to count the number of non-null values in birth_rate
query = 'SELECT COUNT(birth_rate) FROM facts;'
birth_rate_count = cur.execute(query).fetchone()[0]
print("There are {} non-null values in the 'birth_rate' column".format(birth_rate_count))


## Min And Max In SQL
# SQL contains other aggregation functions besides COUNT. MIN and MAX are two aggregation functions
# that allow us to find the maximum and minimum values in columns. Whereas we could use the COUNT
# function with any column, we can only use MAX and MIN with numeric columns.

# Use the MIN function to find the minimum value in population_growth
query = 'SELECT MIN(population_growth) FROM facts;'
min_population_growth = cur.execute(query).fetchone()[0]
print("Minimum population growth = {}".format(min_population_growth))

# Use the MAX function to find the maximum value in death_rate
query = 'SELECT MAX(death_rate) FROM facts;'
max_death_rate = cur.execute(query).fetchone()[0]
print("Maximum death rate = {}".format(max_death_rate))


##  Sum And Average In SQL
# The final two aggregation functions that we'll look at are SUM and AVG.

# Use the SUM function to find the sum of the area_land column
query = 'SELECT SUM(area_land) FROM facts;'
total_land_area = cur.execute(query).fetchone()[0]
print("Total land area = {}".format(total_land_area))

# Use the AVG function to find the mean of the area_water column
query = 'SELECT AVG(area_water) FROM facts;'
avg_water_area = cur.execute(query).fetchone()[0]
print("Average water area = {}".format(avg_water_area))


## Multiple Aggregation Functions
# If we wanted to use the SUM, AVG, and MAX functions on a column, it would be inefficient to write
# three different queries to retrieve the information. You may recall that we can query multiple
# columns by separating the names with a comma:
#   SELECT birth_rate, death_rate, population_growth FROM facts;
# We can apply the sample principle to use multiple aggregation functions in one query:
#   SELECT COUNT(*), SUM(death_rate), AVG(population_growth) FROM facts;
# Because there are three aggregation functions specified in the query, it will return a list
# containing a tuple with three elements.

# Write a single query that finds muliple summary statistics at once
query = 'SELECT AVG(population), SUM(population), MAX(birth_rate) FROM facts;'
facts_stats = cur.execute(query).fetchall()[0]
print("World Population = {}, Average Country Population = {}, Max Birth Rate = {}".format(facts_stats[1],
                                                                                           facts_stats[0],
                                                                                           facts_stats[2]))
## Conditional Aggregation
# As you may recall from earlier, we can use the WHERE statement to only query certain rows in a SQL
# table.  We can also use WHERE statements with aggregation functions to only calculate statistics
# for a certain subset of rows.

# Calculate the mean population_growuth for countries with a population more than 10 Million
query = 'SELECT AVG(population_growth) FROM facts WHERE population > 10000000;'
population_growth = cur.execute(query).fetchone()[0]
print("Average population growth of large countries = {}".format(population_growth))


## Selecting Unique Rows
# There are cases when we'll only want to select the unique values in a column or database, and not
# get each individual row. One example is if our facts table had duplicate entries for each country.
# If we want to get a list of all the countries in the world, we'll need to remove these duplicate
# rows, so countries appear twice. We can do this with the DISTINCT statement:
#   SELECT DISTINCT name FROM facts;
# The DISTINCT statement can also be used with multiple columns, in which case, it will return
# unique groups of those columns.

# Select all the distinct values in the birth_rate column of the facts table
query = 'SELECT DISTINCT birth_rate FROM facts;'
unique_birth_rates = cur.execute(query).fetchall()
print("Unique birth rates:\n{}".format(np.array(unique_birth_rates)[:,0]))


## Distinct Aggregations
# If we wanted to count the number of unique items in the population column, we could use the COUNT
# aggregation function along with the DISTINCT statement. Here's how it would work:
#   SELECT COUNT(DISTINCT population) FROM facts;

# Find the average of all the distinct values in the birth_rate column for large population
query = 'SELECT AVG(DISTINCT birth_rate) FROM facts WHERE population > 20000000;'
average_birth_rate = cur.execute(query).fetchone()[0]
print("Average distinct birth rate for large populations = {}".format(average_birth_rate))

# Find the sum of all the distinct values in the population column for large area
query = 'SELECT SUM(DISTINCT population) FROM facts WHERE area_land > 1000000;'
sum_population = cur.execute(query).fetchone()[0]
print("Sum of distinct population values for large area countries = {}".format(sum_population))


## Arithmetic In SQL
