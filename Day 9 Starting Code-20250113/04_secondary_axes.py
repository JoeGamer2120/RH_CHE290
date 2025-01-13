# -*- coding: utf-8 -*-
"""
This files illustrates how you can create a figure with different axes for 
multiple series that have different scales.
"""

import matplotlib.pyplot as plt
import numpy as np

# Creating the datasets
x = np.arange(1, 51)
y1 = x**1.5 - np.sqrt(x) + 4
y2 = np.tanh(x)/x

# Making a figure instance and an axis instance.
fig, ax = plt.subplots()
ax.plot(x, y1, lw = 2, color = "blue")
ax.plot(x, y2, lw = 2, color = "red")

###############################################################################
# TODO 1: The code above this TODO places both series on the same y-axis. Run
#         the program to see the resulting figure.
#
#         Because of the scale of the "y1" series, the "y2" series appears to
#         linear. Instead, we can plot each series on its own axis to see the
#         shape of each series.
###############################################################################

###############################################################################
# TODO 2: Uncomment the code below to see how to create a figure with a
#         secondary y-axis. 
###############################################################################

# # Making a new figure instance and a new axis instance.
# fig1, ax1 = plt.subplots()

# # Plotting the y1 series on the axis instance.
# #   NOTE: As illustrated below, you can create subscripts by placing the 
# #         characters in the name inside of $name$. The underscore (_) tells the
# #         program what characters to subscript. To superscript, you would
# #         replace the underscore with a caret (^).
# ax1.plot(x, y1, lw = 2, color = "blue", label = "$y_1$")
# ax1.set_ylabel("$y_1$")
# ax1.tick_params(direction = 'in')

# # To create a second y-axis, you will use the ax.twinx() method to create a 
# # second axis instance. You can then plot the second series on the new axis
# # instance.
# ax2 = ax1.twinx()
# ax2.plot(x, y2, lw = 2, color = "red", ls = "--", label = "$y_2$")
# ax2.set_ylabel("$y_2$")
# ax2.tick_params(direction = 'in')

# # Each axis instance has its own legend, thus, you will need to display each
# # legend separately. The placements below are used to place the legends in
# # cloase proximity.
# ax1.legend(bbox_to_anchor = (0.5, 1))
# ax2.legend(bbox_to_anchor = (0.5, 0.9))
