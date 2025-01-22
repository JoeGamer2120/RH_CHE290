import numpy as np

np.random.seed(12)

def main():
    test_problem_4()

def test_problem_4():
    m = np.random.randint(0, 100, 24).reshape(4, 6)
    expected = np.array([180., 252., 285., 357.])
    actual = problem_4(m)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)

    m = np.random.randint(0, 100, 21).reshape(7, 3)
    expected = np.array([98., 177., 216., 163., 107., 175., 226])
    actual = problem_4(m)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    m = np.random.randint(-100, 100, 22).reshape(2, 11)
    expected = np.array([-128., 328.])
    actual = problem_4(m)
    print("\nTest 3:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def problem_4(m):
    """
    This function receives a matrix, m, and returns a vector where each value
    is the sum of the row in the matrix.
    
    Example:
        
        if m = [[1, 2, 3, 4], [5, 6, 7, 8]]
        
        row 1 = 1 + 2 + 3 + 4 = 10
        row 2 = 5 + 6 + 7 + 8 = 26
        
        The vector returned from the function would be [10, 26]

    Parameters
    ----------
    m : ndarray
        an i by j matrix.

    Returns
    -------
    ndarray
        a vector of i elements that is the sum of the rows of m.

    """


main()   