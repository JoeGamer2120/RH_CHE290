"""
This file will illustrate how to use 'fsolve' in the 'optimize' module of SciPy
to solve for the root of a non-linear equation (w and w/o arguments). 
"""
import numpy as np

###############################################################################
# TODO 1: Import fsolve from the optimize module of SciPy
###############################################################################
from scipy.optimize import fsolve

###############################################################################
# TODO 2: Write a function that contains the equation from the handout.
###############################################################################
def f(x):
    return x**2 - np.sin(x / 2)

###############################################################################
# TODO 4: Write a function that contains the equation from the handout that
#         requires input arguments.
###############################################################################
def f2(x, a, b):
    return np.sin(x) + a * np.cos(x) + b

###############################################################################
# TODO 3: Use fsolve to determine the root of the equation. Use an initial
#         guess of 0.4.
#
#         On the next line, print the value of x and f(x).
###############################################################################
x = fsolve(f, 0.4)
print(x, f(x))
# print(x[0], f(x[0]))
###############################################################################
# TODO 5: Use fsolve to determine the root of the equation that requires input
#         arguments. 
#           - Use an initial guess of -2.
#           - Use values of 3 and -2 for the input arguments.
#
#         On the next line, print the value of x and f(x).
###############################################################################
x2 = fsolve(f2, 2, args=(3, -2))
print(x2, f2(x2, 3, -2))

###############################################################################
# TODO 6: Re-run the code from TODO 4 with an initial guess of 2.
###############################################################################

    