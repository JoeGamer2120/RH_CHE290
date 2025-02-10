"""

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp


###############################################################################
# TODO 1: Complete f using the equations defined in class.
###############################################################################

def f(x, y):
    """
    Use this function to return the results of the system of differential 
    equations

    """
    return np.vstack((y[1], 2*y[1] - 0.75*y[0]))

###############################################################################
# TODO 2: Complete bc using the boundary conditions defined in class.
###############################################################################
    
def bc(ya, yb):
    """
    Use this function to return the residuals of the boundary conditions

    """
    return np.array([ya[0] - 2, ya[1] - 0.5])
    

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
    ax.set_ylabel("y")
    ax.legend()


###############################################################################
# TODO 3: Define an x-vector from 0 to 2 using 21 equally spaced points.
###############################################################################
x = np.linspace(0, 2, 21)


###############################################################################
# TODO 4: Define a y-matrix of zeros of size 2 x len(x).
###############################################################################
y = np.zeros( (2, len(x)) )


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
# TODO 7: Uncomment the line below to create a vector of the analytical solution.
###############################################################################

y_e = -0.5*np.exp(1.5*x) + 2.5*np.exp(0.5*x)


###############################################################################
# TODO 8: Send your results to make_plot to create a visualization of the
#         results.
###############################################################################
make_plot(x, y_BVP, y_e)

plt.show()
