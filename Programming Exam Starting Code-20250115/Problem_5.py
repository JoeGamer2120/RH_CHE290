def main():
   
    test_problem_5()
     
    
def test_problem_5():
    expected = -0.1, 0.
    actual = problem_5(-0.2, 0.1)
    print("Test 1:")
    print("-------")
    print("Expected range:", expected)
    print("Actual range:", actual)
    
    expected = 0.14, 0.15
    actual = problem_5(0, 0.01)
    print("\nTest 2:")
    print("-------")
    print("Expected range:", expected)
    print("Actual range:", actual)
    
    expected = 0.75, 1.
    actual = problem_5(0.5, 0.25)
    print("\nTest 3:")
    print("-------")
    print("Expected range:", expected)
    print("Actual range:", actual)
    
    expected = 0.94, 0.93
    actual = problem_5(2, -0.01)
    print("\nTest 4:")
    print("-------")
    print("Expected range:", expected)
    print("Actual range:", actual)
    
def f(x):
    """
    f(x) is a mathematical function with a single argument, x. This function
    will return the numeric value of the mathematical function at x.

    """
    return x**3 - x**2 + 0.05*x + 0.01
    
def problem_5(x1, step):
    """
    Write the code that will determine a bound on where a sign change occurs
    in the function f(x) (defined above). The function you write will start
    its search at x1 and increment by step until a sign change occurs. The
    two values associated with the bounding region will be returned.
    
    You can assume that a sign change is guaranteed and that you will not
    encounter f(x) = 0.
    
    Example:
        Assume f(x) = -x^2 + 1      and  x1 = 0, step = 0.75
        
        The 1st range is:  
            f(0) = 1            and     f(0.75) = 0.4375    --> no sign change
            
        The 2nd range is:  
            f(0.75) = 0.4375    and     f(1.5) = -1.25      --> sign change
        
        The function returns 0.75 and 1.5 (the bounding x values)

    Parameters
    ----------
    x1 : float
        The starting value in the search algorithm.
    step : float
        The increment to use to determine the range.

    Returns
    -------
    floats
        The two values that bound the sign change.

    """
    

main()
    
    
    