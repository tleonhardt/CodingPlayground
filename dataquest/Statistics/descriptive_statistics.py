#!/usr/bin/env python
"""
This example demonstrates statistical techniques. These techniques are referred to collectively as
descriptive statistics since they're used to describe and understand a dataset and not directly for
prediction.

The FiveThirtyEight team recently released a dataset containing the critics scores for a sample of
movies that have substantive (at least 30) user and critic reviews from IMDB, Rotten Tomatoes,
Metacritic, IMDB, and Fandango. Whenever a movie is released, movie review sites ask their approved
network of critics and their site's user base to rate the movie. These scores are aggregated and the
average score from both groups are posted on their site for each movie.

The dataset contains information on most movies from 2014 and 2015 and was used to help the team at
FiveThirtyEight explore Fandango's suspiciously high ratings. You can read their analysis here.

You'll be working with the file fandango_score_comparison.csv, which you can download from their
Github repo:  https://github.com/fivethirtyeight/data/tree/master/fandango

Here are some of the columns in the dataset:
    * FILM - film name.
    * RottenTomatoes - Rotten Tomatoes critics average score.
    * RottenTomatoes_User - Rotten Tomatoes user average score.
    * RT_norm - Rotten Tomatoes critics average score (normalized to a 0 to 5 point scale).
    * RT_user_norm - Rotten Tomatoes user average score (normalized to a 0 to 5 point scale).
    * Metacritic - Metacritic critics average score.
    * Metacritic_user_nom - Metacritic user average score (normalized to a 0 to 5 point scale).
    * Metacritic_norm - Metacritic critics average score (normalized to a 0 to 5 point scale).
    * Fandango_Ratingvalue - Fandango user average score (0 to 5 stars).
    * IMDB_norm - IMDB user average score (normalized to a 0 to 5 point scale).

The full column list and descriptions are available at FiveThirtyEight's Github repo. Let's focus on
the normalized user scores for now and generate histograms to better understand each site's
distributions.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Enable interactive mode so plt.show() won't block
plt.ion()

# Read CSV file into a Pandas DataFrame
movie_reviews = pd.read_csv("../data/fandango_score_comparison.csv")

# Create a Matplotlib subplot grid with the following properties:
#   4 rows by 1 column
#   figsize of 4 (width) by 8 (height)
#   each Axes instance should have an x-value range of 0.0 to 5.0
fig = plt.figure(figsize = (4, 8))
xvals = (0.0, 5.0)
ax1 = fig.add_subplot(4, 1, 1, xlim=xvals)
ax2 = fig.add_subplot(4, 1, 2, xlim=xvals)
ax3 = fig.add_subplot(4, 1, 3, xlim=xvals)
ax4 = fig.add_subplot(4, 1, 4, xlim=xvals)

# Generate the following historgrams:
# 1) Histogram of normalized Rotten Tomatoes scores by users
# 2) Histogram of normalized Metacritic scores by users
# 3) Histogram of Fandango scores by users
# 4) Histogram of IMDB scores by users
#ax1.hist(movie_reviews["RT_user_norm"])
movie_reviews.hist("RT_user_norm", ax=ax1)
movie_reviews.hist("Metacritic_user_nom", ax=ax2)
movie_reviews.hist("Fandango_Ratingvalue", ax=ax3)
movie_reviews.hist("IMDB_norm", ax=ax4)

# Automatically adjust subplot parameters to ensure padding so that labels and titles don't overlap
plt.tight_layout()

# Show the plot
plt.show(fig)

# Cleanup memory allocated to the figure and axes
plt.close(fig)

"""
The most obvious things that stick out is that essentially all of the Fandango average user reviews
are greater than 3 on a 5 point scale. The distributions of the Rotten Tomatoes and Metacritic scores,
on the other hand, more closely resemble a normal distribution, which is generally what you'd expect
if you knew nothing else. This is because the normal distribution is the most common distribution
in nature and is used to approximate many phenomenon.
"""


## Mean
# Now that you hopefully have some visual understanding of these scores, let's calculate some statistical
# measures to see how the properties the histograms suggested are reflected in numerical values.

# Select just the columns containing normalized user reviews and assign to a separate DataFrame
user_reviews = movie_reviews[['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']]

# Note: The below could more succinctly be done using user_reviews.describe()

# Generate a series containing the mean values of each column
means = user_reviews.mean()

# Extract individual mean values
rt_mean = means['RT_user_norm']
mc_mean = means['Metacritic_user_nom']
fg_mean = means['Fandango_Ratingvalue']
id_mean = means['IMDB_norm']
print("Mean normalized ratings:\n{}".format(means))


## Variance and Standard Deviation
variance = user_reviews.var(ddof=0)
std = user_reviews.std(ddof=0)

# Extract individual variance and standard deviation values
rt_var = variance['RT_user_norm']
rt_stdev = std['RT_user_norm']
mc_var = variance['Metacritic_user_nom']
mc_stdev = std['Metacritic_user_nom']
fg_var = variance['Fandango_Ratingvalue']
fg_stdev = std['Fandango_Ratingvalue']
id_var = variance['IMDB_norm']
id_stdev = std['IMDB_norm']
print("Standard deviation of normalized ratings:\n{}".format(std))

"""
The mean and variance values you calculated in the last screens should match the visual intuition the
histograms gave you. Rotten Tomatoes and Metacritic have more spread out scores (high variance) and
the mean is around 3. Fandango, on the other hand, has low spread (low variance) and a much higher mean,
which could imply that the site has a strong bias towards higher reviews. IMDB is somewhere in the middle,
with a low variance, like Fandango's user reviews, but a much more moderate mean value.
"""


## Scatter Plots
# Let's now explore if Fandango's user ratings are at least relatively correct. More precisely, are
# movies that are highly rated on Rotten Tomatoes, IMDB, and Metacritic also highly rated on Fandango?

# Create a Matplotlib subplot grid with the following properties:
#   3 rows by 1 column,
#   figsize of 4 (width) by 8 (height),
#   each Axes instance should have an x-value range of 0.0 to 5.0.
fig = plt.figure(figsize = (4, 8))
xvals = (0.0, 5.0)
ax1 = fig.add_subplot(3, 1, 1, xlim=xvals)
ax2 = fig.add_subplot(3, 1, 2, xlim=xvals)
ax3 = fig.add_subplot(3, 1, 3, xlim=xvals)

# Generate the following scatter plot (y-axis vs x-axis):
# First plot (top most): Fandango user reviews vs. Rotten Tomatoes user reviews.
# Second plot: Fandango user reviews vs. Metacritic user reviews.
# Third plot (bottom most): Fandango user reviews vs. IMDB user reviews
user_reviews.plot.scatter('RT_user_norm', 'Fandango_Ratingvalue', ax=ax1)
user_reviews.plot.scatter('Metacritic_user_nom', 'Fandango_Ratingvalue', ax=ax2)
user_reviews.plot.scatter('IMDB_norm', 'Fandango_Ratingvalue', ax=ax3)
plt.tight_layout()
plt.show(fig)
plt.close(fig)