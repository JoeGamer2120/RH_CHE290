"""
This file demonstrates how to:
    - create a basic plot for a single series
    - how to modify the axes
    - how to save a figure to a file
"""

import matplotlib.pyplot as plt
import numpy as np


# Creating the dataset.
x = np.linspace(0, 2 * np.pi)
y = np.cos(x)


# Making a figure instance and an axis instance.
fig, ax = plt.subplots()

# Plotting the series on the axis instance.
ax.plot(x, y)
###############################################################################
# TODO 1: Read through the code to this point to understand what the code is
#         attempting to accomplish. Once you feel that you understand to code,
#         run the program.
#
#         To see the figure, you need to select the "Plots" tab in the "object
#         inspector" (the top-right panel).
###############################################################################

###############################################################################
# TODO 2: Uncomment the lines below and re-run the program. (You can uncomment
#         all of the lines or do so selectively.
#
#         Explanations of each line:
#           - By default, the axis tick marks are to the outside. The first
#             line sets the tick marks to the inside.
#           - To set the axis labels, use the command ax.set_xlabel("label")
#             for the x-axis or ax.set_ylabel("label") for the y-axis.
#           - To set the axis ranges, use ax.set_xlim(xmin, xmax) for the
#             x-axis or ax.set_ylim(ymin, ymax) for the y-axis.
###############################################################################

ax.tick_params(direction = 'in')
ax.set_xlabel("x")
ax.set_ylabel("cos(x)")
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

###############################################################################
# TODO 3: Uncomment the line below and re-run the program. This line
#         demonstrates how to save a figure to a file in the current folder.
#
#         figure_1.png is the name of the saved file.
#         dpi = 200 sets the size of the figure, which is larger than the
#                   default size.
###############################################################################

# fig.savefig("figure_1.png", dpi = 200)

plt.show()