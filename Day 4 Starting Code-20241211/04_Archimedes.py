"""
Complete the function below (Achimedes) according to the specifications in 
the 'practice problems' handout.

Once you have completed the function, uncomment the line at the bottom of the 
file that calls main() to run the function test to compare the calculated value 
of pi to the accepted value of pi.
"""

import numpy as np

def main():
    test_Archimedes()

def test_Archimedes():
    pi = Archimedes(10)
    print("Estimate of pi:", pi)
    print("Actual value of pi:", np.pi)
    
    
def Archimedes(n):
    """
    This function will use the algorithm developed by Archimedes to estimate
    the value of pi.

    Parameters
    ----------
    n : int
        The number of iterations for the calculation.

    Returns
    -------
    float
        An estimate for pi using the algorithm.

    """    
    A = 1
    N = 6
    
    for i in range(n):
        N *= 2
        A = np.sqrt(2 - np.sqrt(4 - A**2))
        
        L = N * A / 2
        U = L / (np.sqrt(1 - A**2 / 2))
        
        pi = (U + L) / 2
    return pi

    
main()