"""
Complete the function below (prime_range) according to the specifications in 
the 'practice problems' handout.

Once you have completed the function, uncomment the line at the bottom of the 
file that calls main() to run the function test.
"""
def main():
    test_prime_range()
    
def test_prime_range():
    
    expected = 168
    actual = prime_range(1, 1000)
    print("Test 1:")
    print("----------")
    print("Expected value:", expected)
    print("Actual value:", actual )
    
    expected = 262
    actual = prime_range(1000, 3000)    
    print("\nTest 2:")
    print("----------")
    print("Expected value:", expected)
    print("Actual value:", actual )
    
    expected = 1
    actual = prime_range(8, 11)    
    print("\nTest 3:")
    print("----------")
    print("Expected value:", expected)
    print("Actual value:", actual)

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

###############################################################################
# TODO 1: Complete the function below (prime_range). Run the file to test your
#         code.
###############################################################################

def prime_range(start, stop):
    """

    Parameters
    ----------
    start : int
        The first value on the range for counting prime numbers
    stop : int
        The last number (inclusive) on the range for counting prime numbers.

    Returns
    -------
    The amount of prime numbers between start and start.

    """
    count = 0
    
    for j in range(start, stop + 1):
        bol = is_prime(j)
        if bol == True:
            count += 1
            
    return count
            
    
    



main()

        
    