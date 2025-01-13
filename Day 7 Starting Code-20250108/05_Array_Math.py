"""
This file will illustrate different array operations.
"""

import numpy as np

def main():
    """
    Uncomment the lines below when instructed by a TODO.
    """
    
    # scalar_operations()
    # element_wise_operations()
    # matrix_multiplication()
    matrix_inversion()

###############################################################################
# SCALAR OPERATIONS
#
# Any mathematical operation (+, -, *, /, **) performed on an array (vector or
# matrix) with a scalar value (i.e., a constant) is performed on each element
# of the array. In other words, adding a constant to a vector of length 4
# results in that constant being added to all 4 values in the vector.
###############################################################################

def scalar_operations():   
    """
    TODO 1: Uncomment the call to this function in main().
    """
    
    vec_a = np.arange(1, 4)
    
    print("The original vector is:")
    print(vec_a)
    print("\nThe examples below use a constant of 5.\n")
    
    print("When you add a constant to a vector:")
    print(vec_a + 5)
    print("\nWhen you subtract a constant to a vector:")
    print(vec_a - 5)
    print("\nWhen you multiply a constant to a vector:")    
    print(vec_a * 5)
    print("\nWhen you divide a vector by a constant:")
    print(vec_a / 5)
    print("\nWhen you raise a vecto to a constant power:")
    print(vec_a ** 5)

###############################################################################
# Element-wise Operations
#
# Element-wise operations means that the mathematical operation will be
# performed only on the elements of the array in the same location. For
# example, the element in row 2 column 3 of one array will be added to the
# element in row 2 column 3 of the other array.
#
# Element-wise operations are performed using the standard symbols for 
# simple arithmetic (_, -, *, /).
#
# NOTE: Arrays must generally be the same size to perform these operations.
###############################################################################

def element_wise_operations():
    """
    TODO 2: Uncomment the call to this function in main().
    """
    vec_a = np.arange(1, 4)
    vec_b = np.arange(5, 8)
    
    print("\nVECTOR EXAMPLES")
    print("-----------------")
    print("The original vectors are:")
    print(vec_a)
    print("\n", vec_b)
    print("\nElement-wise addition gives:")
    print(vec_a + vec_b)
    print("\nElement-wise subtraction gives:")
    print(vec_a - vec_b)
    print("\nElement-wise multiplication gives:")
    print(vec_a * vec_b)
    print("\nElement-wise division gives:")
    print(vec_a / vec_b)
    
    matrix_a = np.arange(1, 10).reshape(3, 3)
    matrix_b = np.arange(11, 20).reshape(3, 3)

    print("\nMATRIX EXAMPLES")
    print("-----------------")    
    print("The original matrices are:")
    print(matrix_a)
    print("\n", matrix_b)
    print("\nElement-wise multiplication gives:")
    print(matrix_a * matrix_b)
    print("\nThe other operations are analogous.")

###############################################################################
# MATRIX MULTIPLICATION
#
# To perform standard matrix multiplication, you can use the dot method that is
# part of NumPy.
#
# The syntax for dot is: np.dot(array_a, array_b)
###############################################################################

def matrix_multiplication():
    """
    TODO 3: Uncomment the call to this function in main().
    """
    
    vec_a = np.arange(1, 4)
    vec_b = np.arange(5, 8)

    print("\nVECTOR EXAMPLES")
    print("-----------------")
    print("The original vectors are:")
    print(vec_a)
    print("\n", vec_b)
    print("\nVector multiplication gives:")
    print(np.dot(vec_a, vec_b))    
    
    matrix_a = np.arange(1, 10).reshape(3, 3)
    matrix_b = np.arange(11, 20).reshape(3, 3)
    
    print("\nMATRIX EXAMPLES")
    print("-----------------")
    print("\nThe original matrices are:")
    print(matrix_a)
    print("\n", matrix_b)
    print("\nMatrix multiplication gives:")
    print(np.dot(matrix_a, matrix_b))
    

###############################################################################
# MATRIX INVERSION
#
# To invert a matrix, use the inv function in the linalg method in NumPy.
#
# The syntax for len is: np.linalg.inv(array name)
###############################################################################
    
def matrix_inversion():
    """
    TODO 4: Uncomment the call to this function in main().
    """
    
    matrix_a = np.array([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
    
    print("\nThe original matrix is:")
    print(matrix_a)
    print("\nThe inverse of the matrix is:")
    print(np.linalg.inv(matrix_a))    
main()