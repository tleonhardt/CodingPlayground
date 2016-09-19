#!/usr/bin/env python
"""
There are many times when we don't just want to query data from SQL tables, and instead we want to
modify the existing data or add new data. Modifying data in SQL tables is possible through 3 statements:
    * INSERT -- adds new data
    * UPDATE -- changes the values of some columns in existing data
    * DELETE -- removes existing data
In this mission, we'll cover these 3 statements. As we do so, we'll be working with factbook.db, a
database which contains data on very countery in the world.  There is a single table in the file
called facts. Each row in facts represents a single country, and contains several
columns, including:
    * name -- the name of the country
    * area -- the total land and sea area of the country
    * population -- the population of the country
    * birth_rate -- the birth rate of the country
    * created_at -- the date the record was created
    * updated_at -- the date the record was updated
"""
import sqlite3

conn = sqlite3.connect("../data/factbook.db")
cur = conn.cursor()

## Working With Dates In SQL
# Dates are an extremely important part of querying and analyzing data. Some common use cases are
# segmenting records by date, figuring out how many events occurred on each date, and finding all
# the dates on which a particular event occurred.
#
# Because of how common it is to use dates when querying data, SQL has built-in support for handling
# dates. It makes it easy to query based on date and time ranges. We can query a date range from the
# facts table using the following syntax:
#   SELECT * FROM facts WHERE created_at < "2015-11-01" AND created_at > "2015-10-30";

query = 'SELECT * FROM facts WHERE updated_at > "2015-10-30 16:00" AND updated_at < "2015-11-2 15:00" LIMIT 10;'
in_dates = cur.execute(query).fetchall()
print("Some data updated between Oct 30, 2015 and Nov 2, 2015:\n{}".format(in_dates))


## Data Types
# In Python, variables can have data types, such as string, float, or integer. Whereas these data
# types don't have to be specified upfront in Python, each column in a SQL table has to have a data
# type specified when the table is created. This helps SQL store and search the data efficiently.
# Every SQL database engine has slightly different names for data types. Some of the common data
# types for SQLite are:
#    * INTEGER -- similar to the integer type in Python
#    * REAL -- similar to the float type in Python
#    * FLOAT -- similar to the float type in Python
#    * TEXT -- similar to the string type in Python
#    * VARCHAR(255) -- similar to the string type in Python
# The reason why SQLite has so many names for similar data types is to provide compatibility with
# other databases, some of which will only allow one or the other (REAL or FLOAT, for example).
#
# To see the data types of each column in a table, you can use the PRAGMA statement:
#   PRAGMA table_info(tableName);

# Write a SQL query that returns the data type of each column in facts
query = 'PRAGMA table_info(facts);'
facts_types = cur.execute(query).fetchall()
print("Data types of each column in the facts table:\n{}".format(facts_types))


## Primary Keys
# Every SQL table has a primary key. A primary key is a column or combination of columns that are
# unique for each row in the table. The primary key is how SQL uniquely identifies each row. Most
# tables have an integer column called id by default, which is the primary key.
#
# The most common name for the primary key column in a SQL table is id, although it doesn't have to be.

# Write a SQL query that uses the ORDER BY and LIMIT statements to select the entire row that has
# the highest id value.
query = 'SELECT * FROM facts ORDER BY id DESC LIMIT 1;'
highest_id = cur.execute(query).fetchall()
print("Data for highest primary key in facts table:\n{}".format(highest_id))


## Inserting Data Into A Table
# Sometimes, we'll receive new rows that we want to add to a SQL table. We can insert a row into a
# table using the INSERT SQL statement. Here's an example INSERT statement:
#   INSERT INTO tableName VALUES (value1, value2, ...);

# Write a SQL query that inserts a row into facts
query = '''INSERT INTO facts
           VALUES (262, "dq", "DataquestLand", 60000, 40000, 20000, 500000, 100, 50, 10, 20,
                   "2016-02-25 12:00:00", "2016-02-25 12:00:00");'''
cur.execute(query)
print("Insert a row into the facts table")


## Missing Values
# Because it's so common for data to be missing, SQL has explicit support for handling missing, or
# NULL, values. You can retrieve any rows where a specific column is NULL by using the following syntax:
#   SELECT * from tableName WHERE columnName IS NULL;

# Insert a row will some NULL values
query = '''INSERT INTO facts
           VALUES (263, "dq", "DataquestLand", NULL, NULL, 20000, 500000, 100, 50, 10, 20,
                   "2016-02-25 12:00:00", "2016-02-25 12:00:00");'''
cur.execute(query)
print("Insert a row into the facts table which contains some NULL values")


## Updating Rows
# et's say we wanted to simulate a takeover of Australia by New Zealand and rename Australia. You
# can use the UPDATE statement for this:
#    UPDATE tableName SET column1=value1, column2=value2, ... WHERE column1=value3, column2=value4, ...
# Here's a concrete example:
#    UPDATE facts SET name="New Zealand", code="nz" WHERE name="Australia"

# Write a SQL query that updates a column value
query = 'UPDATE facts SET name="ToddLand" WHERE name="DataquestLand";'
cur.execute(query)
print("Updated name of 'DataquestLand' to 'ToddLand'")


## Deleting rows
# Let's say we wanted to remove any rows associated with the United States. We'd have to use the
# DELETE statement like this:
#   DELETE FROM tableName WHERE column1=value1, column2=value2, ...;
# Here's a concrete example:
#   DELETE FROM facts WHERE name="United States";

# Write a SQL query that removes all the rows in facts where name is a constant
query = 'DELETE FROM facts WHERE name = "ToddLand";'
cur.execute(query)
print("Deleted all rows with name == 'ToddLand'")


conn.close()
