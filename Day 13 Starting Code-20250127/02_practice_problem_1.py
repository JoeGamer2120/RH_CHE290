"""
See the separate handout for the equations to be used for this problem. 
"""

import numpy as np
import matplotlib.pyplot as plt

###############################################################################
# TODO 1: Define all of the provided constants below.
###############################################################################
Po = 1      #atm
To = 350    #k
gamma = 1.4
Cp = 1.021  #kJ/kg*K
m = 4.5     #kg

###############################################################################
# TODO 2: Create a vector of pressures ranging from P0 to 20 with steps of 0.5.
#         Use the pressure vector to create a corresponding temperature vector.
#         Once you have the temperature vector, create a work vector.
###############################################################################
P = np.arange(Po, 20, 0.5)

T = To * (P/Po)**((gamma-1)/gamma)
W = m * Cp * (T - To)


###############################################################################
# TODO 3: Create figure and axes instances.
###############################################################################
fig, ax1 = plt.subplots()
ax1.plot(P, T, color = 'black', ls = '-', lw = 2, label = "Temperature (K)")
ax1.set_ylabel('Temperature (K)', fontsize = 14)
ax1.set_xlabel('Pressure (atm)', fontsize = 14)
ax1.tick_params(direction = 'in')
ax1.set_ylim(0, 900)

ax2 = ax1.twinx()
ax2.plot(P, W, color = 'red', ls = '--', lw = 2, label = "Work (kJ)")
ax2.set_ylabel('Work (kJ)', fontsize = 14)
ax2.tick_params(direction = 'in')
ax2.set_ylim(0, 2500)

plt.show()




###############################################################################
# TODO 4: Create a plot with the following features:
#           - Two y-axes. The temperature on the primary y-axis and the work
#             on the secondary y-axis.
#           - The temperature should be a solid black line with a
#             linewidth of 2.
#           - The work should be a red dashed line with a linewidth of 2.
#           - The tick marks on all axes should be in.
#           - The primary y-axis label is: Temperature (K)  
#           - The secondary y-axis label is: Work (kJ)
#           - The x-axis label is: Pressure (atm)
#           - The font size for the axis labels should be 14 pt.
#               NOTE: this is just another argument to add to the label
#                     command. For example: fontsize = 10 sets the font to 10pt
#
#         See the handout for what the completed figure will look like.
###############################################################################

