"""
This file is intended to provide more practice with while loops.
"""

import math

def main():
    """
    Uncomment the test calls below as needed.
    """

    test_sum_primes()
    test_my_invest()
    test_e_inverse()

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

def test_sum_primes():
    expected = 17
    actual = sum_primes(2, 4)
    print("Test 1:")
    print("------------")
    print("Expected years:", expected)
    print("Actual years:", actual)
    
    expected = 173
    actual = sum_primes(50, 3)
    print("\nTest 2:")
    print("------------")
    print("Expected years:", expected)
    print("Actual years:", actual)
    
    expected = 6126
    actual = sum_primes(1000, 6)
    print("\nTest 3:")
    print("------------")
    print("Expected years:", expected)
    print("Actual years:", actual)

def test_my_invest():
    expected = 8
    actual = my_invest(10000, 1000, 0.05)
    print("Test 1:")
    print("------------")
    print("Expected years:", expected)
    print("Actual years:", actual)

    expected = 44
    actual = my_invest(20000, 100, 0.06)
    print("\nTest 2:")
    print("------------")
    print("Expected years:", expected)
    print("Actual years:", actual)    
    
    expected = 28
    actual = my_invest(1000000, 5000, 0.12)
    print("\nTest 3:")
    print("------------")
    print("Expected years:", expected)
    print("Actual years:", actual)

def test_e_inverse():
    expected_n = 1840
    expected_val = 0.367779
    actual_val, actual_n = e_inverse()
    print("Test:")
    print("--------")
    print("Expected n:", expected_n)
    print("Actual n:", actual_n)
    print("\nExpected value (about):", expected_val)
    print("Actual value:", actual_val)
    


###############################################################################
# TODO 1: Complete the function (sum_primes) below according to the 
#         specifications in the doc-string. Test your function by
#         uncommenting test_sum_primes() in main().
###############################################################################
def sum_primes(m, n):
    """
    This function will sum together n prime numbers starting with m, where m
    does not have to be a prime number. You can use the function is_prime(n) 
    to test for primality.
    
    Example 1:
        m = 4, n = 3
        
        The first prime number after 4 is 5. The next two prime numbers are 
        7 and 11.
        
        5 + 7 + 11 = 23 (return value)
    
    Example 2:
        m = 59, n = 2
        
        59 is a prime number. The next prime number is 61. 
        
        59 + 61 = 120 (return value)

    Parameters
    ----------
    m : int
        The starting point to determine the first prime number to sum. m does
        not have to be prime.
    n : int
        The amount of prime numbers to add together.

    Returns
    -------
    int
        The sum of n prime numbers starting at m.

    """
    count = 0
    i = 0
    total = 0
    
    while count < n:
        if is_prime(m + i) == True:
            total += (m + i)
            count += 1
        
        i += 1
        
    return total
    
    
    

###############################################################################
# TODO 2: Complete the function (my_invest) below according to the 
#         specifications in the doc-string. Test your function by
#         uncommenting test_my_invest() in main().
###############################################################################

    
def my_invest(goal, deposit, rate):
    """
    This function will determine the number of years necessary to achieve
    your financial goal if you make yearly deposits. The interest is compounded
    annually, and your deposit will be at the beginning of the year.
    
    Example:
        if deposit = $100 and the interest is 2%:
        - The initial deposit at the beginning of year 1 is $100
        - At the end of the year, $2 (2% of $100) is added to the account.
        - At the beginning of year 2, $100 is deposited bringing the account
          balance to $202.
          etc.

    Parameters
    ----------
    goal : float
        Your financial goal in dollars.
    deposit : float
        The amount of money deposited into your account at the beginning of
        each year.
    rate : float
        The interest rate earned on the account in fractional form.

    Returns
    -------
    year : int
        The number of years necessary to achieve your financial goal.

    """
    balance = 0
    year = 0
    
    while balance < goal:
        balance += deposit
        balance *= (1+rate)
        year += 1
        
    return year
        
###############################################################################
# TODO 3: Complete the function (e_inverse) below according to the 
#         specifications in the doc-string. Test your function by
#         uncommenting test_e_inverse() in main().
###############################################################################

def e_inverse():
    """
    The inverse of the mathematical constant e can be approximated as:
        
        1/e ~ (1 - 1/n)^n
    
    This function will loop through values of n until the difference between
    the approximation (using the formula above) and the actual value (from the 
    math library) is less than 0.0001. The function will return (in order) 
    the value of the approximation and the value of n.

    Returns
    -------
    float
        The approximation of 1/e.
    int
        The value of n used to create the approximation within the specified
        tolerance.

    """
    tol = 0.0001
    e = 5 # This is the inverse of e
    n = 1
    
    while tol < (abs(e - 1/math.exp(1))):
        e = (1 - 1/n)**n
        n += 1
        
    return (e, n)
        
    
main()


 

    