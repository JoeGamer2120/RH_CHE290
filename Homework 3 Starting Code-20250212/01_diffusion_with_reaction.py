"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME: Josiah Schlabach
"""

import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt


###############################################################################
# TODO 1: Complete f using the equations defined in the problem statement.
###############################################################################

def f(x, Ca):
    """
    Use this function to return the results of the system of differential 
    equations

    """
    D = 1.5 * 10**-6
    k = 5 * 10**-6
    return np.vstack((Ca[1], k*Ca[0]/D))

###############################################################################
# TODO 2: Complete bc using the boundary conditions defined in the problem
#         statement.
###############################################################################
    
def bc(ya, yb):
    """
    Use this function to return the residuals of the boundary conditions

    """
    return np.array([ya[0] - 0.1, yb[0]])

###############################################################################
# TODO 8: Complete the make_plot function according to the following 
#         specifications:
#
#           - Use points to represent the numerical solution.
#           - Use a line to represent the analytical solution.
#           - Create a legend that shows that the points represent the results
#             from "BVP" and the line represents the "exact" solution.
#           - Tick marks to the inside
#           - The x-axis ranges from 0 to 4.
#           - The label on the x-axis is 'x (cm)'.
#           - The label on the y-axis is 'cA (M)', where the A is subscripted.
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
    ax.set_xlim(0, 4)
    ax.set_xlabel("x (cm)")
    ax.set_ylabel("$c_A$")
    ax.legend()



###############################################################################
# TODO 3: Define an x-vector from 0 to 4 using a spacing of 0.25.
###############################################################################
x = np.arange(0, 4.25, 0.25)

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
y_bvp = sol.y[0]


###############################################################################
# TODO 7: Create a vector of values containing the analytical solution.
###############################################################################
ca0 = 0.1
k = 5 * 10**-6
D = 1.5 * 10**-6
L = 4
num = np.cosh(np.sqrt(k/D) * (L-x))
dem = np.cosh(np.sqrt(k/D) * L)

y_e = ca0 * (num/dem)


###############################################################################
# TODO 9: Send your results to make_plot to create a visualization of the
#         results.
###############################################################################
make_plot(x, y_bvp, y_e)
plt.show()