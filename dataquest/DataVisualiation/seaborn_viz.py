#!/usr/bin/env python
"""
Seaborn is a Python library supported by Stanford University that enables you to create beautiful,
presentation-ready data visualizations. While Seaborn uses Matplotlib under the hood to represent,
manipulate, and customize plots, it exposes a high-level API that abstracts away a lot of the
internal Matplotlib logic.

I couldn't find the 'births.csv' file used during this tutorail, so I switched to a different dataset
so I could experiment with Seaborn.

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
import seaborn as sns


# Use Pandas to read the CSV file into a DataFrame
recent_grads = pd.read_csv('../data/recent-grads.csv')

# Enable interactive mode so plt.show() won't block
plt.ion()

# Histogram: distplot()
sns.distplot(recent_grads['Median'], kde=False)

# Seaborn Styling
# Just by importing Seaborn, the default styles are overriden for all plots
recent_grads.hist(column='Median')

# Customizing Histogram: Distplot()
plt.figure()
sns.distplot(recent_grads['Median'], kde=False, axlabel='Median Salary, $')

# Customize overall style
plt.figure()
sns.set_style('dark')
sns.distplot(recent_grads['Median'], kde=False, axlabel='Median Salary, $')
sns.plt.show()

# Generate a boxplot with the birthord column on the x-axis and the agepreg column on the y-axis
plt.figure()
sns.boxplot(recent_grads['Major_category'], recent_grads['Median'])
sns.plt.show()

# Pair Plot - n x n matrix of pairwise plots (need to make sure to not have any missing values)
plt.figure()
sns.pairplot(recent_grads[['Median', 'Total', 'Sample_size', 'Men', 'Women', 'ShareWomen', 'Employed']])
sns.plt.show()
