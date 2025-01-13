"""
This file contains practice problems working with vectors.
"""

import numpy as np

np.random.seed(241)


def main():
    """
    Uncomment the function calls below to test your functions.
    """
    # test_vector_sum()
    # test_vector_mean()
    # test_vector_min()
    # test_count_less_than_x()
    # test_index_less_than_x()


def test_vector_sum():
    v = np.random.randint(0, 10, 50)
    expected = sum(v)
    actual = vector_sum(v)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(25, 100, 17)
    expected = sum(v)
    actual = vector_sum(v)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(1, 20, 150)
    expected = sum(v)
    actual = vector_sum(v)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)    

def test_vector_min():
    v = np.random.randint(0, 100, 10)
    expected = np.min(v)
    actual = vector_min(v)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(-1000, 1000, 100)
    expected = np.min(v)
    actual = vector_min(v)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(0, 10**6, 2000)
    expected = np.min(v)
    actual = vector_min(v)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)

def test_vector_mean():
    v = np.random.randint(0, 100, 10)
    expected = np.mean(v)
    actual = vector_mean(v)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(-1000, 1000, 100)
    expected = np.mean(v)
    actual = vector_mean(v)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(0, 10**6, 2000)
    expected = np.mean(v)
    actual = vector_mean(v)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)


def test_count_less_than_x():
    v = np.random.randint(0, 10, 50)
    expected = 17
    actual = count_less_than_x(v, 3)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(25, 100, 17)
    expected = 3
    actual = count_less_than_x(v, 50)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    v = np.random.randint(1, 20, 15)
    expected = 11
    actual = count_less_than_x(v, 15)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)

def test_index_less_than_x():
    v = np.random.randint(0, 10, 50)
    expected = np.array([1, 2, 9, 13, 14, 16, 21, 22, 26, 30, 31, 35, 36, 
                         38, 39, 43, 47], dtype=float)
    actual = index_less_than_x(v, 3)
    print("Test 1:")
    print("--------")
    print("Expected:\n", expected)
    print("Actual:\n", actual)
    
    v = np.random.randint(25, 100, 17)
    expected = np.array([10, 14, 16], dtype=float)
    actual = index_less_than_x(v, 50)
    print("\nTest 2:")
    print("--------")
    print("Expected:\n", expected)
    print("Actual:\n", actual)
    
    v = np.random.randint(1, 20, 15)
    expected = np.array([0, 1, 5, 6, 8, 9, 10, 11, 12, 13, 14], dtype=float)
    actual = index_less_than_x(v, 15)
    print("\nTest 3:")
    print("--------")
    print("Expected:\n", expected)
    print("Actual:\n", actual)     


def vector_sum(v):
    """
    TODO 1: This function receives a vector, v, and returns the sum of the 
            values contained in the vector. You must write your own code
            to calculate the sum (i.e., you should not use a built-in
            function).

    Parameters
    ----------
    v : ndarray
        A vector of integer values.

    Returns
    -------
    int
        The sum of the elements of v.

    """
    sum = 0
    
    for i in range(len(v)):
        sum += v[i]
    
    return sum
 
def vector_mean(v):
    """
    TODO 2: This function receives a vector, v, and returns the mean of the
            value contained in the vector. You must write your own code
            to calculate the mean (i.e., you should not use a built-in
            function).
            
            You may use the vector_sum function from TODO 1, if you choose.

    Parameters
    ----------
    v : ndarray
        A vector of integer values.

    Returns
    -------
    float
        The mean of the elements of v.

    """
    mean = vector_sum(v) / len(v)
    
    return mean
    
def vector_min(v):
    """
    TODO 3: This function receives a vector, v, and determines the minimum
            value contained within the vector. You must write your own code
            to find the minimum (i.e., you should not use a built-in
            function).

    Parameters
    ----------
    v : ndarray
        A vector of integer values.

    Returns
    -------
    int
        The minimum value contained within v.

    """
    min = v[0]
    
    for i in range(len(v)):
        if min >= v[i]:
            min = v[i]
        
    return min


def count_less_than_x(v, x):
    """
    TODO 4: This function receives a vector, v, and an integer value, x. The 
            function will determine the number of elements in v that contain
            a value that is less than or equal to x.

    Parameters
    ----------
    v : ndarray
        A vector of integer values
    x : int
        An integer value used to compare to elements of v. 

    Returns
    -------
    int
        The number of elements in v that contains values that are less than or
        equal to x.

    """
    count = 0
    
    for i in range(len(v)):
        if v[i] <= x:
            count += 1
            
    return count

def index_less_than_x(v, x):
    """
    TODO 5: This function receives a vector, v, and an integer value, x. The
            function will return a vector that contains the indicies of v that
            have values that are less than or equal to x.
            
            You may use count_less_than_x from TODO 4, if you choose.
            
            Example:
                v = [4 2 6 1 8 4 3]
                x = 3
                
                The indices of the elements of v that are <= 3 are 1, 3, 6, 
                therefore, the vector [1, 3, 6] is returned from the function.

    Parameters
    ----------
    v : ndarray
        A vector of integer values
    x : int
        An integer value used to compare to elements of v. 

    Returns
    -------
    ndarray
        A vector of indices where elements of v are <= x.

    """
    array = np.zeros(count_less_than_x(v, x))
    
    j = 0
    for i in range(len(v)):
        if v[i] <= x:
            array[j] = i
            j += 1
            
    return array

main()