#!/usr/bin/env python
"""
When are the most articles submitted?
"""
import dateutil

from read import load_data

# Read in the Hacker News dataset
hn = load_data()

def extract_hour(timestamp):
    date_time = dateutil.parser.parse(timestamp)
    return date_time.hour

# Make a column of submission hours
hn['submission_hour'] = hn['submission_time'].apply(extract_hour)

# Count the number of occurences of each hour
hours = hn['submission_hour'].dropna().value_counts()

# Print out the results
print(hours)
