"""
See the separate handout for the equations to be used for this problem. 
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    [x1, g1, g2] = Wilson(1.05, 1.35)
    data = get_data()
    make_plot(x1, g1, g2, data)

def Wilson(L_12, L_21):
    """
    The function uses the Wilson model to create vectors of the activity
    coefficients over the full range of composition.

    Parameters
    ----------
    L_12 and L_21 : floats
        The model parameters.


    Returns
    -------
    x1 : ndarray
        The vector of mole fractions for component 1
    g1 and g1 : ndarrays
        The vectors of the activity coefficients for both components

    """
    ###########################################################################
    # TODO 1: Perform the calculations for the activity coefficients using
    #         the Wilson model.
    #
    #         You may copy your code from the similar practice problem on
    #         day 13.
    ###########################################################################
    x1 = np.linspace(0, 1, 50)
    x2 = 1 - x1
    g1 = np.zeros(50)
    g2 = np.zeros(50)
    
    for i in range(len(x1)):
        g1[i] = np.exp(-np.log(L_12*x2[i] + x1[i]) + x2[i]*(L_12/(L_12*x2[i] + x1[i]) - L_21/(L_21*x1[i] + x2[i])))
        g2[i] = np.exp(-np.log(L_21*x1[i] + x2[i]) - x1[i]*(L_12/(L_12*x2[i] + x1[i]) - L_21/(L_21*x1[i] + x2[i])))
    

    return x1, g1, g2



def get_data():
    """
    This function will read the Excel file and assign the information to
    relevant variable names before return the information.

    Returns
    -------
    data : ndarray
        The activity coefficient data.

    """
    
    ###########################################################################
    # TODO 2: Complete this function to read the data from the Excel file,
    #         convert the data into an ndarray, and return the array.
    ###########################################################################
    
    df = pd.read_excel('Data File.xlsx', 'Activity Coefficients')
    data = df.to_numpy()
    
    return data


def make_plot(x1, g1, g2, data):
    """
    This function creates a plot that compares the activity coefficient data
    to the model.

    Parameters
    ----------
    x1 : ndarray
        The vector of mole fractions for component 1
    g1 and g1 : ndarrays
        The vectors of the activity coefficients for both components
    data : ndarray
        The activity coefficient data.

    Returns
    -------
    None.

    """

    ###########################################################################
    # TODO 3: Create a plot with the following features:
    #           - The activity coefficient DATA will be plotted as circles
    #             (no lines).
    #           - The activity coefficient MODEL will be plotted as solid
    #             lines (no markers)
    #           - Component one information will be red; component two
    #             information will be green.
    #           - The y-axis label is a Greek gamma.
    #           - The x-axis label is x1 with the 1 subscripted
    #           - The tick marks on all axes are in.
    #
    #         You can compare your figure to the included "figure_2.png".
    ###########################################################################
    fig, ax = plt.subplots()
    #
    ### Wilson Model
    #
    ax.plot(x1, g1, color = 'red')
    ax.plot(x1, g2, color = 'green')
    
    #
    ### Activity Coefficient Model
    #
    x_data = data[:, 0]
    gamma1 = data[:, 1]
    gamma2 = data[:, 2]
    
    ax.scatter(x_data, gamma1, color = 'red', marker = 'o')
    ax.scatter(x_data, gamma2, color = 'green', marker = 'o')
    
    ax.set_xlim(0, 1)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$gamma$')
    ax.tick_params(direction = 'in')
    
    plt.show()
    
main()