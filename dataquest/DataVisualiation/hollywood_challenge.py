#!/usr/bin/env python
"""
In this challenge, you'll practice creating data visualizations using data on Hollywood movies that
were released between 2007 to 2011. The goal is to better understand the underlying economics of
Hollywood and explore the outlier nature of success of movies. The dataset was compiled by David
McCandless and you can read about how the data was compiled here. You'll use a version of this
dataset that was compiled by John Goodall, which can be downloaded from his Github repo here.

We've renamed the file to hollywood_movies.csv. Here are some of the columns in the dataset:
    Year: the year the movie was released
    Critic Rating: average rating by the critics
    Audience Rating: average rating by the audience
    Genre: the genre the movie belongs to
    Budget: the movie's budget, in millions of dollars
    Domestic Gross: domestic (U.S.) revenue, in millions of dollars
    Worldwide Gross: total revenue worldwide, in millions of dollars
    Profitability: ratio of Budget to Worldwide Gross
"""
# Import the libraries you need and set up the environment.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Enable interactive mode so plt.show() won't block
plt.ion()

# Read hollywood_movies.csv into a Pandas Dataframe
hollywood_movies = pd.read_csv('../data/hollywood_movies.csv')

# Display the first 5 rows
print(hollywood_movies.head())

# Select the exclude column and display its distribution using the value_counts method.
# NOTE: Null voluaes (NaN) aren't counted and don't show up in value_counts()
print(hollywood_movies['exclude'].value_counts())

# Remote the exclude column, since it only contains null values
del hollywood_movies['exclude']


## Scatter Plots - Profitability And Audience Ratings
fig = plt.figure(figsize=(6,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
title = 'Hollywood Movies, 2007 - 2011'

ax1.scatter(hollywood_movies['Profitability'], hollywood_movies['Audience Rating'])
ax1.set(xlabel='Profitability', ylabel='Audience Rating', title=title)

ax2.scatter(hollywood_movies['Audience Rating'], hollywood_movies['Profitability'])
ax2.set(xlabel='Audience Rating', ylabel='Profitability', title=title)

plt.show()


## Scatter Matrix - Profitability And Critic Ratings
# Filter out the movie Paranormal Activity due to its outlier profitability
max_profitability = hollywood_movies['Profitability'].max()
normal_movies = hollywood_movies[hollywood_movies['Profitability'] < max_profitability]

# Generate a scatter matrix of the Profitability and Audience Rating columns
pd.scatter_matrix(normal_movies[['Profitability', 'Audience Rating']], figsize=(6,6))

# Use box plots to better understand the distributions of ratings by critics vs audience
normal_movies[['Critic Rating', 'Audience Rating']].plot.box()


## Box Plot - Critic Vs Audience Ratings Per Year
# Use the Dataframe method sort_values to sort normal_movies by the Year column.
normal_movies = normal_movies.sort_values(by='Year')

# Create a Figure instance
fig = plt.figure(figsize=(8,4))

# Create 2 horizontally oriented subplots
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# On the left subplot, generate a separate box plot for the values in Critic Rating
sns.boxplot(x=normal_movies['Year'], y=normal_movies['Critic Rating'], ax=ax1)

# On the right subplot, generate a separate box plot for the values in Audience Rating
sns.boxplot(x=normal_movies['Year'], y=normal_movies['Audience Rating'], ax=ax2)

plt.show()


## Box Plots - Profitable Vs Unprofitable Movies
# Create a new Boolean column called Profitable, equal to True if Profitability > 1
def is_profitable(row):
    if row["Profitability"] <= 1.0:
        return False
    return True
normal_movies["Profitable"] = normal_movies.apply(is_profitable, axis=1)
print(normal_movies["Profitable"].value_counts())

# Create a Figure instance of 12" x 6"
fig = plt.figure(figsize=(12,6))

# Add 2 horizontally oriented subplots
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# On the left subplot, make a boxplot for Audience Rating
sns.boxplot(x=normal_movies['Profitable'], y=normal_movies['Audience Rating'], ax=ax1)

# On the right subplot, make a boxplot for Critic Rating
sns.boxplot(x=normal_movies['Profitable'], y=normal_movies['Critic Rating'], ax=ax2)

plt.show()
