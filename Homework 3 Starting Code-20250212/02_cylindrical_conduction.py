"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME: Josiah Schlabach
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

### GLOBAL VARIABLE DECLARATION
ri = 1 
r0 = 2 
k = 0.1 
q = 5
Ts = 50



###############################################################################
# TODO 1: Complete f using the equations defined in the problem statement.
###############################################################################

def f(r, T):
    """
    Use this function to return the results of the system of differential 
    equations

    """
    return np.vstack((T[1], -1/r * T[1] - q/k))

###############################################################################
# TODO 2: Complete bc using the boundary conditions defined in the problem
#         statement.
###############################################################################
    
def bc(ya, yb):
    """
    Use this function to return the residuals of the boundary conditions

    """
    return np.array([ya[1], yb[0] - Ts])

###############################################################################
# TODO 8: Complete the make_plot function according to the following 
#         specifications:
#
#           - Use points to represent the numerical solution.
#           - Use a line to represent the analytical solution.
#           - Create a legend that shows that the points represent the results
#             from "BVP" and the line represents the "exact" solution.
#           - Tick marks to the inside
#           - The x-axis ranges from 1 to 2.
#           - The label on the x-axis is 'r (cm)'.
#           - The label on the y-axis is 'T (oC)', where the o is superscripted.
###############################################################################

def make_plot(x, y, y_e):
    """
    This function creates a plot of the results.

    Parameters
    ----------
    x : ndarray
        A vector of independent values.
    y : ndarray
        A vector of dependent values from the numeric solution.
    y_e : ndarray
        A vector of dependent values from the exact solution.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    
    ax.scatter(x, y, label = "BVP")
    ax.plot(x, y_e, label = "exact")
    ax.tick_params(direction = "in")
    ax.set_xlim(1, 2)
    ax.set_xlabel("r (cm)")
    ax.set_ylabel("$T (^{o}C)$")
    ax.legend()


###############################################################################
# TODO 3: Define an x-vector from 1 to 2 using a spacing of 0.05.
###############################################################################
x = np.arange(1, 2.05, 0.05)


###############################################################################
# TODO 4: Define a y-matrix of zeros of appropriate size
###############################################################################
y = np.zeros((2, len(x)))

###############################################################################
# TODO 5: Create a solution object using solve_bvp
###############################################################################
sol = solve_bvp(f, bc, x, y)

###############################################################################
# TODO 6: Store the numerical solution for y in a variable (do not use the same
#         variable name that you used for the "zero" matrix in TODO 4).
###############################################################################
T_bvp = sol.y[0]

###############################################################################
# TODO 7: Create a vector of values containing the analytical solution.
###############################################################################
term1 = ((q * r0**2) / (4 * k)) * (1 - (x/r0)**2)
term2 = ((q*ri**2) / (2*k)) * np.log(x / r0)

T = term1 + term2 + Ts


###############################################################################
# TODO 9: Send your results to make_plot to create a visualization of the
#         results.
###############################################################################
make_plot(x, T_bvp, T)
plt.show()
