#!/usr/bin/env python
"""
This is a simple example of creating a 3D plot using matplotlib.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Configure the legend font size for all matplotlib plots
mpl.rcParams['legend.fontsize'] = 10

# Create a new figure
fig = plt.figure()

# An Axes3D object is created just like any other axes using the projection=‘3d’ keyword
ax = fig.add_subplot(111, projection='3d')
# NOTE: For older versions of matplotlib prior to 1.0.0, use this syntax:
# ax = Axes3D(fig)

# Generate a parametric curve
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# Plot the curve
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
