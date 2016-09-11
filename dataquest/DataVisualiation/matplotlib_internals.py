#!/usr/bin/env python
"""
You can make plots easily using high-level API functions within Pandas, Seaborn, or Matplotlib.
But under the hood they all rely on the low-level APIs within Matplotlib.  Knowing the internals of
Matplotlib can allow you to customize your plots to maximize their impact and visual appeal.
"""
import matplotlib.pyplot as plt
import numpy as np


# Enable interactive mode so plt.show() won't block
plt.ion()

# 2 simple lists of values
month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

# Create a simple scatter plot using a higher level Matplotlib method
plt.scatter(month, temperature)
plt.show()

# The most commonly used Matplotlib functions are the high-level stateful ones like scatter() used
# above.  These all work the way MATLAB does and are rather non-Pythonic.  Matplotlib also has an
# object-oriented API which is at a little bit lower level of abstraction and is much more Pythonic.

# Figure is the top-level Matplotlib object that manages the entire plotting area. A Figure instance
# acts as a container for your plots and contains some useful parameters and methods.

# Subplot is the Matplotlib object that you use to create the axes for a plot. While a Figure can
# contain multiple subplots that are laid out on a grid, we'll start with just one plot.

# Instantiate a new Figure instance (width: 5 inches, height: 7 inches) and assign to variable fig
fig = plt.figure(figsize=(5,7))
# Call .add_subplot() on the Figure instance to add an empty plot and assign the subplot to var ax
ax = fig.add_subplot(1,1,1)
# Call plt.show() to display our creation (which isn't plotting anything yet)
plt.show()
# You'll notice that the plot has a width to height ratio of 5 to 7, contains only 1 plot, and both
# the x and y axes ticks run from 0.0 to 1.0.

# Print the types
print(type(fig))
print(type(ax))

# A Subplot is an abstraction that creates an Axes object whenever you call .add_subplot().
# An Axes object controls how the plotting actually happens. The Axes object describes what's
# actually inside the plot we're interested in (like the points in a scatter plot) and also
# describes the x and y axes, including the ticks, labels, etc.

# While each Figure instance can contain multiple plots, and therefore multiple Axes objects, that
# specify how each plot looks, each unique Axes object can only belong to one figure. Subplots and
# Axes are synonomous for our purposes, but working with Subplots is a much cleaner and convenient interface.

# We can manaully set the axis limits
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month), np.max(month)])
ax.set_ylim([np.min(temperature), np.max(temperature)])
plt.show()

# We now need to graph the actual dots in the scatter plot using the 2 list objects from before, month and temperature
# The Axes object we created contains a method called .scatter() that generates points for each combination of values on the plot.
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month),np.max(month)])
ax.set_ylim([np.min(temperature), np.max(temperature)])

color = 'darkblue'
marker = 'o'

# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color=color, marker=marker)
plt.show()

# Our scatter plot is almost ready! We're missing a few things however:
# - The axes ticks we set were too tight and caused the first and last points in our plot to be cut off
# - The axes are missing names, or labels, that describe what the values represent
# - The plot is missing a title
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month) - 1, np.max(month) + 1])
ax.set_ylim([np.min(temperature) * 0.9, np.max(temperature) * 1.1])

color = 'darkblue'
marker = 'o'

# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color='darkblue', marker='o')
ax.set_xlabel('Month')
ax.set_ylabel('Temperature')
ax.set_title('Year Round Temperature')
plt.show()


# In the previous code cell, we painstakingly specified each property we wanted for the plot using
# different methods, all starting with set_, for each one. Matplotlib thankfully has a .set() method
# that we can use to specify all the attributes we want that Axes object to have in the parameters
# of that function call.
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set(xlim=(0,13), ylim=(10,110), xlabel='Month', ylabel='Temperature', title='Year Round Temperature')
ax.scatter(month, temperature, color='darkblue', marker='o') #add xlabel, ylabel, and title
plt.show()


## Multiple Subplots
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


## Adding data to multiple subplots
month_2013 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2013 = [32,18,40,40,50,45,52,70,85,60,57,45]
month_2014 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2014 = [35,28,35,30,40,55,50,71,75,70,67,49]

fig = plt.figure()
# Generate a grid of plots, 2 columns by 1 row
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# Both plots have the same x and y axes rnages
x_axis = (0, 13)
y_axis = (10, 110)

# The left plot is a scatter plot with month2013 on the x-axis and temperature_2013 on y
ax1.scatter(month_2013, temperature_2013, color='darkblue', marker='o')
ax1.set(title='2013', xlim=x_axis, ylim=y_axis, xlabel='Month', ylabel='Temperature')

# The right plot is a scatter plot with month2014 on the x-axis and temperature_2014 on y
ax2.scatter(month_2014, temperature_2014, color='darkgreen', marker='o')
ax2.set(title='2014', xlim=x_axis, ylim=y_axis, xlabel='Month', ylabel='Temperature')

# prevent overlap of axes labels and such
plt.tight_layout()

plt.show()


## Adding multiple data items to a single subplot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# The 1st plot is a scatter plot with month2013 on the x-axis and temperature_2013 on y
ax.scatter(month_2013, temperature_2013, color='darkblue', marker='o', label='2013')

# The 2nd plot is a scatter plot with month2014 on the x-axis and temperature_2014 on y
ax.scatter(month_2014, temperature_2014, color='darkgreen', marker='d', label='2014')

# Both pices of data on same subplot share axes properties
ax.set(title='Year Round Temperature', xlim=x_axis, ylim=y_axis, xlabel='Month', ylabel='Temperature')

# We can add a legend to show what is what
ax.legend()

# Show the figure
plt.show()
