"""
This file will demonstrate how to solve Initial Value Problems (IVPs) using
the solve_ivp function in the integrate sub-module of SciPy.

To illustrate the functionality of solve_ivp, this code will use a simple
example function for which we can get an analytical solution. The function
used for illustration purposes is:
    
    y' = t^2

where y' is used to represented dy/dt. We know that the result of this
differential equation upon integration is:
    
    y = (1/3)t^3 + C

where C (the constant of integration) is determined by the INITIAL VALUE (thus,
making this and Initial Value Problem).
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Another option for importing functions from sub-modules (instead of importing
the whole sub-module and calling the function) is to only import the desired
function.

This option is illustrated below where we are saying to only import solve_ivp
from the sub-module 'integrate' of 'SciPy' (i.e., from scipy.integrate)
"""

from scipy.integrate import solve_ivp

def main():
    # basic_ivp()
    # ivp_with_times()
    ivp_with_multiple_initial_values()
    
    
###############################################################################
# ODE DEFINITION
#
# To use solve_ivp, we need to define a function or functions that represent
# the ODE(s) that we are attempting to solve. We will start with one ODE.
#
# The arguments MUST be placed in the "independent", "dependent" order. For
# example, since our ODE is of the form dy/dt, t is the independent variable
# and y is the dependent variable. If we had an ODE of the form dy/dx, the
# order would be (x, y).
#
# We will handle the possibility of additional input arguments later.
###############################################################################

def f(t, y): 
    return t**2

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
    y_exact = t**3/3
    
    fig, ax = plt.subplots()
    ax.scatter(t, y, label = 'IVP solution')
    ax.plot(t, y_exact, label = 'exact solution')
    ax.legend()
    ax.tick_params(direction = "in")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    plt.show()

def plot_multiple_series(t, y, C):
    """
    This function will make a plot of y vs. t for a multiple series with
    different constants of integration. It will create scatter plots of the 
    results of the ODE solver and lines of the exact solution for comparison.

    Parameters
    ----------
    t : array
        The independent variable of the differential equation.
    y : array
        The dependent variable of the differential equation.
    C : float
        The constant of integration (i.e., the initial condition).

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()

    for i in range(len(C)):
        y_exact = t**3/3 + C[i]
        ax.plot(t, y_exact, label = "C = " + str(C[i]))
        ax.scatter(t, y[i], label = "C = " + str(C[i]))
    ax.legend()
    ax.tick_params(direction = "in")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    plt.show
    
def basic_ivp():
    """
    This function illustrates the basic structure of using solve_ivp.

    Returns
    -------
    None.

    """
    ###########################################################################
    # The basic syntax of solve_ivp is:
    #   sol = solve_ivp(f, t_span, y0)
    #
    #   - f: the differential equation to solve
    #   - t_span: the span/range of the independent variable to integrate over.
    #   - y0: the initial value (i.e, y(t = 0))
    #   - sol: an object of the results of the function
    #
    # We could put the values for t_span and y0 into the function call
    # directly, but we are going to define those values in variables
    # that we will place into the function instead.
    #
    # Note that since the span contains two values, we must pass those values
    # as either a list or a tuple
    ###########################################################################
    
    t_start = 0 
    t_stop = 10
    initial_value = 0
    
    ###########################################################################
    # TODO 1: Run the program.
    #
    #         You should get a ValueError because, even though we are only 
    #         using a single value for y0, we must still pass it as a list or 
    #         a tuple.
    ###########################################################################
    
    # sol = solve_ivp(f, [t_start, t_stop], initial_value)
    
    ###########################################################################
    # TODO 2: Comment out the function call above (below TODO 1) and uncomment
    #         the line below this TODO. Run the program.
    #
    #         You can see the resulting plot displayed.
    #
    #         See comments below for additional explanations.
    ###########################################################################    
    
    sol = solve_ivp(f, [t_start, t_stop], [initial_value])
    
    ###########################################################################
    # The resulting independent variable values are stored in the t variable of
    # the solution object, and dependent variable is stored in the y variable.
    #
    # Below, those values are stored in their own variables to make passing 
    # the variables to the plot function more readable.
    ###########################################################################
    
    t = sol.t
    y = sol.y
    
    ###########################################################################
    # While the numerical solution and exact solution line up, the shape of the
    # curve does not display a representative shape. In this example, we
    # allowed the solver to determine the number of points to use in the
    # solution.
    ###########################################################################

    ###########################################################################
    # TODO 3: Uncomment the line below and run the program to see the number of 
    #         points used by the solver.
    ###########################################################################    
    print(len(t))
    
    ###########################################################################
    # TODO 4: Uncomment the line below and run the program to see the values 
    #         of the points used by the solver.
    ###########################################################################    
    print(t)
  
    ###########################################################################
    # The line below calls the make_plot function to create a plot of the 
    # results. The line below it (commented out) shows how you could create use
    # the results directly from the solution object without defining variables
    # first. If you choose to uncomment the last line of this function, you 
    # will see the same plot.
    ###########################################################################

    make_plot(t, y)
    # make_plot(sol.t, sol.y)
    plt.show()

def ivp_with_times():
    """
    This function illustrates how to use the optional input of t_eval to create
    a solution for a set range of the independent variable.

    Returns
    -------
    None.

    """
    t_start = 0 
    t_stop = 10
    
    ###########################################################################
    # If we want to determine a solution of the differential equation at 
    # specified values, we can first create an ndarray of those values that 
    # we can then pass into the function.
    #
    # Below is one example of creating such an array using np.linspace.
    ###########################################################################
    t_span = np.linspace(t_start, t_stop, 10)
    
    initial_value = 0
    
    ###########################################################################
    # To use the newly created values of t with the solver, we can use the
    # optional function input 't_eval' as written below.
    ###########################################################################
    
    sol = solve_ivp(f, [t_start, t_stop], [initial_value], t_eval = t_span)
    
    t = sol.t
    y = sol.y

    ###########################################################################
    # TODO 5: Comment out the call to basic_ivp() in main(), and uncomment the
    #         call to this function (ivp_with_times) in main(). Run the program
    #         a check the newly created plot to observe the results.
    ###########################################################################    

    make_plot(t, y)

def ivp_with_multiple_initial_values():
    """
    This function illustrates how to get a solution with multiple initial
    conditions.

    Returns
    -------
    None.

    """
    t_start = 0 
    t_stop = 10
    t_span = np.linspace(t_start, t_stop, 10)
    
    ###########################################################################
    # To use multiple initial values, you simply supply as list or tuple of
    # values for the y0 argument.
    #
    # Here, the variable initial_guess does not have to be contained in
    # brackets in the function call because the variable is already defined
    # as a list of values.
    ###########################################################################
    
    initial_value = [0, 20, 40]
    sol = solve_ivp(f, [t_start, t_stop], initial_value, t_eval = t_span)
    
    t = sol.t
    y = sol.y
    
    ###########################################################################
    # TODO 6: Comment out the call to ivp_with_times() in main(), and uncomment
    #         the call to this function (ivp_with_multiple_initial_values) in 
    #         main(). Run the program a check the newly created plot to observe 
    #         the results.
    ###########################################################################
    
    plot_multiple_series(t, y, initial_value)
    plt.show()


main()
