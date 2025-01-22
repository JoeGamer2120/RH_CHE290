import numpy as np

np.random.seed(12)

def main():
    test_problem_7()

def is_prime(n):
    """
    DO NOT TOUCH THIS FUNCTION. YOU SHOULD USE THIS FUNCTION TO COMPLETE
    THE PROBLEM.
    
    Parameters
    ----------
    n : int
        An integer >= 2.


    Returns
    -------
    True if the given integer is prime, else returns False.

    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """

    if n <= 1:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False
    return True


def test_problem_7():
    m = np.random.randint(2, 1001, 24).reshape(4, 6)
    expected = 1, 461
    actual = problem_7(m)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)

    m = np.random.randint(2, 101, 21).reshape(7, 3)
    expected = 4, 47
    actual = problem_7(m)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(101, 1001, 22).reshape(2, 11)
    expected = 3, 937
    actual = problem_7(m)
    print("\nTest 3:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def problem_7(m):
    """
    This function receives a matrix, m, of positive integers. The matrix can be
    composed of any number of rows and columns. The function will do the 
    following:
        - it determines how many elements are prime numbers
        - it determines the largest prime number 
    
    The function returns those values in that order.
    
    You may assume that each matrix has at least one prime number.
    
    Example:
        
        if m = [[1, 2, 3, 4], [5, 6, 7, 8]]
        
        2, 3, 5, and 7 are prime numbers, for a total of 4 primes.
        The largest prime number is 7.
        
        The function returns 4, 7 (you do not have to return a vector)

    Parameters
    ----------
    m : ndarray
        an i by j matrix.

    Returns
    -------
    int
        The total number of primes contained in the matrix.
    
    int
        The largest prime number in the matrix

    """
    

main() 
  