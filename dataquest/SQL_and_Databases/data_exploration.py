#!/usr/bin/env python
"""
In this example, we will practice calculating summary statistics in SQL while exploring data from
factbook.db. Recall that factbook.db contains information about each country in the world. We will
work with the facts table, where each row represents a single country. Here's the descriptions of
some of the columns:
    * name -- the name of the country
    * area -- the total land and sea area of the country
    * population -- the population of the country
    * birth_rate -- the birth rate of the country
    * created_at -- the date the record was created
    * updated_at -- the date the record was updated

We will focus on the population values for each country and predicting the next year's population
using the data. First, we will need to explore the data and look for any data quality issues.
"""
import sqlite3

conn = sqlite3.connect("../data/factbook.db")
cur = conn.cursor()

# Calculat the means in SQL for the population, population_growth, birth_rate, and death_rate
query = 'SELECT AVG(population), AVG(population_growth), AVG(birth_rate), AVG(death_rate) FROM facts;'
(pop_avg, pop_growth_avg, birth_rate_avg, death_rate_avg) = cur.execute(query).fetchone()
print('pop_avg = {}, growth_avg = {}, birth_avg = {}, death_avg = {}'.format(pop_avg,
                                                                             pop_growth_avg,
                                                                             birth_rate_avg,
                                                                             death_rate_avg))
## Ranges
# While the averages give you some sense of the values in these columns, let's calculate the ranges
# as well to better understand the lower and upper bounds for these columns. This way, you can also
# look for the presence of any outliers.
ranges = 'SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth), MIN(birth_rate), MAX(birth_rate), MIN(death_rate), MAX(death_rate) FROM facts;'
pop_ranges = cur.execute(ranges).fetchone()
pop_min = pop_ranges[0]
pop_max = pop_ranges[1]
pop_growth_min = pop_ranges[2]
pop_growth_max = pop_ranges[3]
birth_rate_min = pop_ranges[4]
birth_rate_max = pop_ranges[5]
death_rate_min = pop_ranges[6]
death_rate_max = pop_ranges[7]
print("\nUnfiltered population ranges:")
print("Population min/max = {}, {}".format(pop_min, pop_max))
print("Population growth rate min/max = {}, {}".format(pop_growth_min, pop_growth_max))
print("Birth rate min/max = {}, {}".format(birth_rate_min, birth_rate_max))
print("Death rate min/max = {}, {}".format(death_rate_min, death_rate_max))


## Filtering
# If you observed the values in the previous screen, you may have noticed the outlier values. The
# max value for population is 7,256,490,011 while the minimum is 0. We know that China, the most
# populated country in the world, doesn't even have 2 billion people but the max value for the
# population column is over 7 billion. The minimum value for the population column is also
# problematic, since no country has 0 people.
#
# These quirks exist because the database contains rows for entities that aren't countries. For
# example, there's a row representing the entire world (hence the 7 billion population) and some
# rows representing oceanic areas (hence the population of 0).

# Write a single query that returns the minimum and maximum values for countries where population is less than 2 billion and population is greater than 0
filtered = 'SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth), MIN(birth_rate), MAX(birth_rate), MIN(death_rate), MAX(death_rate) FROM facts WHERE population < 2e9 AND population > 0;'
filtered_ranges = cur.execute(filtered).fetchone()
pop_min = filtered_ranges[0]
pop_max = filtered_ranges[1]
pop_growth_min = filtered_ranges[2]
pop_growth_max = filtered_ranges[3]
birth_rate_min = filtered_ranges[4]
birth_rate_max = filtered_ranges[5]
death_rate_min = filtered_ranges[6]
death_rate_max = filtered_ranges[7]
print("\nFiltered population ranges:")
print("Population min/max = {}, {}".format(pop_min, pop_max))
print("Population growth rate min/max = {}, {}".format(pop_growth_min, pop_growth_max))
print("Birth rate min/max = {}, {}".format(birth_rate_min, birth_rate_max))
print("Death rate min/max = {}, {}".format(death_rate_min, death_rate_max))


##  Predicting Future Population Growth
# These measures seem to align more with reality. Let's now predict next year's population for each
# country using the following formula:
#   projected_population = population + (population * population_growth)

# Use SQL arithmetic to return the projected population values
query = '''SELECT name, population, population_growth, ROUND(population * (1.0 + population_growth/100.0), 0)
           FROM facts
           WHERE population is not NULL AND population_growth is not NULL AND population < 7e9 AND population > 0
           ORDER BY population DESC
           LIMIT 10;
        '''
projected_population_data = cur.execute(query).fetchall()
print(projected_population_data[0:10])


## Exploring Projected Population
# To understand how the population would shift under the projected population values, calculate the
# min, max, and average values for the projected population values.
formula = 'population * (1 + population_growth/100.0)'
proj_pop_query = '''SELECT ROUND(MIN({0}), 0), ROUND(MAX({0}), 0), ROUND(AVG({0}), 0)
                    FROM facts
                    WHERE population > 0 AND population < 7000000000 AND population is not null and population_growth is not null;
                 '''.format(formula)

proj_results = conn.execute(proj_pop_query).fetchone()

pop_proj_min = proj_results[0]
pop_proj_max = proj_results[1]
pop_proj_avg = proj_results[2]

print("Projected Population min, max, average: {}, {}, {}".format(pop_proj_min, pop_proj_max, pop_proj_avg))
