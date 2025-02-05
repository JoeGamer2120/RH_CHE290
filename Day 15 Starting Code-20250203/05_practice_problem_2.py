"""
In this practice problem, you will use solve_ivp to determine the numerical 
solution for the concentrations of 3 species as a function of time for a
chemical reaction.

The governing differential equations are:
    dCa/dt = -2kCa^0.5
    dCb/dt = 2kCa^0.5
    dCc/dt = kCa^0.5
    
where
    Ca: the concentration of species A
    Cb: the concentration of species B
    Cc: the concentration of species C
    t: the time of the reaction
    k: reaction rate constant

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def main():
    system_of_rxns()


def odes(t, C, k):
    """
    Complete this function to be used by solve_ivp to determine the numeric
    solution to this problem.    

    Parameters
    ----------
    t : float
        the reaction time.
    C : array
        the concentrations of each species.
    k : float
        the reaction rate constant.

    Returns
    -------
    list
        the values of the differential equations at the current value of t.

    """
    
    ###########################################################################
    # TODO 1: Complete this function according the problem statement. 
    # The governing differential equations are:
    #     dCa/dt = -2kCa^0.5
    #     dCb/dt = 2kCa^0.5
    #     dCc/dt = kCa^0.5
    ###########################################################################
    return -2 * k * C[0]**0.5, 2 * k * C[0]**0.5, k * C[0]**0.5
    
    



def make_plot(t, C):
    """
    This function will be used to make a plot of each concentration as a
    function of time.
    
    Parameters
    ----------
    t : array
        the list of reaction times.
    C : array
        the values of the concentratios of each species that correspond to the 
        reaction times.

    Returns
    -------
    None.

    """
    
    ###########################################################################
    # TODO 3: Complete this function to create a plot of the concentration of
    #         each species as a function of time. 
    #
    #         You can compare your result to the provided figure.
    #
    #         The plot should have the following characteristics:
    #           - tick marks to the inside
    #           - x-axis labeled with "time" with units of s
    #           - y-axis labeled with "concentration" with units of M
    #           - a legend
    #           - x-axis limits from 0 to 35
    ###########################################################################
    fig, ax = plt.subplots()
    
    Ca = C[0]
    Cb = C[1]
    Cc = C[2]
    
    ax.scatter(t, Ca, color = 'Red', label = '$C_a$')
    ax.scatter(t, Cb, color = 'Blue', label = '$C_b$')
    ax.scatter(t, Cc, color = 'Green', label = '$C_c$')
    ax.tick_params(direction = 'in')
    ax.set_xlabel('time (s)')
    ax.set_ylabel('concentration (M)')
    ax.set_xlim(0, 35)
    ax.legend()
    plt.show()


def system_of_rxns():
    """
    This function will be used to create the numeric solution to the problem.

    Returns
    -------
    None.

    """
    
    ###########################################################################
    # TODO 2: Complete this function to determine the numerical solution to the
    #         problem according to the following specifications:
    #           - The initial conditions are:
    #               Ca(t = 0) = 2
    #               Cb(t = 0) = 0
    #               Cc(t = 0) = 0
    #           - The final reaction time is 35
    #           - A total of 50 points should be used for the time
    #           - k = 0.025
    ###########################################################################
    t_start = 0
    t_end = 35
    t_span = np.linspace(t_start, t_end, 50)
    k = 0.025
    
    init_value = [2, 0, 0]
    sol = solve_ivp(odes, [t_start, t_end], init_value, t_eval = t_span, args = (k, ))
    
    t = sol.t
    C = sol.y
    
    make_plot(t, C)
    

main()