"""
See the separate handout for the equations to be used for this problem. 
"""

import numpy as np
import matplotlib.pyplot as plt

def Wilson(L_12, L_21):
    """
    The function uses the Wilson model to create a plot of activity
    coefficients over the full range of composition.

    Parameters
    ----------
    L_12 and L_21 : floats
        The model parameters.


    Returns
    -------
    None.

    """
    ###########################################################################
    # TODO 1: Perform the calculations to the following specifications:
    #           - Create a vector for x1 from 0 to 1. Use 50 data points.
    #             (optional) Create a vector for x2.
    #           - Calculate the activity coefficients the correspond to each
    #             composition and store the results in two separate vectors.
    ###########################################################################
    x1 = np.linspace(0, 1, 50)
    x2 = 1 - x1
    gamma1 = np.zeros(50)
    gamma2 = np.zeros(50)
    
    for i in range(len(x1)):

        
        gamma1[i] = np.exp(-np.log(L_12*x2[i] + x1[i]) + x2[i]*(L_12/(L_12*x2[i] + x1[i]) - L_21/(L_21*x1[i] + x2[i])))
        gamma2[i] = np.exp(-np.log(L_21*x1[i] + x2[i]) - x1[i]*(L_12/(L_12*x2[i] + x1[i]) - L_21/(L_21*x1[i] + x2[i])))
    
    ###########################################################################
    # TODO 2: Create figure and axes instances and plot the activity
    #         coefficient of both species vs. x1.
    ###########################################################################
    fig, ax = plt.subplots()
    
    ax.plot(x1, gamma1, color = 'blue', ls = '-')
    ax.plot(x1, gamma2, color = 'orange', ls = '-')
    
    ax.set_xlabel('$x^2$')
    ax.set_ylabel('$\gamma$')
    ax.set_xlim(0, 1)
    
    plt.show()

    ###########################################################################
    # TODO 3: This problem is going to illustrate how you can create special
    #         characters/formatting on your figures.
    #
    #         - When you want to use superscripts, you enclose the variable
    #           in dollar signs, and use the caret in front of the character
    #           to be superscripted. Example: "$x^2$"
    #         - If you want to superscript more than one character, enclose
    #           them inside of {}. Example: "$10^{23}$"
    #         - The only difference for subscripting is that you use a _ 
    #           instead of a caret.
    #         - When you want to use Greek letters, you place the character
    #           name inside of dollar signs, then use \before the Greek name.
    #           Example: "$\beta$"
    #
    #         Use the above descriptions to re-create the figure that is in
    #         the handout with the problem statement. Be sure to include the 
    #         following features:
    #    
    #         - The y-axis label is a Greek gamma.
    #         - The x-axis label is x1 with the 1 subscripted
    #         - There is a legend with Greek gammas and species numbers
    #           subscripted.
    ########################################################################### 


    
Wilson(1.05, 1.35)