"""
This file demonstrates how you can use solve_ivp to integrate a second-order
ODE.

For illustration, this code will use the example from the handout.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(x, y):
    return y[1], 2*y[1] - 0.75*y[0]

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
    ax.set_xlim(0, 2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()

###############################################################################
# Creating a vector of x values according the the problem specification.
###############################################################################
start = 0
stop = 2

x = np.linspace(start, stop, 21)

###############################################################################
# Defining the initial conditions, then using solve_ivp as before.
###############################################################################

y0 = 2
y0_prime = 0.5
sol = solve_ivp(f, [start, stop], [y0, y0_prime], t_eval = x)

###############################################################################
# Storing the result of the integration into the variable y. Note that the
# contains two solutions vectors; one for y and one for y' (in that order based
# on the function definition). Since we only care about y, that vector is
# stored in the first row of y (i.e., y[0]).
###############################################################################
y = sol.y[0]

###############################################################################
# Creating a vector of the analytical result.
###############################################################################
y_analy = -0.5*np.exp(1.5*x)+2.5*np.exp(x/2)

###############################################################################
# Making a plot that compares the numerical and analytical results.
###############################################################################
make_plot(x, y, y_analy)

