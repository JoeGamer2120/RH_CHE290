"""
This file provides an example of how you can construct unit tests to
ensure that your code (typically functions) is working correctly.
"""

###############################################################################
# Unit testing is one way to systematically test sections of code and
# functions. To perform a unit test, you determine the expected answers for the 
# code (or function) for a variety of test cases. Whenever possible, try to 
# include edge cases. 
#
# Assume that our program has a need to determine the magnitude of a variety
# of vectors. Instead of continually having to type out the formula (and
# risking typos), we create a function (vector_magnitude) to perform the 
# calculation. Before implementing the function in the program, best practice
# is to test the function to ensure it works correctly.
# 
# The code below is a basic example of function implementation with unit
# tests. Notice that the unit test is its own function. Coding the unit test
# into an independent function makes it easy to activate/deactivate the test.
# 
# One way to perform a unit test (as illustrated below) is to create a variable
# that contains the expected value from the function. Another variable stores
# the actual value that gets returned from the function. Then, a series of
# print statements are used that enables comparison between expectation and
# actuality. If those two match for all test cases, the function passes the 
# test. If any test case fails, the whole function fails and must be fixed.
###############################################################################
def main():
    test_vector_magnitude()

def test_vector_magnitude():
    
    expected = 3**0.5
    actual = vector_magnitude(1, 1, 1)
    print("Test 1:")
    print("Expected: ", expected)
    print("Actual: ", actual)
    print()
    
    expected = 0.0
    actual = vector_magnitude(0, 0, 0)
    print("Test 2:")
    print("Expected: ", expected)
    print("Actual: ", actual)
    print()
    
    expected = 6.0
    actual = vector_magnitude(2**0.5, 3, 5)
    print("Test 3:")
    print("Expected: ", expected)
    print("Actual: ", actual)
    
    
def vector_magnitude(x, y, z):
    return (x**2 + y**2 + z**2)**0.5


main()