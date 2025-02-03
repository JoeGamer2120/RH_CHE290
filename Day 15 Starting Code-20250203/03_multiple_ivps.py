"""
This file will demonstrate how to solve a systme of Initial Value Problems 
(IVPs).

To illustrate how to do this, we will use the following system of ODEs:
    
    y1' = -y1
    y2' = y1 - y2

where we now have to separate dependent variables, y1 and y2. We will use the
following set of initial conditions:

    y1(0) = 1
    y2(0) = 0
    
We know that the result of this set of differential equations upon integration 
are:
    
    y1 = exp(-t)
    y2 = t*exp(-t)

We can use these analytical results to verify that our code is working
correctly.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def main():
    multiple_odes()
    
    
###############################################################################
# ODE DEFINITION
#
# When defining a system of ODEs, the function definition is the same as before
# because the dependent variables (y1 and y2) will be treated as an array of
# values. As such, the function must return multiple values (the results of
# each differential equation). 
###############################################################################

def f(t, y): 
    return -y[0], y[0] - y[1]



def plot_multiple_series(t, y):
    fig, ax = plt.subplots()


    y1 = y[0]
    y2 = y[1]
    y1_exact = np.exp(-t)
    y2_exact = t*np.exp(-t)
    ax.scatter(t, y1, label = '$y_1$ IVP')
    ax.scatter(t, y2, label = '$y_2$ IVP')
    ax.plot(t, y1_exact, label = '$y_1$ exact')
    ax.plot(t, y2_exact, label = '$y_2$ exact')
    ax.legend()
    ax.tick_params(direction = "in")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    

def multiple_odes():
    """
    This function illustrates how to solve a system of ODEs.

    Returns
    -------
    None.

    """
    t_start = 0 
    t_stop = 10
    t_span = np.linspace(t_start, t_stop, 25)
    
    ###########################################################################
    # The function call below should look similar to those from before. The
    # only difference is that here the list of initial values correspond to
    # initial values of each dependent variable (y1 and y2, respectively).
    ##########################################################################
    
    initial_value = [1, 0]
    sol = solve_ivp(f, [t_start, t_stop], initial_value, t_eval = t_span)
    
    t = sol.t
    y = sol.y
    
    ###########################################################################
    # TODO 1: Run this code and observe the resulting plot. 
    ###########################################################################
    
    plot_multiple_series(t, y)
    plt.show()


main()
