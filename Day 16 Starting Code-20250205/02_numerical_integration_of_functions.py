"""
This file will illustrate how to perform a numerical integration on a function
using quad in the integrate sub-module of SciPy.
"""

###############################################################################
# IMPORTING QUAD
#
# When you intend to perform a numerical integration on a function (instead of
# a data set), import the 'quad' function (short for 'quadrature') from 
# integrate in SciPy.
###############################################################################

from scipy.integrate import quad

def main():
    # simple_quad()
    quad_with_args()

###############################################################################
# DEFINING YOUR FUNCTION
#
# Define a function that contains the equation you intend to integrate. As a 
# simple illustration, we will use y = x^2
###############################################################################
def f(x):
    return x**2

###############################################################################
# QUAD
#
# The syntax of the quad function is:
#       I, err = quad(f, a, b)
#
# where:
#       I: the result of the integration
#       err: the estimated error in the result
#       f: the function to be integrated
#       a, b: the lower and upper limits of integration     
###############################################################################

###############################################################################
# TODO 1: After reading the provided explanations above, run the program to see 
#         the result of the function below.
###############################################################################

def simple_quad():
    I, err = quad(f, 0, 1)
    print("The exact value of the integral is:", 1/3)
    print("\nThe result of the numerical integration is:", I)
    print("\nThe estimated error is:", err)

###############################################################################
# TODO 2: The function to be integrated below has additional input arguments
#         that must be supplied in order to determine a numeric result.
#
#         Read the description in quad_with_args for how to supply these
#         values. After you have done so, uncomment the call to the function
#         quad_with_args in main() to see the results.
###############################################################################


def f2(x, a, b):
    return a*x**2 + b

def quad_with_args():
    """
    When the function you plan to integrate has additional input arguments 
    (beyond x), you can supply the values of those arguments by using
    the optional 'args' input to quad. As before, the arguments must be
    supplied in the form of a tuple.

    Returns
    -------
    None.

    """
    I, err = quad(f2, 0, 1, args = (2, -1))
    print("The exact value of the integral is:", -1/3)
    print("\nThe result of the numerical integration is:", I)
    print("\nThe estimated error is:", err)

main()