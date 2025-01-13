"""
Complete this program according the specifications in the problem statement.

YOUR NAME: Josiah Schlabach
"""


def main():
    """
    Uncomment the tests below as you complete each function.

    """
    test_is_prime()
    test_prime_factors()


def test_is_prime():
    expected = False
    actual = is_prime(1)
    print("Test 1:")
    print("----------")
    print("Expected:", expected)
    print("Actual:", actual)

    expected = True
    actual = is_prime(2)
    print("\nTest 2:")
    print("----------")
    print("Expected:", expected)
    print("Actual:", actual)

    expected = True
    actual = is_prime(3)
    print("\nTest 3:")
    print("----------")
    print("Expected:", expected)
    print("Actual:", actual)

    expected = False
    actual = is_prime(9)
    print("\nTest 4:")
    print("----------")
    print("Expected:", expected)
    print("Actual:", actual)

    expected = False
    actual = is_prime(49)
    print("\nTest 5:")
    print("----------")
    print("Expected:", expected)
    print("Actual:", actual)

    expected = True
    actual = is_prime(97)
    print("\nTest 6:")
    print("----------")
    print("Expected:", expected)
    print("Actual:", actual)


def test_prime_factors():
    x = 2
    print("Test 1:")
    print("----------")
    print("Expected:")
    print("2 is a prime factor of", x)
    print("\nActual:")
    prime_factors(x)

    x = 51
    print("\nTest 2:")
    print("----------")
    print("Expected:")
    print("3 is a prime factor of", x)
    print("17 is a prime factor of", x)
    print("\nActual:")
    prime_factors(x)

    x = 79
    print("\nTest 3:")
    print("----------")
    print("Expected:")
    print("79 is a prime factor of", x)
    print("\nActual:")
    prime_factors(x)


def is_prime(x):
    """
    This function will determine if x is a prime number. The function will
    return True is the number is prime and False if the number is not prime.

    Parameters
    ----------
    x : int
        The number to be evaluated for primality. You can assume that x >= 2.

    Returns
    -------
    bool
        The result of the primality test.

    """

    if x == 2 or x == 3:
        return True

    elif x == 1:
        return False

    elif x % 2 == 0:
        return False

    for N in range(3, int(x**0.5) + 1):
        if x % N == 0:
            return False

    return True


def prime_factors(x):
    """
    This function will determine all of the prime factors of x except for 1.
    You may assume x >= 2.

    Parameters
    ----------
    x : int
        The value to be factored.

    Returns
    -------
    None.

    """

    if x % 2 == 0:
        print("2 is a prime factor of " + str(x))

        while x % 2 == 0:
            x = x // 2
            if x == 1:
                return

    for i in range(3, x + 1, 2):
        if x % i == 0:
            print(str(i) + " is a prime factor of " + str(x))
        while x % 3 == 0:
            x = x // 3
            if x == 1:
                return


main()
