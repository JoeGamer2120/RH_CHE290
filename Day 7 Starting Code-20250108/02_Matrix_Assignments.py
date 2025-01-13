"""
This file will illustrate a variety of ways to define matrices using NumPy.
"""


import numpy as np

def main():
    """
    Uncomment the lines below when instructed by a TODO.
    """
    # matrix_example_1()
    # matrix_example_2()
    # matrix_reshape()
    # ones_and_zeros_example()
    # identity_matrix_example()


###############################################################################
# ASSIGNING MATRICES
#
# Defining a matrix is similar to defining a vector; however, a matrix contains
# m vectors of length n. 
# 
# Two possible ways to define a matrix are:
#   - Define each element individually (see matrix__example_1). Note that each
#     row is contained within brackets all rows are contained within another
#     set of brackets.
#
#   - Define each row individually using an acceptable method, then defining 
#     the matrix using the already defined rows (see matrix_example_2).
#     Note that the collection of vector variables are all contained within
#     brackets.
#
# Each row in the matrix MUST have the same number of elements or you will get
# a TypeError.
###############################################################################


def matrix_example_1():
    """
    TODO 1: Uncomment the call to this function in main().
    """
    
    matrix_a = np.array([[1, 2], [3, 4], [5, 6]])
    matrix_b = np.array([[1, 2, 3], [4, 5, 6]])
        
    print("This matrix example gives:\n", matrix_a,"\n")
    print("and:\n", matrix_b,"\n")

def matrix_example_2():
    """
    TODO 2: Uncomment the call to this function in main().
    """
    
    r_1 = np.linspace(1, 3, 3)
    r_2 = np.linspace(4, 6, 3)
    r_3 = np.linspace(7, 9, 3)
    
    matrix_c = np.array([r_1, r_2, r_3])
    print("This matrix example gives:\n", matrix_c,"\n")

###############################################################################
# ASSIGNING MATRICES (reshaping)
#
# Another way to create a matrix is to create a vector (for example, using
# arange), then reshaping the vector into a matrix.
#
# The syntax for reshape is: variable_name.reshape(n_rows, n_columns)
###############################################################################

def matrix_reshape():
    """
    TODO 3: Uncomment the call to this function in main().
    """
    
    matrix_c = np.arange(1, 10)
    print("The original vector is: \n", matrix_c)
    matrix_c = matrix_c.reshape(3,3)
    print("\nThe reshaped matrix is:\n",matrix_c)

###############################################################################
# ASSIGNING MATRICES (zeros and ones)
#
# To create a matrix that contains all 0s or 1s (for example, to initialize a
# matrix), you can use the functions zeros or ones.
#
# The synatax of either is: np.zeros(shape)     or      np.ones(shape)
#   shape is an tuple of ints for the number rows and columns that will 
#   contain 0 or 1.
###############################################################################

def ones_and_zeros_example():
    """
    TODO 4: Uncomment the call to this function in main().
    """
    
    zeros_matrix = np.zeros((4,3))
    ones_matrix = np.ones((3,4))
    
    print("The zeros matrix is:\n", zeros_matrix)
    print("\nThe ones matrix is:\n", ones_matrix)

###############################################################################
# ASSIGNING AN IDENTITY MATRIX
#
# If you need to define an identity matrix (1s along the diagonal with 0s 
# everywhere else), you can use the funtion identity. 
#
# The synatax this function is: np.identity(n)
#   n is an int for the number of rows (and colmumns) to create.
###############################################################################

def identity_matrix_example():
    """
    TODO 5: Uncomment the call to this function in main().
    """
    
    identity = np.identity(4)
    print("This identity matrix is:\n", identity)
    
    
main()  
