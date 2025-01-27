"""
Complete the function "Euler" below according to Problem Statement 3 on the
printout.
"""

import numpy as np

def main():
    test_Euler()
    
def test_Euler():
    tf = 2
    h = 0.5
    y0 = 1
    t = np.arange(0, tf+h, h)     
    expected = np.array([1, 1, 1.20609, 2.565231, 7.60713])
    actual = Euler(t, y0, h)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    tf = 1
    h = 0.2
    y0 = 0
    t = np.arange(0, tf+h, h)     
    expected = np.array([0, 0, 0.009771, 0.057509, 0.18870, 0.4735714])
    actual = Euler(t, y0, h)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)


def f(t):
    """
    This is the differential equation to be integrated. DO NOT ALTER this
    function

    Parameters
    ----------
    t : float
        The time.

    Returns
    -------
    float
        The functional value at t.

    """
    return t**2*np.exp(t)

def Euler(t, y0, h):
    """
    

    Parameters
    ----------
    t : ndarray
        An array of times.
    y0 : float
        The initial condition.
    h : float
        The time step.

    Returns
    -------
    ndarray
        An array of the functional values at each time.

    """
    z = np.zeros(len(t))
    lt = len(t)
    
    for i in range(lt):
        if i == 0:
            z[i] += y0
        else:
            func = f(t[i])
        
            y = y0 + func * h
        
            z[i] += y
            y0 = y
        
    return z
        
    
  
        
main()