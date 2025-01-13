"""
This file contains practice problems working with matrices.
"""

import numpy as np

np.random.seed(721)

def main():
    """
    Uncomment the function calls below to test your functions.
    """
    
    # test_matrix_sum()
    # test_matrix_mean()
    # test_matrix_max()
    # test_matrix_transpose()
    test_count_less_than_x()
    # test_index_less_than_x()

def test_matrix_sum():
    m = np.random.randint(0, 10, 28).reshape(7,4)
    expected = np.sum(m)
    actual = matrix_sum(m)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(25, 100, 16).reshape(4,4)
    expected = np.sum(m)
    actual = matrix_sum(m)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(1, 20, 120).reshape(10,12)
    expected = np.sum(m)
    actual = matrix_sum(m)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def test_matrix_mean():
    m = np.random.randint(0, 15, 56).reshape(8,7)
    expected = np.mean(m)
    actual = matrix_mean(m)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(-50, 125, 70).reshape(7,10)
    expected = np.mean(m)
    actual = matrix_mean(m)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(25, 60, 27).reshape(3,9)
    expected = np.mean(m)
    actual = matrix_mean(m)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)

def test_matrix_max():
    m = np.random.randint(0, 15, 56).reshape(8,7)
    expected = np.max(m)
    actual = matrix_max(m)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(-50, 125, 70).reshape(7,10)
    expected = np.max(m)
    actual = matrix_max(m)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(25, 60, 27).reshape(3,9)
    expected = np.max(m)
    actual = matrix_max(m)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)    

def test_matrix_transpose():
    m = np.random.randint(0, 100, 16).reshape(4, 4)
    expected = np.transpose(m)
    actual = matrix_transpose(m)
    print("Test 1:")
    print("--------")
    print("Expected:\n", expected)
    print("\nActual:\n", actual)

def test_count_less_than_x():
    m = np.random.randint(0, 10, 49).reshape(7,7)
    expected = 19
    actual = count_less_than_x(m, 3)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(25, 100, 16).reshape(4,4)
    expected = 9
    actual = count_less_than_x(m, 50)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(1, 20, 120).reshape(12,10)
    expected = 90
    actual = count_less_than_x(m, 15)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)

def test_index_less_than_x():
    m = np.random.randint(0, 10, 49).reshape(7,7)
    expected = np.array([[0, 1], [0, 2], [0, 3], [0, 5], 
                         [2, 0], [2, 3], [2, 4], [3, 1],
                         [3, 4], [5, 0], [5, 5], [6, 0],
                         [6, 3], [6, 6]], dtype=float)
    actual = index_less_than_x(m, 2)
    print("Test 1:")
    print("--------")
    print("Expected:        Actual:")
    for i in range(len(expected)):
        print(expected[i], "      ", actual[i])


def matrix_sum(m):
    """
    TODO 1: This function receives a matrix, m, and returns the sum of the 
            values contained in the matrix. You must write your own code
            to calculate the sum (i.e., you should not use a built-in
            function).

    Parameters
    ----------
    m : ndarray
        A matrix of integer values.

    Returns
    -------
    int
        The sum of the elements of m.

    """
    sum = 0
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            sum += m[i,j]
            
    return sum


def matrix_mean(m):
    """
    TODO 2: This function receives a matrix, m, and returns the mean of the
            value contained in the matrix. You must write your own code
            to calculate the mean (i.e., you should not use a built-in
            function).
            
            You may use the matrix_sum function from TODO 1, if you choose.

    Parameters
    ----------
    m : ndarray
        A matrix of integer values.

    Returns
    -------
    float
        The mean of the elements of m.

    """
    mean = matrix_sum(m) / (len(m) * len(m[0]))
    
    return mean
    
    
def matrix_max(m):
    """
    TODO 3: This function receives a matrix, m, and determines the maximum
            value contained within the Matrix. You must write your own code
            to cfin the maximum (i.e., you should not use a built-in
            function).

    Parameters
    ----------
    m : ndarray
        A vector of integer values.

    Returns
    -------
    int
        The maximum value contained within m.

    """
    mmax = m[0,0]
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i,j] > mmax:
                mmax = m[i,j]
                
                
    return mmax
    
def matrix_transpose(m):
    """
    TODO 4: This function will transpose matrix m. Transposing a matrix is 
            where the rows and columns are swapped. You must write your own 
            code to transpose the matrix (i.e., you should not use a built-in
            function).
    
    Example:
            1   2   3
        m = 4   5   6
            7   8   9
        
        The tranposed matrix is:
        
            1   4   7
            2   5   8
            3   6   9
        

    Parameters
    ----------
    m : ndarray
        A square matrix of integer values.

    Returns
    -------
    ndarray
        The transpose of matrix m.

    """
    # [i,j] --> [j,i]
    
    mat = np.zeros((len(m), len(m[0])))
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            mat[i,j] += m[j,i]
            
    return mat

    
def count_less_than_x(m, x):
    """
    TODO 5: This function receives a matrix, m, and an integer value, x. The 
            function will determine the number of elements in m that contain
            a value that is less than or equal to x.


    Parameters
    ----------
    m : ndarray
        A matrix of integer values
    x : int
        An integer value used to compare to elements of m. 

    Returns
    -------
    int
        The number of elements in m that contains values that are less than or
        equal to x.

    """
    count = 0
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i,j] <= x:
                count += 1
                
    return count


def index_less_than_x(m, x):
    """
    TODO 6: This function receives a matrix, m, and an integer value, x. The
            function will return an n by 2 (n = # of rows) matrix that contains 
            the indicies of m that have values that are less than or equal 
            to x.
            
            You may use count_less_than_x from TODO 5, if you choose.
            
            Example:
                m = [[4 2 6], 
                     [1 8 4], 
                     [3 7 2]]
                x = 3
                
                The indices of the elements of m that are <= 3 are [0, 1], 
                [1, 0], [2, 0], and [2, 2], therefore, the matrix:
                    
                    [[0, 1],
                     [1, 0],
                     [2, 0],
                     [2, 2]] 
                
                is returned from the function.

    Parameters
    ----------
    m : ndarray
        A matrix of integer values
    x : int
        An integer value used to compare to elements of m. 

    Returns
    -------
    ndarray
        An n by 2 matrix of indices where elements of m are <= x.

    """
    mat = np.zeros(count_less_than_x(m, x), 2)
    
    row = 0
    
    for i in range(len(m)):
        col = 0
        for j in range(len(m[0])):
            if m[i,j] <= x:
                mat[row,col] = 
            
    
    

    
    
    
main()