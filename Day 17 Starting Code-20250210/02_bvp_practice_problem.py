"""
Complete the problem as defined in the separate handout.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp


###############################################################################
# TODO 1: Complete f using the equations defined in class.
###############################################################################

def f(x, T):
    """
    Use this function to return the results of the system of differential 
    equations

    Don't forget that you need to define the equations constants inside of this
    function definition
    """
    a = 1000
    L = 2
    return np.vstack((T[1], -a * (1 - x/L))) 

###############################################################################
# TODO 2: Complete bc using the boundary conditions defined in class.
###############################################################################
    
def bc(ya, yb):
    """
    Use this function to return the residuals of the boundary conditions

    """

    return np.array([ya[0], yb[1]])


def make_plot(x, y, y_e):
    """
    You do not need to modify this function.

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
    ax.set_xlim(0, 2)
    ax.set_xlabel("x")
    ax.set_ylabel("T")
    ax.legend()


###############################################################################
# TODO 3: Define an x-vector from 0 to 2 using 21 equally spaced points.
###############################################################################
x = np.linspace(0, 2, 21)

###############################################################################
# TODO 4: Define a y-matrix of zeros of size 2 x len(x).
###############################################################################
y = np.zeros((2, len(x)))

###############################################################################
# TODO 5: Create a solution object using solve_bvp
###############################################################################
sol = solve_bvp(f, bc, x, y)

###############################################################################
# TODO 6: Store the numeric solution for y in a variable (do not use the same
#         variable name that you used for the "zero" matrix in TODO 4).
###############################################################################
x = sol.x
y_BVP = sol.y[0]



###############################################################################
# TODO 7: Create a vector of the analytical solution.
###############################################################################
a = 1000
L = 2
y_e = ((a * L**2) / 2) * (x / L - (x/L)**2 + (1/3)*(x/L)**3)


###############################################################################
# TODO 8: Send your results to make_plot to create a visualization of the
#         results.
###############################################################################
make_plot(x, y_BVP, y_e)
plt.show()



