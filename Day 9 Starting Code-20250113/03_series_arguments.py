"""
This file illustrates some of the various arguments that can be used with
data series.
"""

import matplotlib.pyplot as plt
import numpy as np

###############################################################################
# TODO 1: Read through the code below to understand what the code is 
#         attempting to accomplish. Once you understand what the code is 
#         attempting to accomplish, run the program and observe the resulting 
#         figure.
###############################################################################

# Creating the dataset
x = np.linspace(0, 2*np.pi)
y = np.cos(x)

# Making a figure instance and an axis instance.
fig, ax = plt.subplots()
  
# Creating a list of colors.  
colors = ['black', 'green', 'red', 'blue']

# Creating a list of line widths
lws = [0.5, 1, 1.5, 2]

# Creating a list of line styles
lss = ["-", "--", ":", "-."]

# Placing each data series with different arguments on the same figure. The
# same data series is used each time but is shifted by the index, n.    
for n in range(len(colors)):
    ax.plot(x, y + n, color = colors[n], lw = lws[n], ls = lss[n])

# Setting the ticks to the inside
ax.tick_params(direction = 'in')

plt.show(block=True)