"""
Complete the function "my_pi" below according to Problem Statement 2 on the
printout.
"""
import numpy as np

def main():
    test_my_pi()

def test_my_pi():
    expected = np.pi
    actual = my_pi()
    print("Test:")
    print("------")
    print("Expected: {:0.6f}".format(expected))
    print("Actual: {:0.6f}".format(actual))

def my_pi():
    """
    
    Returns
    -------
    float
        An estimate of pi.

    """
    pi = 0
    x = -1
    
    while True:
        x += 2
        term1 = 4 / x
        x += 2
        term2 = 4 / x
        
        if term1 < 10**-6:      # Determine if term1 meets tolerance otherwise add
            break
        else:
            pi += term1
        
        if term2 < 10**-6:      # Determine if term2 meets tolerance otherwise subtract
            break
        else:
            pi -= term2
        
    return pi
        
        

    

main()