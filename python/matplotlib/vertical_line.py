#!/usr/bin/env python
"""
Example of using plt.axvline() to plot a a vertical line on a Matplotlib plot.
"""
import numpy as np
import matplotlib.pyplot as plt

values = np.random.randn(100)
plt.hist(values, label='values')
plt.axvline(values.mean(), color='red', linestyle='--', linewidth=4, label='mean')
plt.legend()
plt.show()
