#!/usr/bin/env python
"""
Which words appears most often in the headlines?
"""
import collections

from read import load_data

# Read in the Hacker News dataset
hn = load_data()

# Combine all of the headlines into one long string
all_headlines = ""
for headline in hn['headline']:
    all_headlines += str(headline).lower() + " "

# Split the long string into words
all_words = all_headlines.split()

# Count up how many times each word occurs
counts = collections.Counter(all_words)

# Print the 100 words that occur the most
print(counts.most_common(100))
