"""
This file will illustrate how to use 'fsolve' in the 'optimize' module of SciPy
to solve for the solution of a system of non-linear equations.
"""

import numpy as np
from scipy.optimize import fsolve

###############################################################################
# TODO 1: Complete the function that contains the equations from the handout.
#         The function should return the results of both equations separately.
###############################################################################
def f(x):
    # x = x[0]
    # y = x[1]
    
    f1 = x[0]**2 + 3*x[1] - 5
    f2 = x[1]**2 + x[0] - 2
    return f1, f2

###############################################################################
# TODO 2: Use fsolve to find the solution to the system of equations. Use an
#         initial guess of x = 0 and y = 1.
#
#         On the next line, print the value of x and f(x).
###############################################################################
x = fsolve(f, [-1, -4])
print(x, f(x))

###############################################################################
# TODO 3: Re-run the code from TODO 4 with an initial guess of x = -1 and 
#         y = -4.
###############################################################################