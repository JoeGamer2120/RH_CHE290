"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME: Josiah Schlabach
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


###############################################################################
# TODO 1: Define the function below to return the functional values for a
#         system of differential equations.
###############################################################################


def f(x, y, a):
    return -a


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

    ax.scatter(x, y, label="IVP")
    ax.plot(x, y_e, label="exact")
    ax.tick_params(direction="in")
    ax.set_xlim(0, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


###############################################################################
# TODO 2: Create a vector of equally-spaced x values from 0 to 1 using 21
#         total points.
###############################################################################
x_s = 0
x_e = 1
x_span = np.linspace(x_s, x_e, 21)

###############################################################################
# TODO 3: For this system, use a = 500 and Tmax = 450.
#         Use solve_ivp to get a solution.
###############################################################################
Tmax = 450
T_0 = Tmax
T_p = 0
a = 500
sol = solve_ivp(f, [x_s, x_e], [T_0, T_p], t_eval=x_span, args=(a,))


###############################################################################
# TODO 4: Store the result of the integration into its own variable.
###############################################################################
x = sol.t
T = sol.y

###############################################################################
# TODO 5: Create a vector of the analytical result.
###############################################################################
# T_an = -(a / 2) * x_span**2 + Tmax
T_an = -(a / 2) * x**2 + Tmax

###############################################################################
# TODO 6: Make a plot that compares the numerical and analytical results.
###############################################################################

make_plot(x_span, T, T_an)
