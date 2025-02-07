"""
Complete this problem according to the specifications outlined in the problem
statement.

YOUR NAME: Josiah Schlabach
"""
import numpy as np
from scipy.integrate import quad

def main():
    test_work()

def test_work():
    T = 325
    a = 3.78e-6
    b = 2.67e-5
    V_i = 0.025
    V_f = 0.0025
    expected = 6113    
    actual = work(V_i, V_f, T, a, b)
    print("Test 1:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    T = 273
    a = 2.13e-6
    b = 2.68e-5
    V_i = 3.5
    V_f = 0.1
    expected = 8068    
    actual = work(V_i, V_f, T, a, b)
    print("\nTest 2:")
    print("-------")
    print("Expected:", expected)
    print("Actual:", actual)

###############################################################################
# TODO 1: Define the function below to return the functional value for the
#         pressure using the Peng-Robinson equation of state. You may code
#         the value of R directly into the function.
###############################################################################

def Peng_Robinson(V, T, a, b):
    R = 8.314 * 10**-5      # bar m^3 / mol

    return (R * T) / (V - b) - (a) / (V * (V + b) + b * (V - b))

###############################################################################
# TODO 2: Complete the function below to determine the amount of work
#         associated with the compression of a real gas using numerical
#         integration on the governing equation. The function must return an
#         integer value.
###############################################################################

def work(V_init, V_final, T, a, b):
    I, err = quad(Peng_Robinson, V_init, V_final, args=(T, a, b))
    
    return -int(I * 10**5)  # J / mol

main()