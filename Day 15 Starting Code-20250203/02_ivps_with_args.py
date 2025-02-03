"""
This file will demonstrate how to solve Initial Value Problems (IVPs) when the
function containing ODE has additional input arguments beyond "t" and "y".

Here, we will use an analogous equation as in the previous file with an
additional constant, a:
    
    y' = at^2

where y' is used to represented dy/dt. We know that the result of this
differential equation upon integration is:
    
    y = (a/3)t^3 + C

where C (the constant of integration) is determined by the INITIAL VALUE (thus,
making this and Initial Value Problem).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def main():
    ivp_with_arguments()
    
    

def f(t, y, a): 
    return a*t**2

def make_plot(t, y):
    """
    This function will make a plot of y vs. t for a single series. It will 
    create a scatter plot of the results of the ODE solver and a line of the
    exact solution for comparison.

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
    
    y_exact = t**3
    
    fig, ax = plt.subplots()
    ax.scatter(t, y, label = 'IVP solution')
    ax.plot(t, y_exact, label = 'exact solution')
    ax.legend()
    ax.tick_params(direction = "in")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    
def ivp_with_arguments():
    """
    This function illustrates how to supply additional arguments to the
    function, f, when they are required for function execution.

    Returns
    -------
    None.

    """
    
    t_start = 0 
    t_stop = 10
    t_span = np.linspace(t_start, t_stop, 10)
    
    initial_value = 0
    
    ###########################################################################
    # When we need to supply additional arguments for f to function properly,
    # we use the optional 'args' syntax. This option requires a tuple to be
    # provided, which is why there is (3, ) used below even though f only 
    # has a single additional input argument (a).
    ###########################################################################
    sol = solve_ivp(f, [t_start, t_stop], [initial_value], t_eval = t_span,
                    args = (3, ))
    
    t = sol.t
    y = sol.y

    ###########################################################################
    # TODO 1: Run this code and observe the resulting plot. If you'd like to
    #         try different values of a, you need to make the appropriate 
    #         changes to the exact solution in the make_plot function as the
    #         current equation is based on a = 3.
    ###########################################################################

    make_plot(t, y)
    plt.show()


main()


