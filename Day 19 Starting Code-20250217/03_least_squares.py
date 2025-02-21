"""
This file demonstrates how to use 'least_squares' in the 'optimize' sub-module 
in SciPy to perform least squares regression of non-linear functions.

This example will use the temperature/vapor pressure data in the provided Excel
file.
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import pandas as pd


def f(c, T, Pvap):
    """
    The definition of the difference between our non-linear function (Antoine 
    equation) and the expected value for a given temperature (Pvap) (i.e., the
    residual). For this method, we will use an array (can be a tuple, list, or 
    np.array) for the parameters, and we MUST place the array FIRST in the 
    argument list. As a reminder a general form of the relationship is:
        
        log10(Pvap) = A - B/(T + C)

    Parameters
    ----------
    c: array
        a list/tuple/np.array of the Antoine coefficients.
    T : float
        the temperature.
    Pvap: float
        the vapor pressure.

    Returns
    -------
    float
        the residual.

    """
    return 10**(c[0] - c[1]/(T + c[2])) - Pvap # Residual

###############################################################################
# IMPORTING THE DATA FROM EXCEL 
#
# Here, we are importing the data from the Excel sheet Vapor Pressure Data.xlsx
#
# Then, we are assigning the columns of data to individual variables for 
# temperature and pressure by using the column header names.
#
# As point of reference, the temperatures are in Farenheit and the vapor
# pressures are in psia.
###############################################################################

data = pd.read_excel("Vapor Pressure Data.xlsx")
T = data["T"]
Pvap = data["Pvap"]

###############################################################################
# LEAST SQUARES REGRESSION 
#
# The function name that we will use is:
#   result = optimize.least_squares(f, x0, args = ())
#
# where the inputs are:
#   - f: the function we are using to for the regression
#   - x0: the initial guess of the parameters
#   - (optional) args: any other required input parameters to f     
#
# and the output is:
#   - result: an object of containing a variety of results of the regression
#
# The best-fit parameters are located in result.x
###############################################################################

result = optimize.least_squares(f, (5, 1000, 250), args = (T, Pvap))
coefs = result.x

###############################################################################
# BEST FIT CURVE 
#
# To create a visual comparison of the data and the best-fit model, we can
# create a corresponding data set of vapor pressures using the best-fit
# parameters.
#
# Since our regression function creates residuals, we can create the data set
# using the functional form of our equation (or we could create a separate
# function to perform the same task).
###############################################################################

Pmodel = 10**(coefs[0] - coefs[1]/(T + coefs[2]))

###############################################################################
# CREATING A VISUALIZATION 
#
# A visualization can now be created to compare the data to the best-fit model.
###############################################################################

fig, ax = plt.subplots()

ax.scatter(T, Pvap, label = 'data')
ax.plot(T, Pmodel, label = 'model')
ax.tick_params(direction = 'in')
ax.set_xlabel('temperature ($^oF$)')
ax.set_ylabel('vapor pressure (psia)')
ax.legend()
ax.set_title('Regression using Least Squares')

###############################################################################
# PLOT OF THE RESIDUALS 
#
# The residuals can be found in result.fun. Here, we're creating a second 
# figure to visualize the residuals.
###############################################################################

fig2, ax2 = plt.subplots()
ax2.scatter(T, result.fun)
ax2.plot(T, np.zeros(len(T)), ls = '--')
ax2.tick_params(direction = "in")
ax2.set_xlabel("temperature ($^oF$)")
ax2.set_ylabel("residual")

###############################################################################
# TODO 1: Run the program and look at the plot. 
#
#         There should be agreement between the data and the best-fit model.
###############################################################################


plt.show()