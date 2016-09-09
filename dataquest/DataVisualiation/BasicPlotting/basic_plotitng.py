#!/usr/bin/env python
"""
This analyze data on forest firest from a National Park in Portugal.  The park is divided up into a
9 by 9 grid. Each fire has corresponding X position on the grid and Y position on the grid

Each row describes a fire that happened in Montesinho National Park. Here's a listing of the columns:
    X -- The X position on the grid where the fire occurred.
    Y -- The Y position on the grid where the fire occured.
    month -- the month the fire occcurred.
    day -- the day of the week the fire occurred.
    temp -- the temperature in Celsius when the fire occurred.
    wind -- the wind speed when the fire occurred in units of km/h
    rain -- the rainfall when the fire occurred.
    area -- the area the fire consumed in ha

The intent is to gain some familiarity with Matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Reset matplotlib defaults
mpl.rcParams.update(mpl.rcParamsDefault)


# Use Pandas to read the CSV file into a DataFrame
forest_fires = pd.read_csv('forest_fires.csv')

# Enable interactive mode so plt.show() won't block
plt.ion()


## Scatter Plots
# Make a scatter plot with the wind column on the x-axis and the area column on the y-axis
plt.figure()
plt.scatter(forest_fires['wind'], forest_fires['area'])
plt.xlabel('wind speed (km/h)')
plt.ylabel('burned area (ha)')
plt.show()

# Make a scatter plot with the temp column on the x-axis and the area column on the y-axis
plt.figure()
plt.scatter(forest_fires['temp'], forest_fires['area'])
plt.xlabel('temperature (C)')
plt.ylabel('burned area (ha)')
plt.show()


## Line Charts
age = [5, 10, 15, 20, 25, 30]
height = [25, 45, 65, 75, 75, 75]
# Use the plot() method to plot age on the x-axis and height on the y-axis
plt.figure()
plt.plot(age, height)
plt.xlabel('age (years)')
plt.xlabel('height (inches)')
plt.show()


## Bar Graphs
# Use pivot_table() method to calculate the average area of the fires started at each X or Y position
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=np.mean)
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=np.mean)
# Use the bar() method to plot area_by_y.index on the x-axis and area_by_y on the y-axis
plt.figure()
plt.bar(area_by_y.index, area_by_y)
plt.xlabel('Y grid location')
plt.ylabel('Average area of fires started at location Y')
plt.show()
# Use the bar() method to plot area_by_y.index on the x-axis and area_by_y on the y-axis
plt.figure()
plt.bar(area_by_x.index, area_by_x)
plt.xlabel('X grid location')
plt.ylabel('Average area of fires started at location X')
plt.show()


## Horizontal Bar Graphs
# barh() is a horizontal bar chart and the first variable passed in is plotted on hte y-axis
area_by_month = forest_fires.pivot_table(index="month", values="area", aggfunc=np.mean)
area_by_day = forest_fires.pivot_table(index="day", values="area", aggfunc=np.mean)
# We need to take an extra step to deal with an index consisting of strings
# Use the barh() method to plot range(len(area_by_month)) on the y-axis and area_by_month on the x-axis
plt.figure()
plt.barh(range(len(area_by_month)), area_by_month)
plt.ylabel('month')
plt.xlabel('burned area (ha)')
plt.show()

# Use the barh() method to plot range(len(area_by_day)) on the y-axis and area_by_day on the x-axis
plt.figure()
plt.barh(range(len(area_by_day)), area_by_day)
plt.ylabel('day of week')
plt.xlabel('burned area (ha)')
plt.show()

## Chart Labels
# Make a scatter plot with the wind column of forest_fires on the x-axis and the area column of forest_fires on the y-axis
plt.figure()
plt.scatter(forest_fires['wind'], forest_fires['area'])
plt.title('Wind speed vs fire area')
plt.xlabel('Wind speed when fire started')
plt.ylabel('Area consumed by fire')
plt.show()


## Plot Aesthetics
# Switch to the "fivethirtyeight" style.
plt.style.use("fivethirtyeight")
# plt.style.use("ggplot")
# plt.style.use("dark_background")
# plt.style.use("bmh")

# Make a scatter plot the rain column of forest_fires on the x-axis and the area column of forest_fires on the y-axis
plt.figure()
plt.scatter(forest_fires['rain'], forest_fires['area'])
plt.title('Rain vs Area for forest fires')
plt.xlabel('rainfall when the fire occurred (mm/m2)')
plt.ylabel('Area consumed by fire (ha)')
plt.show()
