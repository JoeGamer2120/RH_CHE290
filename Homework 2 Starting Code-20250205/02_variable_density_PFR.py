"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME: Josiah Schlabach
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

###############################################################################
# TODO 1: Complete f using the equations in the handout to return a value of
#         conversion at a given tau.
#
#         NOTE: instead of trying to define a single equation, it may be easier
#               to define Ca and Cb separately, then return the result of the
#               function using those defined values.
###############################################################################

def f(t, X, Ca0, Cb0, k, delta):
    Ca = (Ca0 - Cb0 * X) / (1 + delta * X)
    Cb = (Cb0 * (1 - X))/ (1 + delta * X)
    return k * Ca * Cb / Cb0

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
t_s = 0
t_e = 900
t_span = np.linspace(t_s, t_e, 1801)

###############################################################################
# TODO 3: Create variables to define the provided constants (P, R, T, ya, yb
#         delta)
###############################################################################
P = 1.25        # atm
R = 0.08206     # L*atm/mol*K
T = 445         # K
ya = 0.5
yb = 0.25
delta = -0.25

###############################################################################
# TODO 4: Calculate the remaining quantities from the constants (Ca0, Cb0, k)
###############################################################################
Ca0 = (P / (R * T)) * ya
Cb0 = P / (R * T) * yb
k = 5 * np.exp(-1800 / T)

###############################################################################
# TODO 5: Use solve_ivp to determine a solution to the problem. Don't forget
#         that the conversion is initially zero.
###############################################################################
init = [0]
args = (Ca0, Cb0, k, delta)
sol = solve_ivp(f, [t_s, t_e], init, t_eval=t_span, args=args)

t = sol.t
C = sol.y

###############################################################################
# TODO 6: Use the results of the solution to create a plot using make_plot.
#         NOTES: 
#           - make_plot is already completed.
#           - a completed figure is included in the download for comparison.
###############################################################################
make_plot(t, C)

plt.show()






