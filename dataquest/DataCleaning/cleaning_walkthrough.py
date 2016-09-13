#!/usr/bin/env python
"""
One of the most controversial issues in the US educational system is the efficacy of standardized
tests, and whether they are unfair to certain groups. Given our prior knowledge about this topic,
investigating the correlations between SAT scores and demographic factors might be an interesting
angle to take. We could correlate SAT scores with factors like race, gender, income, and more.

The NYC Open Data website has a plethora of data on NYC public schools, including SAT data.  But the
data of interest is spread over many different data sets.

First we need to read in and clean multiple datasets and then merge them into a single useful dataset.
"""
import os
import pandas as pd

# Directory containing all of the datasets
data_dir= "../data/schools"

# All of the CSV-format datasets
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

# Dicitonary of Pandas DataFrames for all of the datasets
data = {}

# Read each of the files in the list data_files into a Pandas Dataframe using the read_csv function.
# Add each of the Dataframes to the dictionary data, using the base of the filename as the key.
for data_file in data_files:
    df = pd.read_csv(os.path.join(data_dir, data_file))
    data[os.path.splitext(data_file)[0]] = df

print(data.keys())
