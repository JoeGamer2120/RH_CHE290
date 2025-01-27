"""
This file will demonstrate how you can create log plots.
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    Clausius_Clapeyron(40700, 373, 1)
    # internal_flow(6.5)

def Clausius_Clapeyron(dH, Tref, Pref):
    """
    You can find the equation for this problem in the separate handout.

    Parameters
    ----------
    dH : float
        The heat of vaporation of the substance in J/mol.
    Tref : float
        The reference temperature in K.
    Pref : float
        The reference pressure in bar.

    Returns
    -------
    None.

    """
    
    ###########################################################################
    # TODO 1: Perform the calculations to the following specifications:
    #           - Create a vector of temperatures from Tref to Tref + 100. Use
    #             50 data points.
    #           - Calculate a vector of pressures that correspond to the
    #             temperature vector.
    #           - Don't forget that R = 8.314 J/mol K
    ###########################################################################

    
    ###########################################################################
    # TODO 2: Create figure and axes instances and plot the pressure vs. the
    #         temperature. You do not have to do any additional formatting.
    ###########################################################################


    ###########################################################################
    # TODO 3: Because of the exponential relationship between P and T, the
    #         plot from TODO 2 should not be a straight line (there should be
    #         curvature). To create a plot with a straight line, we can instead
    #         create a semilog plot.
    #
    #         Use one of the following commands to create a semilog plot:
    #           - For a log x-axis: ax.semilogx()
    #           - For a log y-axis: ax.semilogy()
    #
    #         Create NEW figure and axes instance. Now, create a semilog plot
    #         of P vs 1/T. The resulting figure should be a straight line.
    ###########################################################################    


def internal_flow(Pr):
    """
    You can find the equation for this problem in the separate handout.

    Parameters
    ----------
    Pr : float
        The Prandtl number - a fluid property.

    Returns
    -------
    None.

    """
    ###########################################################################
    # TODO 4: Create a vector of Re from 10000 to 100000. Because these values 
    #         are different by an order of magnitude, you can the following
    #         command to create a logarithmically spaced vector:
    #    
    #           np.logspace(start, stop, num)
    #
    #         Here, the start and the stop values are integer powers of 10. For
    #         example, a start value of 0 means 10^0 = 1 or a stop value of
    #         6 means 10^6 = 1000000. 'num' is the number of values to create
    #         along the range. The default value is 50. For this problem,
    #         use the default.
    ###########################################################################    
    

    ###########################################################################
    # TODO 5: Create a vector of Nu using the values of Re that you created and
    #         and the value of Pr provided to the function. 
    ###########################################################################    

    
    ###########################################################################
    # TODO 6: Create figure and axes instances and plot Nu vs. Re. You do not 
    #         have to do any additional formatting.
    ###########################################################################

    ###########################################################################
    # TODO 7: Because of the power-law relationship between Nu and Re, the
    #         plot from TODO 6 should not be a straight line (there should be
    #         curvature). To create a plot with a straight line, we can instead
    #         create a log-log plot.
    #
    #         To create a log-log plot, you can use:
    #           ax.loglog()
    #          
    #         Create NEW figure and axes instance. Now, create a log-log plot
    #         of Nu vs Re. The resulting figure should be a straight line.
    ########################################################################### 




main()