"""
Python does not have mathematical operations built-in beyond the basics. To 
utilize more 'complex' operations (e.g., transcentals, etc.), you must import
a library with those capabilities. Two common libraries are math and NumPy. 
While either of those libraries will suffice for most of these operations, this
file demonstrates the use of NumPy since we will use NumPy's functionality 
later in the course (this functionality is not available in the math library).
"""

import numpy as np

##############################################################################
# MORE MATHEMATICAL OPERATIONS
#
# Most mathematical operations beyond +, - , *, / and ** are not pre-defined 
# in Python. Therefore, you must first import a library that defines those
# operations. Two such libraries are math and NumPy. We will frequently use
# NumPy in this course because of its utility for scientific computing, so
# this material will use NumPy exclusively. However, some of these basic
# mathematical operations could also be completed using the math module instead.
#
#
# WHAT IS NUMPY?
#
# In short, NumPy is a powerful library for doing scientic computing. We will
# learn just a few of NumPy's capabilities throughout this course. The name
# NumPy is short for NUMerical PYthon. If you'd like to explore the 
# documentation for NumPy, you can visit:
#   https://numpy.org/   
# 
#
# HOW DO I IMPORT NUMPY (OR ANY LIBRARY)? 
#
# To import a library, you type an import command at the top of the program
# (usually below the doc-string, if one exists). Specifically, for NumPy the
# command is:
#    import numpy as np
#
# This code tells Python to import the module called numpy, and to call it np
# as a shortcut. If you wanted to import another library, you simply type
# import <library name>. There are some common "shortcuts" used for libraries.
# We will encounter those as needed.
#
# Once NumPy is imported, you can access any of the library's functions (more 
# on functions later) by typing np.<function name>. If you aren't sure of the
# name of a function, you can use the 'dot trick'. Notice that once you type
# np. a list of possible functions appear. You can scroll through the list, or
# you can limit the options by typing a letter.
#
# Example:
#   To take the square root of 16 and assign its value to a, you would write:
#       a = np.sqrt(16)
#
#   To test the dot trick, you could type a = np.sq then stop. You will notice
#   the list of options will be limited to: sqrt, square, squeeze, sq, Square.
#
# TODO 1: At the top of this program (below the doc-string) import NumPy.
# TODO 2: In the space below, assign the value of pi to a variable named my_pi.
#         Pi is part of NumPy and can be called using np.pi. On next line,
#         print the result of np.cos(my_pi). 
#         NOTE: you do have to assign the result of the calculation to a 
#               variable to print its result.
##############################################################################

my_pi = np.pi
print(np.cos(my_pi))
print()

##############################################################################
# USEFUL MATHEMATICAL OPERATIONS IN NUMPY
#
# Below is a list of some common mathematical operations and their NumPy syntax:
#   Square Root:    np.sqrt(value)
#   Power:          np.power(a,b)       (same as a**b)
#   Sine:           np.sin(value)
#   Cosine:         np.cos(value)
#   Tangent:        np.tan(value)
#   Exponential:    np.exp(value)
#   Natural Log:    np.log(value)
#   Log base 10:    np.log10(value)
#
#
# TODO 3: Uncomment the lines below this TODO to see the output of each of
#         operations.
#
##############################################################################

print()
print("The square root of 2 is", np.sqrt(2))
print("2 raised to 3rd power is", np.power(2,3))
print("The sin of pi/2 is", np.sin(np.pi/2))
print("The exponential of 2 is", np.exp(2))
print("The natural log of 2 is", np.log(2))
print("The log10 of 2 is:", np.log10(2))


