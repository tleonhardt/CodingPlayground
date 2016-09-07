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
"""
import pandas as pd

# Use Pandas to read in the Fandango data into a DataFrame and then print out the first two rows
fandango = pd.read_csv('fandango_score_comparison.csv')

# DataFrames use Series objects to represent the columns in the data
# Select the FILM column, assign to the variable series_film, and print the first 5 values.
series_film = fandango['FILM']

# Select the RottenTomatoes column, assign to the variable series_rt, and print the first 5 values.
series_rt = fandango['RottenTomatoes']

# Create series from scratch using a custom index
film_names = series_film.values
rt_scores = series_rt.values
series_custom = pd.Series(rt_scores, index=film_names)

# Apply custom index to whole DataFrame, and any series/columns extracted will have this custom index
fandango_by_name = fandango.set_index('FILM')
rt_custom = fandango_by_name['RottenTomatoes']

# Integer index is preserved, thus a Series acts both like a dictionary and a list
fiveten = series_custom[5:10]
print(fiveten)
