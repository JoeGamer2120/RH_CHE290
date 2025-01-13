"""
This file will illustrate how to index locations in vectors and matrices.
"""
import numpy as np
 
def main():
    """
    Uncomment the lines below when instructed by a TODO.
    """
    # indexing_vectors()
    indexing_matrices()
    # slicing_vectors()
    # slicing_matrices()


###############################################################################
# INDEXING ELEMENTS OF AN ARRAY
#
# The index of an array specifies the location of an element within the array.
# The first element of an array is 0 and each subsequent element is identified
# by the next integer value. To retrieve the last element of a vector you can 
# use -1.
#
# For a vector, a single index, contained within brackets, is used to identify 
# an element since there is only 1 row of data (see indexing_vectors).
#
# For a matrix, a single index can be used to identify a row of elements. To
# identify a single element, two indices are needed. Each index is contained
# within a set of brackets separated by a comma (see_indexing matrices).
###############################################################################

def indexing_vectors():
    """
    TODO 1: Uncomment the call to this function in main() to see where values 
            of vec_g are located.
    """
    
    vec_g = np.array([1, 5, -2, 7, 6])
    
    for i in range(5):
        print("Element", i, "of the array contains", vec_g[i])
    
    print("\nThe last element of vec_g contains:", vec_g[-1], '\n')
    
def indexing_matrices():
    """
    TODO 2: Uncomment the call to this function in main() to see where values 
            of the defined matrices are located.
    """
    
    matrix_a = np.array([[1, 2], 
                         [3, 4], 
                         [5, 6]])
    matrix_b = np.array([[1, 2, 3],
                         [4, 5, 6]])
    
    print("Using a single index:")
    print("---------------------")
    print("Element 0 of matrix_a contains:\n", matrix_a[0], "\n")
    print("Element 0 of matrix_b contains:\n", matrix_b[0], "\n")
    print("Using two indices:")
    print("------------------")
    print("The 2nd row and 2nd column of matrix_a contains:", matrix_a[1, 1])
    print("The 2nd row and 2nd column of matrix_b contains:", matrix_b[1, 1],)
    print("The last element in matrix_a contains:", matrix_a[-1, -1], "\n")
    
    r = 3 
    c = 2 
    for i in range(r):
        for j in range(c):
            print("The", i,"row and", j,"column of matrix_a is:", 
                  matrix_a[i, j])
    print()
    
    r = 2 
    c = 3 
    for i in range(r):
        for j in range(c):
            print("The", i,"row and", j,"column of matrix_b is:", 
                  matrix_b[i, j])

###############################################################################
# SLICING ELEMENTS OF A VECTOR
#
# To retrieve a slice of a vector you can use a two index values separated by a
# colon. If the first number is left off in front of the colon, 0 is assumed. 
# If the second number is left off after the colon, -1 (the end) is assumed.
# The number after the colon is non-inclusive.If only a colon is used, the 
# whole vector is retrieved.
###############################################################################

def slicing_vectors():
    """
    TODO 3: Uncomment the call to this function in main() to see what results 
            with different slices of vec_g.
    """
    
    vec_g = np.array([1, 5, -2, 7, 6])
    
    print(vec_g[1:4])
    print()
    print(vec_g[:2])
    print()
    print(vec_g[2:])

###############################################################################
# SLICING ELEMENTS OF A MATRIX
#
# To retrieve a slice of a matrix, you can a colon as with vectors but for both
# both indices. 
###############################################################################

def slicing_matrices():
    """
    TODO 3: Uncomment the call to this function in main() to see what results 
            with different slices of a new matrix.
    """
    
    matrix_c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    
    print(matrix_c[1:3, 2])
    print()
    print(matrix_c[:, 1:])
    print()
    print(matrix_c[:2, :1])
    print()
    print(matrix_c[2:])
    
main()
