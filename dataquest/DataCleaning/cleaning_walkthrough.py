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
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re

from mpl_toolkits.basemap import Basemap

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

## Reading in the Survey Data
# Read in survey_all.txt
all_survey = pd.read_csv(os.path.join(data_dir, 'survey_all.txt'), delimiter='\t', encoding='windows-1252')

# Read in survey_d75.txt
d75_survey = pd.read_csv(os.path.join(data_dir, 'survey_d75.txt'), delimiter='\t', encoding='windows-1252')

# Combine the d75_survey and all_survey into a single DataFrame
survey = pd.concat([d75_survey, all_survey], axis=0)


## Cleaning Up The Surveys
# Copy the data from the dbn column of survey into a new column in survey called DBN
survey['DBN'] = survey['dbn']

# List of relevant columns
rel_cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11",
            "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11",
            "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11",]

# Filter survey so it only contains the relevant columns we care about
filtered_survey = survey[rel_cols]

# Assign the Dataframe survey to the key survey in the dictionary data
data['survey'] = filtered_survey


## Inserting DBN Fields
# Copy the dbn column in hs_directory into a new column called DBN
data['hs_directory']['DBN'] = data['hs_directory']['dbn']

def pad_two_digits(an_int):
    in_str = str(an_int)
    if len(in_str) == 1:
        return "0" + in_str
    return in_str

# Create a new column called padded_csd in the class_size dataset
data['class_size']['padded_csd'] = data['class_size']['CSD'].apply(pad_two_digits)

# Use the + operator along with the padded_csd and SCHOOL_CODE columns of class_zie, then
# assign the result ot the DBN column of class_size
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']


## Combining The SAT Scores
sat_results = data['sat_results']
# Convert the three SAT score columns from string data type to numeric datatype
sat_results['SAT Math Avg. Score'] = pd.to_numeric(sat_results['SAT Math Avg. Score'], errors='coerce')
sat_results['SAT Critical Reading Avg. Score'] = pd.to_numeric(sat_results['SAT Critical Reading Avg. Score'], errors='coerce')
sat_results['SAT Writing Avg. Score'] = pd.to_numeric(sat_results['SAT Writing Avg. Score'], errors='coerce')

# Create a column called sat_score that is the combined SAT score
sat_results['sat_score'] = sat_results['SAT Math Avg. Score'] + sat_results['SAT Critical Reading Avg. Score'] + sat_results['SAT Writing Avg. Score']


## Parsing Coordinates For Each School
# Extracting the latitude
def get_latitude(in_str):
    matches = re.findall("\(.+, .+\)", in_str)
    if len(matches) == 0:
        return None
    substr = matches[0]
    substr = substr.replace('(', '')
    substr = substr.replace(')', '')
    return substr.split(',')[0]

# Use the apply method with above function to get latitude from Location 1 column
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(get_latitude)

# Extracting the longitude
def get_longitude(in_str):
    matches = re.findall("\(.+, .+\)", in_str)
    if len(matches) == 0:
        return None
    substr = matches[0]
    substr = substr.replace('(', '')
    substr = substr.replace(')', '')
    return substr.split(',')[1]

# Use the apply method with above function to get latitude from Location 1 column
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(get_longitude)

# Convert lat and lon columns to numeric
data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')


## The next step we will need to take is to condense some of the data we have
# First we will need to make sure every value in the DBN column is unique

## Condensing Class Size
# Create a new variable called class_size and assign the value of data['class_size']
class_size = data['class_size']

# Filter class_size so the 'GRADE ' column only contains the value 09-12
class_size = class_size[class_size['GRADE '] == '09-12']

# Filter class_size so that the 'PROGRAM TYPE' column only contains the value 'GEN ED'
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']


## Computing Average Class Sizes
# Find the avergae values for each column for each DBN in class_size
class_size = class_size.groupby('DBN').agg(np.mean)

# DBN is now the index.  Reset the index, making DBN a column again
class_size.reset_index(inplace=True)

data['class_size'] = class_size


## Condensing Demographics
# Filter demographics and only select rows where schoolyear is 20112012
data['demographics'] = data['demographics'][data['demographics']['schoolyear'] == 20112012]


## Condensing Graduation
# Filter graduation and only select rows where the Cohort column equals 2006
data['graduation'] = data['graduation'][data['graduation']['Cohort'] == '2006']

# Filter graduation and only select rows where the Demographic column equals 'Total Cohort'
data['graduation'] = data['graduation'][data['graduation']['Demographic'] == 'Total Cohort']


## Converting AP Test Scores
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
# Convert columns in ap_2010 to numeric values
for col in cols:
    data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col], errors='coerce')


### Now it is finally time to start merging the disparate datasets
## Performing The Left Joins
# Both the ap_2010 and the graduation datasets have many missing DBN values, so we'll use a left
# join when we join the sat_results dataset with them. A left join means that our final Dataframe
# will have all the same DBN values as the original sat_results Dataframe.
# Merge sat_results, ap_2010, and graduation using left joins
combined = data["sat_results"]
combined = combined.merge(data['ap_2010'], how='left', on='DBN')
combined = combined.merge(data['graduation'], how='left', on='DBN')

## Performing the Inner Joins
# Now that we've done the left joins, we still have class_size, demographics, survey, and
# hs_directory left to merge into combined. Because these files contain information that's more
# valuable to our analysis, and because they have fewer missing DBN values, we'll use the inner join
# type when merging these into combined.
combined = combined.merge(data['class_size'], how='inner', on='DBN')
combined = combined.merge(data['demographics'], how='inner', on='DBN')
combined = combined.merge(data['survey'], how='inner', on='DBN')
combined = combined.merge(data['hs_directory'], how='inner', on='DBN')


## Filling In Missing values
# Since we did a number of left joins, we have a number of columns with missing data.  There are many
# ways to deal with this, one is to replace missing values with the column mean.
# Some analyses can deal with missing values (plotitng), but other analyses cannot (correlation).
# Compute the means of all the columns in combined
means = combined.mean()

# Fill in any missing values in combined iwth the column means
combined = combined.fillna(means)

# Fill in any remaining missing values in combined with 0
combined = combined.fillna(0)

### We've finished cleaning and combining our data! We now have a clean dataset on which we can base our analysis.

## Adding A School District Column
# One type of analysis that we might want to do is mapping out statistics on a school district level.
# In order to help us do this, it will be useful to add a column that specifies the school district to the dataset.
# The school district is just the first two characters of the DBN.
def first_2_chars(s):
    """ Extract the first 2 characters of a string and return them.
    @param s : str - input string
    @return str - first 2 characters in s
    """
    return s[0:2]

# Apply the function to the DBN column of combined, and assign result to a new column
combined['school_dist'] = combined['DBN'].apply(first_2_chars)


### --------------- Analying Data
# It is time to find correlations, make plots, and make maps.
# The first step that we'll take is to find correlations between every column and sat_score.
# This will help us figure out what columns might be interesting to investigate more or plot out.

## Finding correlations
# Correlations tell us how closely related two columns are. We'll be using the r value, also called
# Pearson's correlation coefficient, which measures how closely two sequences of numbers are correlated.
# An r value falls between -1 and 1, and tells you if the two columns are positively correlated, not
# correlated, or negatively correlated. The closer to 1 the r value is, the more strongly positively
# correlated the columns are. The closer to -1 the r value is, the more strongly negatively correlated
# the columns are. The closer to 0 the r value is, the less the columns are correlated.
#    In general r-values :
#       - above .25 or below -.25 are enough to qualify a correlation as interesting (potentially relevant)
#       - above .45 or below -.45 tend to be signficient correlations (usually relevant)
#       - above .65 or below -.65 tend to be strong correlations (almost always relevant)
# Find all possible correlations in the "combined" DataFrame
correlations = combined.corr()

# Filter correltaions so that only correlations for the column "sat_score" are shown
correlations = correlations['sat_score']

# Drop NaN values
correlations = correlations.dropna()

# Sort by correlation value
correlations.sort(ascending=False, inplace=True)

# Diplay all the rows in correlations with a correlation above 0.25 or below -0.25
print('Significant correlations with overall SAT score:')
print(correlations[abs(correlations) > 0.25])

# Note the extremely high negative correlation (< -0.7) between SAT Scores and the percentage of
# students receiving a free or reduced-cost lunch (frl_percent). The frl_percent is a direct measure
# of the percentage of students living in (or near) poverty.

## Plotting Enrollment
# Enable matplotlib interactive
plt.ion()

# Plot Total Enrollment vs SAT Score
combined.plot.scatter(x='sat_score', y='total_enrollment')
plt.show()


## Exploring Schools With Low SAT Scores And Enrollment
# From looking at the plot we just generated, it doesn't appear that there's a Significant correlations
# between SAT Score and total enrollment.  However, there is an interesting cluster of points at the
# bottom left where total_enrollment and sat_score are both low.
# Filter the combined Dataframe, and only keep rows with low sat_score and total_enrollment
low_enrollment = combined[combined['total_enrollment'] < 1000]
low_enrollment = combined[combined['sat_score'] < 1000]

# Display all the items in the School Name column of low enrollment
print('\nLow Enrollment schools with Low SAT Scores')
print(low_enrollment['School Name'])

# All of these schools appear to be international schools intended for recent
# immigrants from a foreign country who speak English as a second language.


## Plotting Language Learning Percentage
# From our research in the last screen, we found that most of the high schools with low total
# enrollment and low SAT scores are actually schools with a high percentage of English language
# learners enrolled. This indicates that it's actually ell_percent that correlates strongly with
# sat_score instead of total_enrollment
combined.plot.scatter(x='sat_score', y='ell_percent')
plt.show()


## Mapping the Schools
# It looks like ell_percent correlates with sat_score more strongly, because the scatterplot is
# more linear. However, there's still the cluster with very high ell_percent and low sat_score,
# which is the same group of international high schools that we investigated earlier.
#    In order to explore this relationship, we'll want to map out ell_percent by school district,
# so we can more easily see which parts of the city have a lot of English language learners.

# Setup the Matplotlib Basemap centered on New York City
plt.figure()
m = Basemap(projection='merc',
            llcrnrlat=40.496044,
            urcrnrlat=40.915256,
            llcrnrlon=-74.255735,
            urcrnrlon=-73.700272,
            resolution='i')
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

# Convert the lat and lon columns of combined to lists
longitudes = combined['lon'].tolist()
latitudes = combined['lat'].tolist()

# Plot the locations
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True)
plt.show()


## Plotting Out Statistics
# Now that we can plot out the positions of the schools, we can start to display meaningful
# information on maps, such as the percentage of English language learners by area.
#
# We can shade each point in the scatterplot by passing the keyword argument c into the scatter
# method. The c keyword argument will accept a sequence of numbers, and will shade points
# corresponding to lower numbers or higher numbers differently.
#
# Whatever sequence of numbers we pass into the c keyword argument will be converted to a range
# from 0 to 1. These values will then be mapped onto a color map.
plt.figure()
m = Basemap(projection='merc',
            llcrnrlat=40.496044,
            urcrnrlat=40.915256,
            llcrnrlon=-74.255735,
            urcrnrlon=-73.700272,
            resolution='i')
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

# Convert the lat and lon columns of combined to lists
longitudes = combined['lon'].tolist()
latitudes = combined['lat'].tolist()

# Plot the locations
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True, c=combined['ell_percent'], cmap='summer')
plt.show()


## Calculating District Level Statistics
# Unfortunately, due to the number of schools, it's hard to interpret the map we made in the last
# screen. It looks like uptown Manhattan and parts of Queens have a higher ell_percent, but we can't
# be sure. One way to make it easier to read very granular statistics is to aggregate them. In this
# case, we can aggregate based on district, which will enable us to plot ell_percent district by
# district instead of school by school.

# Find the average values for each column for each school_dist in combined
districts = combined.groupby('school_dist').agg(np.mean)

# Reset the index of districts, making school_dist a column again
districts.reset_index(inplace=True)


## Plotting ell_percent by District
# Now that we've taken the mean of all the columns, we can plot out ell_percent by district. Not
# only did we find the mean of ell_percent, we also took the mean of the lon and lat columns, which
# will give us the coordinates for the center of each district.

# Setup the Matplotlib Basemap centered on New York City
plt.figure()
m = Basemap(projection='merc',
            llcrnrlat=40.496044,
            urcrnrlat=40.915256,
            llcrnrlon=-74.255735,
            urcrnrlon=-73.700272,
            resolution='i')
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

# Convert the lat and lon columns of districts to lists
longitudes = districts['lon'].tolist()
latitudes = districts['lat'].tolist()

# Plot the locations
m.scatter(longitudes, latitudes, s=50, zorder=2, latlon=True, c=districts['ell_percent'], cmap='summer')
plt.show()
