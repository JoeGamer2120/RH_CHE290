"""
Complete this problem by following the TODOs and referencing the equations
provided in the problem statement.

YOUR NAME:
"""

import numpy as np
from scipy.optimize import fsolve

T = 335
a = 0.2 
b12 = 6450
b21 = 3950

def main():
    # test_NRTL()
    # test_f()
    test_LLE()

def test_NRTL():
    T = 335
    a = 0.2 
    b12 = 6450
    b21 = 3950
    x1 = 0.25
    expected = (5.35048, 1.18551)
    actual = NRTL(x1, T, a, b12, b21)

    print("Test:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual) 

def test_f():
    T = 335
    a = 0.2 
    b12 = 6450
    b21 = 3950
    x = (0.95, 0.07) 
    expected = (0.1069160, 0.022429)
    actual = f(x, T, a, b12, b21)
    
    print("Test:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    print("\nNOTE: Only compare the absolute values, ignore sign differences.")

def test_LLE():
    T = 335
    a = 0.2 
    b12 = 6450
    b21 = 3950
    expected = [0.95267555, 0.08524405]
    actual = solve_LLE(T, a, b12, b21)

    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    T = 300
    a = 0.3 
    b12 = 4750
    b21 = 3600
    expected = [0.88629, 0.16936]
    actual = solve_LLE(T, a, b12, b21)

    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def NRTL(x1, T, a, b12, b21):
    """
    This function will calculate the activity coefficients using the provided 
    input values for each species.

    Parameters
    ----------
    x1 : float
        The mole fraction of species 1 in the mixture.
    T : float
        The temperature of the system in K.
    a : float
        The alpha parameter in the NRTL model.
    b12, b21 : floats
        The interaction parameters in the NRTL model.

    Returns
    -------
    floats
        The activity coefficients of each species.

    """
    
    ###########################################################################
    # TODO 1: Calculate and return the activity coefficients for each species
    #         using the NRTL model. Use as many steps as needed to perform the 
    #         calculations.
    #
    #         When you are done, run the test in main() to ensure your function
    #         is working correctly.
    #
    #         NOTES:
    #           - The appropriate value for R is 8.314.
    #           - The function only receives x1; you can determine x2, if
    #             needed.
    #           - Don't forget that the equations provided for the activity 
    #             cofficients are written with the natural log on the left-hand 
    #             side.
    ###########################################################################
    R = 8.314
    tao12 = b12 / (R * T)
    tao21 = b21 / (R * T)
    G12 = np.exp(-a * tao12)
    G21 = np.exp(-a * tao21)
    x2 = 1 - x1
    
    gam1 = np.exp(x2**2 * (tao21 * (G21 / (x1 + x2*G21))**2 + (tao12*G12 / (x2 + x1*G12)**2)))
    gam2 = np.exp(x1**2 * (tao12 * (G12 / (x2 + x1*G12))**2 + (tao21*G21 / (x1 + x2*G21)**2)))

    return gam1, gam2

def f(x, T, a, b12, b21):
    """
    This function returns the results of the system of equations to be solved.
    Fundamentally, the system of equations is a function of x, which contains
    the two unknowns.

    Parameters
    ----------
    x : a list of floats
        The mole fractions of species of 1 in each phase.
    T : float
        The temperature of the system in K.
    a : float
        The alpha parameter in the NRTL model.
    b12, b21 : floats
        The interaction parameters in the NRTL model.

    Returns
    -------
    floats
        The results of the governing equations to be solved.

    """
    ###########################################################################
    # TODO 2: (optional) I recommend (for accounting purposes) making 4
    #         variables for each of the mole fractions. For example:
    #           x1_1: mole fraction of species 1 in phase 1
    #           x1_2: mole fraction of species 1 in phase 2
    #           x2_1: mole fraction of species 2 in phase 1
    #           x2_2: mole fraction of species 2 in phase 2
    ###########################################################################
    x1_1 = x[0]
    x1_2 = x[1]
    x2_1 = 1 - x1_1
    x2_2 = 1 - x1_2

    
    ###########################################################################
    # TODO 3: Use the NRTL function to get activity coefficients of both 
    #         species in each phase.
    #       
    #         You should have two separate calls to the NRTL function. The
    #         first call will return the activity coefficients in phase 1, and 
    #         the second call will return the activity coefficients in phase 2.
    ###########################################################################
    gam1_1, gam2_1 = NRTL(x1_1, T, a, b12, b21)
    gam1_2, gam2_2 = NRTL(x1_2, T, a, b12, b21)


    ###########################################################################
    # TODO 4: Return the results for each equilibrium relationship separately.
    #       
    #         If you prefer, you can calculate the results of each equilibrium
    #         and then return those values.
    #
    #         When you are done, run the test in main() to ensure your function
    #         is working correctly.
    ###########################################################################
    f1 = x1_1*gam1_1 - x1_2*gam1_2
    f2 = x2_1*gam2_1 - x2_2*gam2_2
    return f1, f2

def solve_LLE(T, a, b12, b21):
    ###########################################################################
    # TODO 5: Complete this function to solve the problem using fsolve.
    #
    #         For initial guesses, use 0.99 for x1_1 and 0.01 for x1_2. 
    #         (See TODO 2 for notation.)
    #
    #         When you are done, run the test in main() to ensure your function
    #         is working correctly.
    ###########################################################################
    sol = fsolve(f, [0.99, 0.01], args = (T, a, b12, b21))
    return sol
main()

    
    