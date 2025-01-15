import math

def main():
    test_problem_2()

def test_problem_2():
    expected = math.cos(0)
    actual = problem_2(0)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = math.cos(math.pi)
    actual = problem_2(math.pi)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = math.cos(1)
    actual = problem_2(1)
    print("\nTest 3:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)



def problem_2(x):
    """
    This function will calculate the value of cos(x) using the infinite series
    (see included pdf for equation).
    
    You can truncate the series when a term is > 10^-10

    Parameters
    ----------
    x : float
        The argument of cos(x).

    Returns
    -------
    float
        The value of cos(x).

    """
 

main()
