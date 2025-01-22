def main():
    test_problem_6()

def test_problem_6():
    expected = 2
    actual = problem_6(0.5)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = 100
    actual = problem_6(0.99)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = 200
    actual = problem_6(0.995)
    print("\nTest 3:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)



def problem_6(p):
    """
    This function will calculate the number-average degree of polymerization,
    Xn, for a given extent of reaction, p. The governing equation is defined by
    the equation in the pdf included as part of the starting code download.
    
    The returned value must be an integer.
    
    You can truncate the series when a term is < 10^-10

    Parameters
    ----------
    p : float
        The extent of reaction for the polymerization.

    Returns
    -------
    int
        The number-average degree of polymerization

    """
    
        

main()
