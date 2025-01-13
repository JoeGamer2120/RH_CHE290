"""
This file will illustrate a variety of ways to define vectors using NumPy.
"""

import numpy as np


def main():
    """
    Uncomment the lines below when instructed by a TODO.
    """
    # arange_example()
    # linspace_example()
    # array_example()
    # ones_and_zeros_example()


###############################################################################
# ASSIGNING VECTORS (arange)
#
# For scientific computations, two ways to create a vector of regularly spaced
# values is by  using one of two NumPy functions: arange and linspace.
#
# arange is used to create a vector of values along a range.
#
# The syntax for arange is: np.arange(start, stop, step)
#   start is the value you want to start the range with
#   stop is the value where you want to stop (non-inclusive)
#   step is optional. If not specified, the increment is 1.
###############################################################################


def arange_example():
    """
    TODO 1: Uncomment the call to this function in main().
    """

    vec_a = np.arange(1, 9)
    vec_b = np.arange(9, 1, -1)
    vec_c = np.arange(1, 10, 3)

    print("The first arange example gives:\n", vec_a, "\n" )
    print("The second arange example gives:\n", vec_b, '\n' )
    print("The third arange example gives:\n", vec_c, '\n')

###############################################################################
# ASSIGNING VECTORS (linspace)
#
# linspace is used to create a vector of values that are equally spaced along
# the specified range.
#
# The syntax for linspace is: np.linspace(start, stop, num)
#   start is the first value on the range
#   stop is the last value on the range (inclusive)
#   num is the number of values to use. If not specified, 50 is used.
###############################################################################


def linspace_example():
    """
    TODO 2: Uncomment the call to this function in main().
    """

    vec_d = np.linspace(0, 1)
    vec_e = np.linspace(0, 1, 11)
    vec_f = np.linspace(1, -1, 21)

    print("The first linspace example gives:\n", vec_d, "\n")
    print("The second linspace example gives:\n", vec_e, '\n')
    print("The third linspace example gives:\n", vec_f, '\n')

###############################################################################
# ASSIGNING VECTORS (array)
#
# To define a vector without a well-defined sequence, you can use array.
#
# The syntax for array is: np.array([list of numbers])
#   Each number in this list should be separated by commas
###############################################################################


def array_example():
    """
    TODO 3: Uncomment the call to this function in main().
    """

    vec_g = np.array([1, 5, -2, 7, 6])

    print("The array example gives:\n", vec_g, "\n")


###############################################################################
# ASSIGNING VECTORS (zeros and ones)
#
# To create a vector that contains all 0s or 1s (for example, to initialize a
# vector), you can use the functions zeros or ones.
#
# The synatax of either is: np.zeros(shape)     or      np.ones(shape)
#   shape is an int for the number elements that will contain 0 or 1.
###############################################################################


def ones_and_zeros_example():
    """
    TODO 4: Uncomment the call to this function in main().
    """
    
    zeros_vec = np.zeros(5)
    ones_vec = np.ones(5)

    print("The zeros vector is:\n", zeros_vec, "\n")
    print("The ones vector is:\n", ones_vec, "\n")


main()
