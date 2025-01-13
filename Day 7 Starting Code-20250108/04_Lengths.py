"""
This file will illustrate how to determine the lengths of vectors and matrices.
"""

import numpy as np

def main():
    """
    Uncomment the lines below when instructed by a TODO.
    """
    # vector_length()
    matrix_len()

###############################################################################
# DETERMINING THE LENGTH OF A VECTOR
#
# To determine the length of a vector, you can use len.
#
# The syntax for len is: len(array name)
###############################################################################

def vector_length():
    """
    TODO 1: Uncomment the call to this function in main() to see the use of len 
            for some previously defined vectors.    
    """
    vec_a = np.arange(1, 9)
    vec_b = np.arange(9, 1, -1)
    vec_c = np.arange(1, 10, 3)
    vec_d = np.linspace(0, 1)
    vec_e = np.linspace(0, 1, 11)
    vec_f = np.linspace(1, -1, 21)
    vec_g = np.array([1, 5, -2, 7, 6])
    

    print("The first arange example vector has", len(vec_a), "elements")
    print("The second arange example vector has", len(vec_b), "elements")
    print("The third arange example vector has", len(vec_c), "elements")
    print()
    print("The first linspace example vector has", len(vec_d), "elements")
    print("The second linspace example vector has", len(vec_e), "elements")
    print("The third linspace example vector has", len(vec_f), "elements")
    print()
    print("The 'array' example vector has", len(vec_g), "elements")

###############################################################################
# DETERMINING THE LENGTH OF A MATRIX
#
# Use of len on a matrix will return the number of rows in the matrix. If you
# want to determine the number of columns in a matrix, you can use len on any
# row of the matrix.
###############################################################################
def matrix_len():
    """
    TODO 2: Uncomment the call to this function in main() to see the use of len 
            for the previously defined matrices.    
    """
    matrix_a = np.array([[1, 2], [3, 4], [5, 6]])
    matrix_b = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("\nUsing len(matrix):")
    print("matrix_a has a length of", len(matrix_a))
    print("matrix_b has a length of", len(matrix_b))
    
    print("\nUsing len(matrix[int])")
    print("The 1st row of matrix_a has a length of", len(matrix_a[0]))
    print("The 1st row of matrix_b has a length of", len(matrix_b[0]))

main()