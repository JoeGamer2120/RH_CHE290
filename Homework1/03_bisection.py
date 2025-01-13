"""
Complete this program according the specifications in the problem statement.

YOUR NAME: Josiah Schlabach
"""


def main():
    test_bisection()


def test_bisection():

    expected = -0.07539
    actual = bisection(-0.2, 0)
    print("Test 1:")
    print("----------")
    print("Expected value (about):", expected)
    print("Actual value:", actual)

    expected = 0.14084
    actual = bisection(0, 0.5)
    print("\nTest 2:")
    print("----------")
    print("Expected value (about):", expected)
    print("Actual value:", actual)

    expected = 0.93509
    actual = bisection(0.5, 1)
    print("\nTest 3:")
    print("----------")
    print("Expected value (about):", expected)
    print("Actual value:", actual)


def fx(x):
    """
    f(x) is a mathematical function with a single argument, x. This function
    will return the numeric value of the mathematical function at x.

    """
    return x**3 - x**2 + 0.05 * x + 0.01


###############################################################################
# TODO 1: Complete the function below (bisection) according to the
#         specifications in the problem statement.
#
#         The mathematical function for which the root is to be determined is
#         contained in f(x). If needed for debugging, you can change that
#         function as needed. However, be sure to keep the original function
#         for the final test (by commenting out what's provided).
#
#         Once you have completed the function, uncomment the line at the
#         bottom of the file that will run the function test.
###############################################################################


def bisection(a, b):
    """

    Parameters
    ----------
    a : float
        One value of f(x)
    b : float
        A second value of f(x)
    The range created by a and b contains a root for f(x).

    Returns
    -------
    The root of f(x).

    """

    while True:
        c = (a + b) / 2
        if (fx(a) * fx(c)) < 0:
            b = c

        elif (fx(a) * fx(c)) > 0:
            a = c

        else:
            break

        if abs(fx(c)) <= 10**-8:
            break

    return c


main()

