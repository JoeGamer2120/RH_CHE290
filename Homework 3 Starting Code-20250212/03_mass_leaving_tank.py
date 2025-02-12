"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME: Josiah Schlabach
"""

import numpy as np
import pandas as pd
from scipy import integrate as ig



def main():
    names, data = get_data()
    test_trap(data)
    test_simp(data)


def test_trap(data):
   
    expected = 9521.0
    actual = integrate_trap(data)
    print("Testing integrate_trap:")
    print("-----------------------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def test_simp(data):
   
    expected = 9628.9583
    actual = integrate_simp(data)
    print("\nTesting integrate_simp:")
    print("-----------------------")
    print("Expected:", expected)
    print("Actual:", actual)
    

    
###############################################################################
# TODO 1: Complete get_data to retrieve the data from the provided Excel
#         workbook. The function should return the names of the variables in
#         an ndarray, and the numerical information in another ndarray.
###############################################################################

def get_data(): 
    """
    This function retrieves the information in the Excel sheet, converts that
    information into ndarrays of the labels and the numerical data, and 
    returns those variables.

    Returns
    -------
    ndarray
        The data labels.
    ndarray
        The numerical information from the Excel sheet.

    """
    df = pd.read_excel("Mass Leaving Reactor.xlsx")
    names = df.columns.to_numpy()
    data = df.to_numpy()


    return names, data
###############################################################################

###############################################################################
# TODO 2: Complete integrate_trap to perform the numerical integration of the
#         data using the trapezoidal rule.
#
#         After completing the function, run test_trap to test your code. 
###############################################################################

def integrate_trap(data):
    """
    This function integrates the numerical data using the trapezoidal rule.

    Parameters
    ----------
    data : ndarray
        The numerical information used to perform the numerical integration.

    Returns
    -------
    float
        The result of the numerical integration.

    """
    
    return 

###############################################################################
# TODO 3: Complete integrate_simp to perform the numerical integration of the
#         data using Simpson's rule.
#
#         After completing the function, run test_simp to test your code. 
###############################################################################

def integrate_simp(data):
    """
    This function integrates the numerical data using Simpson's rule.

    Parameters
    ----------
    data : ndarray
        The numerical information used to perform the numerical integration.

    Returns
    -------
    float
        The result of the numerical integration.

    """
    
    return 
    
    

main()

# t = data[:, 0]
# Q = data[:, 1]
# c = data[:, 2]
