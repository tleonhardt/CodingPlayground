#!/usr/bin/env python
"""
The FiveThirtyEight team recently released a dataset containing the critics scores for all movies
that have substantive user and critic reviews from IMDB, Rotten Tomatoes, Metacritic, and Fandango.
We'll be working with the file fandango_score_comparison.csv, which you can download from their
Github repo. Here are some of the columns in the dataset:
    FILM - film name
    RottenTomatoes - Rotten Tomatoes critics average score
    RottenTomatoes_User - Rotten Tomatoes user average score
    RT_norm - Rotten Tomatoes critics average score (normalized to a 0 to 5 point system)
    RT_user-norm - Rotten Tomatoes user average score (normalized to a 0 to 5 point system)
    Metacritic - Metacritic critics average score
    Metacritic_User - Metacritic user average score
    The full column list and descriptions are available on the Github repo.

This is an exercise for learning about Pandas DataFrame objects.
"""
import pandas as pd
import numpy as np

# Use Pandas to read in the Fandango data into a DataFrame
fandango = pd.read_csv('../data/fandango_score_comparison.csv')

# Selecting rows can be done using either bracket notation with slices or iloc and integrs or lists of integers
first_last = fandango.iloc[[0,-1]]

# We can set a custom index based on an existing column
fandango_films = fandango.set_index('FILM', drop=False)

# Selection using custom index can be done using the loc[] method or slices using bracket notation
movies_to_select = ["The Lazarus Effect (2015)",
                    "Gett: The Trial of Viviane Amsalem (2015)",
                    "Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[movies_to_select]

# The apply() method in Pandas allows us to specify Python logic that we want evaluated over Series objects in a DataFrame.
# Both columns and rows are represented as Series objects within a DataFrame
# By default apply() works over columns.

# Here we calculate the standard deviation of only the columns containing floating-point values
# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# Use apply() with a function which returns a single value for an entire Series
deviations = float_df.apply(np.std)


# We can also use apply() with a function that acts on every value instead of an entire series
double_df = float_df.apply(lambda x: x*2)

# To apply a function over the rows in a DataFrame, we need to set the axis parameter to 1
# Calculate the average of each movie's values for RT_user_norm and Metacritic_user_nom
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(np.std, axis=1)
rt_mt_means = rt_mt_user.apply(np.mean, axis=1)
