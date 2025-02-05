"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME:
"""

import matplotlib.pyplot as plt

###############################################################################
# TODO 1: Complete f using the equations in the handout to return a value of
#         conversion at a given tau.
#
#         NOTE: instead of trying to define a single equation, it may be easier
#               to define Ca and Cb separately, then return the result of the
#               function using those defined values.
###############################################################################

def f(t, X, Ca0, Cb0, k, delta):
    return

def make_plot(t, y):
    """
    This function will make a plot of y vs. t for a single series. It will 
    create a scatter plot of the results of the ODE solver.

    Parameters
    ----------
    t : array
        The independent variable of the differential equation.
    y : array
        The dependent variable of the differential equation.

    Returns
    -------
    None.

    """
    
    fig, ax = plt.subplots()
    ax.scatter(t, y)
    ax.tick_params(direction = "in")
    ax.set_xlabel(" $\\tau (s)$")
    ax.set_ylabel("conversion")


###############################################################################
# TODO 2: The residence time for the reactor is 900 s. Create a vector of
#         equally spaced points over the span of the residence times.
###############################################################################


###############################################################################
# TODO 3: Create variables to define the provided constants (P, R, T, ya, yb
#         delta)
###############################################################################


###############################################################################
# TODO 4: Calculate the remaining quantities from the constants (Ca0, Cb0, k)
###############################################################################


###############################################################################
# TODO 5: Use solve_ivp to determine a solution to the problem. Don't forget
#         that the conversion is initially zero.
###############################################################################


###############################################################################
# TODO 6: Use the results of the solution to create a plot using make_plot.
#         NOTES: 
#           - make_plot is already completed.
#           - a completed figure is included in the download for comparison.
###############################################################################







