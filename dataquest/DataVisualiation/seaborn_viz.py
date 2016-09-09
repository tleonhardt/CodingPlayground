#!/usr/bin/env python
"""
Seaborn is a Python library supported by Stanford University that enables you to create beautiful,
presentation-ready data visualizations. While Seaborn uses Matplotlib under the hood to represent,
manipulate, and customize plots, it exposes a high-level API that abstracts away a lot of the
internal Matplotlib logic.

In this lesson, we'll be working with data from the National Survey of Family Growth. The data was
collected from January 2002 to March 2003 and contains data on pregnancy, family life, and more.
We've selected a few columns from the original data, which are:
    prglngth -- the length of the pregnancy in weeks.
    birthord -- which child this was for the pregnant mother.
    birthwgt_lb1 -- the pounds portion of the birth weight.
    birthwgt_oz1 -- the ounces portion of the birth weight.
    agepreg -- the mother's age at the end of the pregnancy, in years.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Use Pandas to read the CSV file into a DataFrame
births = pd.read_csv('../data/births.csv')

# Enable interactive mode so plt.show() won't block
# plt.ion()

%matplotlib inline

# Histogram: distplot()
sns.distplot(births['prglngth'], kde=False)
sns.plt.show()

# Seaborn Styling
# Just by importing Seaborn, the default styles are overriden for all plots
births.hist(column='agepreg')

# Customizing Histogram: Distplot()
sns.distplot(births['prglngth'], kde=False, axlabel='Pregnancy Length, weeks')
sns.plt.show()

sns.set_style('dark')
sns.distplot(births['birthord'], kde=False, axlabel='Birth number')
sns.plt.show()

# Generate a boxplot with the birthord column on the x-axis and the agepreg column on the y-axis
sns.boxplot(births['birthord'], births['agepreg'])
sns.plt.show()
