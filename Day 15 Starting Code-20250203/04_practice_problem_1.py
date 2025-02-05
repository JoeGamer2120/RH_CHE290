"""
In this practice problem, you will use solve_ivp to determine the numerical 
solution for the conversion as a function of reactor volume for a second-order
chemical reaction.

The governing differential equation is:
    dX/dV = r/Fa0

where
    X: conversion
    V: reactor volume
    r: reaction rate
    Fa0: the initial flow rate of species A

The reaction rate is related to the concentration of species A through:
    r = k*Ca^2

where
    k: reaction rate constant
    Ca: concentration of species A

Finally, the concentration is related to the conversion through:
    Ca = Ca0*(1-X)

where
    Ca0: the initial concentration of species A

(In short, the differential equation that you are going to solve is:
 
     dX/dV = k * Ca0^2 * (1-X)^2 / Fa0
)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def main():
    second_order_reaction()

def f(V, X, k, Ca0, Fa0):
    """
    Complete this function to be used by solve_ivp to determine the numeric
    solution to this problem.

    Parameters
    ----------
    V : float
        reactor volume.
    X : float
        reaction conversion.
    k : float
        reaction rate constant.
    Ca0 : float
        initial concentration of species A.
    Fa0 : float
        initial flow rate of species A.

    Returns
    -------
    float
        the value of the differential equation at the current value of V.

    """
    ###########################################################################
    # TODO 1: Complete this function according the problem statement. 
    ###########################################################################
    return k * Ca0**2 * (1-X)**2 / Fa0


def make_plot(V, X, k, Ca0, Fa0):
    """
    This function will be used to make a plot that compares the numerical
    result from solve_ivp to the analytical solution.
    
    Parameters
    ----------
    V : array
        the list of volumes inside the reactor.
    X : array
        the values of the conversion that correspond to the reactor volume.

    Returns
    -------
    None.

    """
    
    ###########################################################################
    # TODO 3: Complete this function to create a plot that compares the 
    #         results from solve_ivp (using a scatter) and the analytical
    #         solution (use a line).
    #
    #         The analytical solution to this problem is:
    #           X = k*Ca0^2*V/(Fa0 + k*Ca0^2*V)
    #
    #         The plot should have the following characteristics:
    #           - tick marks to the inside
    #           - x-axis labeled with "volume" with units of dm^3
    #           - y-axis labeled with "conversion"
    #           - a legend
    #           - x-axis limits from 0 to 1.5
    ###########################################################################
    X_act = k * Ca0**2 * V / (Fa0 + k * Ca0**2 * V)
    
    fig, ax = plt.subplots()
    ax.scatter(V, X, label = "IVP Solution")
    ax.plot(V, X_act, label = "Actual Solution")
    ax.set_xlabel("volume $dm^3$")
    ax.set_ylabel('conversion')
    ax.legend()
    ax.set_xlim(0, 1.5)
    
    plt.show()
    

    
def second_order_reaction():
    """
    This function will be used to create the numerical solution to the problem.

    Returns
    -------
    None.

    """
    
    ###########################################################################
    # TODO 2: Complete this function to determine the numeric solution to the
    #         problem according to the following specifications:
    #           - The initial condition is X(V = 0) = 0
    #           - The final reactor volume is 1.5
    #           - A total of 30 points should be used for the volume
    #           - k = 1.1
    #           - Ca0 = 1
    #           - Fa0 = 0.9
    ###########################################################################
    
    V_range = np.linspace(0, 1.5, 30)
    
    sol = solve_ivp(f, [0, 1.5], [0], t_eval = V_range, args = (1.1, 1, 0.9))
    
    V = sol.t
    X = sol.y
    
    make_plot(V, X, 1.1, 1, 0.9)
main()