"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME:
"""


import matplotlib.pyplot as plt


###############################################################################
# TODO 1: Define the function below to return the functional values for a 
#         system of differential equations.
###############################################################################

def f(x, y, a):
    return

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
    
    ax.scatter(x, y, label = "IVP")
    ax.plot(x, y_e, label = "exact")
    ax.tick_params(direction = "in")
    ax.set_xlim(0, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

###############################################################################
# TODO 2: Create a vector of equally-spaced x values from 0 to 1 using 21 
#         total points.
###############################################################################


###############################################################################
# TODO 3: For this system, use a = 500 and Tmax = 450. 
#         Use solve_ivp to get a solution.
###############################################################################



###############################################################################
# TODO 4: Store the result of the integration into its own variable.
###############################################################################


###############################################################################
# TODO 5: Create a vector of the analytical result.
###############################################################################


###############################################################################
# TODO 6: Make a plot that compares the numerical and analytical results.
###############################################################################


