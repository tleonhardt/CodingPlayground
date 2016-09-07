#!/usr/bin/env python
""" This script uses Pandas to summarize data from the college majors dataset from FiveThirtyEight.

The American Community Survey is a survey run by the US Census Bureau that collects data on
everything from the affordability of housing to employment rates for different industries. For this
challenge, you'll be using the data derived from the American Community Survey for years 2010-2012.
The team at FiveThirtyEight has cleaned the dataset and made it available on their Github repo.

Here's a quick overview of the files we'll be working with:
* all-ages.csv - employment data by major for all ages
* recent-grads.csv - employment data by major for just recent college graduates

Here are descriptions of a few of the columns (there are 21 columns in total):
    Rank - The numerical rank of the major by post-graduation median earnings.
    Major_code - The numerical code of the major.
    Major - The description of the major.
    Major_category - The category of the major.
    Total - The total number of people who studied the major.
    Men - The number of men who studied the major.
    Women - The number of women who studied the major.
    ShareWomen - The share of women (from 0 to 1) who studied the major.
    Employed - The number of people who studied the major and were employed post-graduation.
"""
import pandas as pd

# Read the datasets into Pandas DataFrames
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

# Use the Total column to calculate the number of people who fall under each Major_category for each dataset
all_ages_major_categories =  all_ages.pivot_table(index='Major_category', values='Total', aggfunc=sum).to_dict()
recent_grads_major_categories = recent_grads.pivot_table(index='Major_category', values='Total', aggfunc=sum).to_dict()

# Use the Low_wage_jobs and Total columns to calculate the proportion of recent college graduates that worked low wage jobs
low_wage_percent = recent_grads['Low_wage_jobs'].sum() / recent_grads['Total'].sum()

# Let's now calculate the number of majors where recent grads did better than the overall population.
# First, create versions of both datasets indexed by Major code so it is easier to compare the two datasets
all_by_major = all_ages.set_index('Major_code')
recent_by_major = recent_grads.set_index('Major_code')

# Now add the 'Unemployment_rate' column from recent_by_major as a new column to all_by_major
all_by_major['Recent_unemployment_rate'] = recent_by_major['Unemployment_rate']

# Now calculate the number of majors for which recent grads are doing better and vice versa
recent_grads_lower_unemp_count = sum(all_by_major['Recent_unemployment_rate'] < all_by_major['Unemployment_rate'])
all_ages_lower_unemp_count = sum(all_by_major['Unemployment_rate'] < all_by_major['Recent_unemployment_rate'])

print("Num majors where recent grads have lower unemployment rate than historical: {}".format(recent_grads_lower_unemp_count))
print("Num majors where recent grads have higher unemployment rate than historical: {}".format(all_ages_lower_unemp_count))
