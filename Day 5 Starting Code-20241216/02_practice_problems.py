"""
Complete the two practice problems below that utilize while loops. Refer to the
handout for the relevant equations and descriptions.
"""
import math

def main():
    """
    Uncomment the following calls to test functions as you complete tasks

    Returns
    -------
    None.

    """
    test_my_exp_1()
    test_my_exp_2()
    test_my_sqrt()

def test_my_exp_1():
    expected = 7
    actual = my_exp(2, 1)
    print("Test 1:")
    print("-------")
    print("Expected value: ", expected)
    print("Actual value:", actual)

    expected = 1/3
    actual = my_exp(-2, 1)
    print("\nTest 2:")
    print("-------")
    print("Expected value: ", expected)
    print("Actual value:", actual)

def test_my_exp_2():
    expected = math.exp(2)
    actual = my_exp(2, 10**-8)
    print("Test 1:")
    print("-------")
    print("Expected value: {:0.5f}".format(expected))
    print("Actual value: {:0.5f}".format(actual))

    expected = math.exp(-2)
    actual = my_exp(-2, 10**-8)
    print("\nTest 2:")
    print("-------")
    print("Expected value: {:0.5f}".format(expected))
    print("Actual value: {:0.5f}".format(actual))
    
def test_my_sqrt():
    expected = math.sqrt(4)
    actual = my_sqrt(4)
    print("Test 1:")
    print("-------")
    print("Expected value: ", expected)
    print("Actual value:", actual)

    expected = math.sqrt(12)
    actual = my_sqrt(12)
    print("\nTest 2:")
    print("-------")
    print("Expected value: {:0.5f}".format(expected))
    print("Actual value: {:0.5f}".format(actual))
    
    expected = math.sqrt(0.5)
    actual = my_sqrt(0.5)
    print("\nTest 3:")
    print("-------")
    print("Expected value: {:0.5f}".format(expected))
    print("Actual value: {:0.5f}".format(actual))   
    
###############################################################################
# TODO 1: Complete the function (my_exp) below according to the specifications
#         in the practice problem handout.
#
#         Once you have completed the function, uncomment the function call to
#         test_my_exp_1 above. That test case uses for x = 2 and tol 1. The 
#         function should perform the calculation as follows (where 'term' is 
#         x^n/n!):
#
#           n       term
#           0        1      (1 is not < 1)
#           1        2      (2 is not < 1)
#           2        2      (2 is not < 1)
#           3        4/3    (4/3 is not < 1)
#           4        2/3    (2/3 is < 1)
#         -----------------
#                    7  (the total of adding all of the terms)
#
#         The factorial of x is built into the math module as: 
#               math.factorial(x)
#
#         Once your function passes test_my_exp_1 (tests will a large 
#         tolerance), uncomment the call to test_my_exp_2 to test your function
#         to compare to realistic values of exp(x).
###############################################################################


def my_exp(x, tol):
    """
    This function uses the equation provided in the practice problems handout
    to determine the value of exp(x) to a specified accuracy (tol).

    Parameters
    ----------
    x : float
        The argument of exp(x).
    tol : float
        The accuracy/tolerance to which exp(x) will be calculated.

    Returns
    -------
    float
        The result of exp(x).

    """
    n = 0
    term = 1
    exp = 0
    
    while abs(term) >= tol:
        term = (x**n) / math.factorial(n)
        exp += term
        n += 1
        
    return exp

    
###############################################################################
# TODO 2: Complete the function (my_sqrt) below according to the specifications
#         in the practice problems handout.
#
#         Once you have completed the function, uncomment the function call to
#         test_my_sqrt above to test your function.
###############################################################################         

def my_sqrt(A):
    """
    This function uses Halley's method to approximate the A^(1/2) according to
    algorithm outlined in the practice problems handout.

    Parameters
    ----------
    A : float
        The argument of A^(1/2).

    Returns
    -------
    float
        The approximation of the result for A^(1/2).

    """
    e = 10**-8 # Tolerance
    
# Check A to determine inital condition
    if A >= 1:
        x = 1
    else:
        x = A / 2 
# Iterate using the forumulas described in the worksheet until Tolerance 
    while True:
        y = (1/A) * x**2
        xn = (x/8) * (15 - y*(10-3*y))
        
    # Tolerance Check
        if (abs(xn - x)) <= e:
            break
       
        x = xn
        
    return xn
            
    
   
        


main()