#!/usr/bin/env python
"""
In this example, we'll explore how to interact with a SQLite database in Python.  SQLite is a database
that doesn't require a standalone server process and stores the entire database as a file on disk.
This makes it ideal for working with larger datasets that can fit on disk but not in memory. Since
the Pandas library loads the entire dataset we're working with into memory, this makes SQLite a
compelling alternative option for working with datasets that are larger than 8 gigabytes (which is
roughly the amount of memory modern computers contain). In addition, since the entire database can
be contained within a single file, some datasets are released online as a SQLite database file (using
the extension .db).

You can interact with a SQLite database in two main ways:
    * using the Sqlite Python module.
    * using the SQLite shell.

We'll work with the dataset from the American Community Survey on college majors and job outcomes.
The full table has 21 columns, which are explained in more detail on FiveThirtyEight's Github repo:
    https://github.com/fivethirtyeight/data/tree/master/college-majors

Here are some of the most important columns:
    * Rank - Rank by median earnings
    * Major_code - Major code
    * Major - Major description
    * Major_category - Category of major
    * Total - Total number of people with major
    * Sample_size - Sample size (unweighted) of full-time
    * Men - Male graduates
    * Women - Female graduates
    * ShareWomen - Women as share of total
    * Employed - Number employed

The database we'll be working with is called "jobs.db" and the data is in table "recent_grads".

From Python 2.5 and onwards, the Sqlite module has come built-in to the Python language, which means
we don't need to install any separate libraries to get started. Specifically, we'll be working with
the Sqlite3 Python module, which was developed to work with SQLite version 3.

Once imported, we connect to the database we want to query using the connect() function. The
connect() function has a single required parameter, the database we want to connect to. Since the
database we're working with is stored as a file on disk, we need to pass in the filename. The
connect() function returns a Connection instance, which maintains the connection to the database we
want to work with. When you're connected to a database, SQLite locks the database file and prevents
any other process from connecting to the database simultaneously. This was a design decision made by
the SQLite team to keep the database lightweight and avoid the complexity that arises when multiple
processes are interacting with the same database.
"""
import sqlite3

# Once imported, we connect to the database we want to query using the connect() function
conn = sqlite3.connect('../data/jobs.db')

## Cursor Object And Tuple
# Before we can execute a query, we need to express our SQL query as a string. While we use the
# Connection class to represent the database we're working with, we use the Cursor class to:
#   * run a query against the database
#   * parse the results from the database
#   * convert the results to native Python objects
#   * store the results within the Cursor instance as a local variable
# After running a query and converting the results to a list of tuples, the Cursor instance stores
# the list as a local variable. Before diving into the syntax of querying the database, let's learn
# more about tuples.

# We need to use the Connection instance method cursor() to return a Cursor instance corresponding to
# the database we want to query.
cursor = conn.cursor()

# SQL Query as a string
query = "select * from recent_grads;"

# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)

# Fetch the full results set, as a list of tuples
results = cursor.fetchall()

# Display the first 3 results.
print("First 3 rows:\n{}".format(results[0:3]))

# Write a query that returns all of the values in the Major column
query = "select Major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print("First 3 majors:\n{}".format(majors[0:3]))


## Fetching A Specific Number Of Results
# To make it easier to work with large results sets, the Cursor class allows you to control the
# number of results you want to retrieve at any given time. To return a single result (as a tuple),
# we use the Cursor method fetchone() and to return n results, we use the Cursor method fetchmany().

# Write and run a query that returns the Major and Major_category columsn
query = "select Major, Major_category from recent_grads;"
cursor.execute(query)

# Fetch the first 5 results
five_results = cursor.fetchmany(5)
print("First 5 results:\n{}".format(five_results))


# Write and execute a query that returns the major names in reverse alphabetical order
query = 'SELECT Major FROM recent_grads ORDER BY Major DESC LIMIT 5'
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
print('Last 5 Majors (reverse alphabetical order):\n{}'.format(reverse_alphabetical))


## Closing The Connection
# Since SQLite restricts access to the database file when we're connected to a database, we need to
# close the connection when we're done working with it. Closing the connection to the database allows
# other processes to access the database, which is important when you're in a production environment
# and working with other team members. In addition, if we made any changes to the database, they are
# automatically saved and our changes are persisted in the database file upon closing.
conn.close()
