#!/usr/bin/env python
"""
We'll be working with the data from the American Community Survey from a survey on job outcomes for recent college graduates based on the major they studied in college.

You can find the cleaned up version of the dataset on FiveThirtyEight's Github repo.

Here are some of the columns in the dataset:
    Rank - Rank by median earnings
    Major_code - Major code
    Major - Major description
    Major_category - Category of major
    Total - Total number of people with major
    Sample_size - Sample size (unweighted) of full-time
    Men - Male graduates
    Women - Female graduates
    ShareWomen - Women as share of total
    Employed - Number employed
"""
import pandas as pd
import matplotlib.pyplot as plt


# Use Pandas to read the CSV file into a DataFrame
recent_grads = pd.read_csv('../data/recent-grads.csv')

# Enable interactive mode so plt.show() won't block
plt.ion()


## Histograms - good for analyzing a single column and looking for outliers or distribution
columns = ['Median','Sample_size']
# Set the `layout` parameter as `(2,1)` so the graphs are displayed as 2 rows & 1 column
recent_grads.hist(column=columns, layout=(2,1), grid=False)

# By default, the .hist() method uses 10 as the number of bins, but you can specify a different value using the bins parameter
recent_grads.hist(column='Sample_size', bins=50)


## Box Plots - Box and Whisker plot
# Select just `Sample_size` & `Major_category` columns from `recent_grads`
# Name the resulting DataFrame as `sample_size`
sample_size = recent_grads[['Sample_size', 'Major_category']]

# Run the `boxplot()` function on `sample_size` DataFrame and specify, as a parameter,
# that we'd like a box and whisker diagram to be generated for each unique `Major_category`
sample_size.boxplot(by='Major_category')

# Format the resulting plot to make the x-axis labels (each `Major_category` value)
# appear vertically instead of horizontally (by rotating 90 degrees)
plt.xticks(rotation=90)

# Generate a similar box plot for the Total column:
recent_grads[['Total', 'Major_category']].boxplot(by='Major_category')
plt.xticks(rotation=90)


## Multiple plots in one Chart
plt.figure()
# Plot Unemployment_rate on x-axis, Median salary on y-axis, in red
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['Median'], color='red', label='Unemployment rate')
# Plot ShareWomen (Female % in major) on x-axis, Median salary on y-axis, in blue
plt.scatter(recent_grads['ShareWomen'], recent_grads['Median'], color='blue', label='Share of Women')
plt.legend()
plt.ylabel('Median Salary ($)')
plt.show()


# Generate 2 scatter plots on the same chart, one for the Unemployment_rate and one for ShareWomen,
# both compared against the y-axis of the 25th percentile salary ('P25th' column).
plt.figure()
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['P25th'], color='red', label='Unemployment rate')
plt.scatter(recent_grads['ShareWomen'], recent_grads['P25th'], color='blue', label='ShareWomen')
plt.legend()
plt.ylabel('25th percentile Salary ($)')
plt.show()
