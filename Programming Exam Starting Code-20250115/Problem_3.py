
def main():
    test_problem_3()


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

def test_problem_3():
    expected = 23
    actual = problem_3(4, 3)
    print("Test 1:")
    print("------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = 791
    actual = problem_3(101, 7)
    print("\nTest 2:")
    print("------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = 12458
    actual = problem_3(1000, 12)
    print("\nTest 3:")
    print("------")
    print("Expected:", expected)
    print("Actual:", actual)


def problem_3(a, n):
    """
    This function receives integer values a and n. The function will sum n
    prime numbers starting at a, where a does not have to be a prime number.
    You can use is_prime (already defined) to determine if a number is prime.
    
    Example:
        If a = 6 and n = 3, the first 3 prime numbers starting at 6 are
        7, 11, 13
        
        The sum of those values is 7 + 11 + 13 = 31
        
        The function returns 31.

    Parameters
    ----------
    a : int
        The starting value to determine the set of prime numbers to sum.
    n : int
        The quantity of prime numbers to include in the sum.

    Returns
    -------
    int
        The sum of n prime numbers that are >= a.

    """


main()