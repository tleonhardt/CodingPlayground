#!/usr/bin/env python
"""
Very basic SQLite query using CIA World Factbook database.
"""
import sqlite3

conn = sqlite3.connect('../data/factbook.db')

curr = conn.cursor()
query = 'SELECT name FROM facts ORDER BY population ASC LIMIT 10;'
curr.execute(query)
print(curr.fetchall())
