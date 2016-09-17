#!/usr/bin/env python
"""
Read data in from Hacker News
"""
import pandas as pd

def load_data():
    columns = ['submission_time', 'upvotes', 'url', 'headline']
    df = pd.read_csv('../../data/hn_stories.csv', header=None, names=columns)
    return df

if __name__ == "__main__":
    # This will call load_data if you run the script from the CLI
    hn_stories = load_data()

    # Print out first few rows
    print(hn_stories.head())
