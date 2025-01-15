"""
This file demonstrates two ways to make a plot with multiple series. It also
demonstrates how to created a legend to differentiate between the series.
"""

import matplotlib.pyplot as plt
import numpy as np

# Creating the datasets
x = np.linspace(0, 2 * np.pi)
y1 = np.cos(x)
y2 = np.sin(x)

# Making a figure instance and an axis instance.
# fig, ax = plt.subplots()

# Plotting both series on the axis instance.
# ax.plot(x, y1)
# ax.plot(x, y2)

# Setting the ticks to the inside and labeling the axes.
# ax.tick_params(direction = 'in')
# ax.set_xlabel("x")
# ax.set_ylabel("f(x)")

###############################################################################
# TODO 1: Read through the code to this point to understand what the code is
#         attempting to accomplish. This method uses ax.plot for each series
#         individually to place both series on the same plot. Once you
#         understand what the code is attempting to accomplish, run the program
#         and observe the resulting figure.
###############################################################################

###############################################################################
# TODO 2: The figure creating above results in two series on the same figure;
#         however, you may not know which is which. To create a legend of the
#         series, you must first 'label' each data set. Then, you can use the
#         ax.legend() command to display the legend.
#
#         Uncomment the lines below this TODO to achieve this goal.
#
#         NOTE: we can create a new figure the same way as before by using
#               fig, ax = plt.subplots(), but by giving the figure and axes
#               different names than the first figure. Now, all commands must
#               refer to the new axes instance.
###############################################################################

# # Making a new figure instance and a new axis instance.
# fig2, ax2= plt.subplots()

# # Plotting both series on the new axis instance with labels for the series.
# ax2.plot(x, y1, label = "cos(x)")
# ax2.plot(x, y2, label = "sin(x)")

# # Setting the ticks to the inside, labeling the axes and displaying the legend.
# ax2.tick_params(direction = 'in')
# ax2.set_xlabel("x")
# ax2.set_ylabel("f(x)")
# ax2.legend()

###############################################################################
# TODO 3: The two previous TODOs illustrated how to place two data sets on the
#         same figure by writing two separate commands. Another method for
#         putting multiple series on the same figure involves creating an
#         array of y-values, then using a for loop to plot each series, as
#         illustrated by the code below this TODO.
#
#         You can also create an array of arguments to be used for each series.
#         In the example below, a series of 'labels' is used to create a legend
#         as in the previous TODO.
#
#         The 'bbcox_to_anchor' is used to set the location of the legend.
#         The coordinates (0,0) is the bottom left, and (1,1) is the top right.
###############################################################################

# # Making a new figure instance and a new axis instance.
fig3, ax3 = plt.subplots()

# # Creating an array of the data. The data series will be contained in the rows
# # of the array.
y_series = np.array([y1, y2])

# # Creating a list of the labels.
labels = ["cos(x)", "sin(x)"]

# # Using a for loop to place each data series on the new figure.
for i in range(len(y_series)):
    ax3.plot(x, y_series[i], label=labels[i])

# # Setting the ticks to the inside, labeling the axes and displaying the legend
# # at x = 0.5 (middle of the figure) and y = 1 (the top of the figure)
ax3.tick_params(direction="in")
ax3.set_xlabel("x")
ax3.set_ylabel("f(x)")
ax3.legend(bbox_to_anchor=(0.5, 1))


plt.show()

