"""
This file will illustrate how to perform a numerical integration on a data set
using trapezoid and simpson in the integrate sub-module of SciPy.
"""

import numpy as np

###############################################################################
# IMPORTING TRAPEZOID AND SIMPSON
#
# When you intend to perform a numerical integration on a data set (instead of
# a function), import the 'trapezoid' or 'simpson' function from integrate in 
# SciPy.
###############################################################################

from scipy.integrate import trapezoid
from scipy.integrate import simpson

def main():
    ###########################################################################
    # CREATING THE DATA SET
    #
    # Below we are creating a data set of x and y values. For simplicity (and
    # comparison to an analytical result) we will use y = x^2 for a range of 0
    # to 1 with a dx = 0.1.
    ###########################################################################

    x = np.arange(0, 1.1, 0.1)
    y = x**2
    dx = 0.1
    
    run_trap(x, y)
    # run_simps_x(x, y)
    # run_simps_dx(y, dx)

###############################################################################
# TODO 1: Read the description below about the use of the function trapezoid. 
#         After you understand the function, run the program to see the result.
###############################################################################    
def run_trap(x, y):
    """
    The syntax for trapezoid is:
        I = trapezoid(y, x)
    
    where:
        I: result of the integration
        y: 'y' values of the data set
        x: 'x' values of the data set

    Parameters
    ----------
    x : ndarray
        The independent variable over which to perform the integration.
    y : ndarray
        The dependent variable over which to perform the integration.

    Returns
    -------
    None.

    """
    
    I = trapezoid(y, x)
    print("The result of the integration is:", I)
    print("The exact value is:", 1/3)

###############################################################################
# TODO 2: Read the description below about the use of the function simpson with
#         provided values of x. After you understand the function, uncomment 
#         the call to the function in main() and run the program to see the 
#         result.
###############################################################################

def run_simps_x(x, y):
    """
    The syntax for simpson is:
        I = simpson(y, x =, dx =)
    
    where:
        I: result of the integration
        y: 'y' values of the data set
        x: 'x' values of the data set; if no x-values are to be used, then
           use x = None (see run_simps_dx)
        dx: (optional) specify a spacing of x-values if discrete values are not
            specified

    Parameters
    ----------
    x : ndarray
        The independent variable over which to perform the integration.
    y : ndarray
        The dependent variable over which to perform the integration.

    Returns
    -------
    None.

    """
    I = simpson(y, x = x)
    print("The result of the integration is:", I)
    print("The exact value is:", 1/3)

###############################################################################
# TODO 3: Read the description below about the use of the function simpson with
#         a provided value of dx. After you understand the function, uncomment 
#         the call to the function in main() and run the program to see the 
#         result.
###############################################################################
    
def run_simps_dx(y, dx):
    """
    See description in run_simps_x above.

    Parameters
    ----------
    y : ndarray
        The dependent variable over which to perform the integration.
    dx : float
        The spacing to use for the x-values.

    Returns
    -------
    None.

    """
    I = simpson(y, x = None, dx = dx)
    print("The result of the integration is:", I)
    print("The exact value is:", 1/3)
    

main()