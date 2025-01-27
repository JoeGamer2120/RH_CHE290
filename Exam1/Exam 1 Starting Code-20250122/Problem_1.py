"""
Complete the function "problem_1" below according to Problem Statement 1 on the
printout.
"""

import numpy as np

np.random.seed(100)


def main():
    test_problem_1()

def test_problem_1():
    m = np.random.randint(2, 1001, 101)
    expected = 411.0
    actual = problem_1(m)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)

    m = np.random.randint(1, 99, 1000)
    expected = 52.82196
    actual = problem_1(m)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)

    m = np.random.randint(101, 5000, 250)
    expected = 2619.3829787
    actual = problem_1(m)
    print("\nTest 3:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def problem_1(m):
    """
    

    Parameters
    ----------
    m : ndarray
        An array of integers.

    Returns
    -------
    float
        The average of the values in the array that are not multiples of 2 
        or 3.

    """
    tot = 0
    count = 0
    
    for i in range(len(m)):
        ele = m[i]                          # Used for Debugging
        if ele % 2 != 0 or ele % 3 != 0:
            tot += m[i]
            count += 1
            
    mean = tot / count
    
    return mean
    
    

main()