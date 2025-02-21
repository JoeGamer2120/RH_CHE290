"""
Complete this problem by following the TODOs and referencing the equations
provided in the problem statement.

YOUR NAME:
"""

from os import wait
import numpy as np
from scipy import optimize
import pandas as pd
import matplotlib.pyplot as plt


def main():
    a = 0.3
    P, x, y, P1_vap, P2_vap = get_data()
    # G_exp = G_data(P, x, y, P1_vap, P2_vap)
    # tau_12, tau_21 = regress_parameters(a, x, G_exp)
    # test_regression(tau_12, tau_21)
    # test_NRTL()
    # P_m, x_m, y_m = model_value(a, tau_12, tau_21, P1_vap, P2_vap)
    # make_plot(P, x, y, P_m, x_m, y_m)


def test_regression(tau_12, tau_21):
    expected = [1.321645, 0.870953]
    actual = [tau_12, tau_21]
    print("Regression Test:")
    print("----------------")
    print("Expected:", expected)
    print("Actual:", actual)


def test_NRTL():
    expected = (4.08475, 1.2597)
    actual = NRTL(0.3, 0.2, 2.2, 1.3)
    print("NRTL Test:")
    print("----------------")
    print("Expected:", expected)
    print("Actual:", actual)


def get_data():
    ###########################################################################
    # TODO 1: Import the data from the Excel spreadsheet. While it is not
    #         necessary, I recommend you convert the data to numpy arrays (if
    #         nothing else, it helps the code to run slightly faster.)
    #
    #         You will be returning the following variables in order:
    #                P, x1, y1, P1_vap, P2_vap
    #
    #         You will not use the first and last data points in your
    #         calculations, so the first three variables should NOT contain
    #         those points. (The final size of the vectors should be 15.)
    #
    #         The first pressure corresponds to the vapor pressure of species 2
    #         and the last pressure corresponds to the vapor pressure of
    #         species 1.
    ###########################################################################
    excel = pd.read_excel("VLE data.xlsx")
    # P_col = excel["P"]
    # x1_col = excel["x1"]
    # y1_col = excel["y1"]
    P = excel[2:17, :1]
    x1 = excel[2:17, 1:2]
    y1 = excel[2:17, 2:3]
    P1_vap = excel[16:17, :1]
    P2_vap = excel[2:3, :1]

    return


def G_data(P, x, y, P1_vap, P2_vap):
    """
    This function will calculate the values of G using the data. (See the
    equations in the assignment.)

    Parameters
    ----------
    P : ndarray
        A vector of pressures.
    x : ndarray
        A vector of x-values for species 1.
    y : ndarray
        A vector of y-values for species 1.
    P1_vap : float
        The vapor pressure of species 1.
    P2_vap : float
        The vapor pressure of species 2.

    Returns
    -------
    ndarray
        A vector of experimental values of G.

    """

    ###########################################################################
    # TODO 2: Calculate the values of G_ex from the data.
    ###########################################################################

    return


def G_resid(tau, a, x, G_exp):
    """
    This function will calculate the residuals of G from the data and the
    model.

    This is the function you will use in the least squares regression to
    determine the interaction parameters (tau).

    Parameters
    ----------
    tau : list
        A list containing the interaction parameters (tau_12 and tau_21) for
        NRTL model.
    a : float
        The alpha parameter in the NRTL model.
    x : ndarray
        The x-values for species 1 from the data.
    G_exp : ndarray
        A vector of experimental values of G.

    Returns
    -------
    ndarray
        The residuals of G for the data and the model.

    """
    ###########################################################################
    # TODO 3: Calculate the values of G_ex using the model. Return the
    #         residuals.
    ###########################################################################

    return


def regress_parameters(a, x, G_exp):
    ###########################################################################
    # TODO 4: Complete this function to solve the problem using least squares.
    #
    #         Use 1 for the initial guesses of both parameters.
    #
    #         When you are done, run the test in main() to ensure your function
    #         is working correctly.
    ###########################################################################

    return


def NRTL(x, a, tau12, tau21):
    """
    This function will calculate the activity coefficients for both species
    in a binary mixture.

    Parameters
    ----------
    x : float
        The mole fraction of species 1 in the mixture.
    a : float
        The alpha parameter for the NRTL model.
    tau12, tau21 : floats
        The interaction parameters for the NRTL model


    Returns
    -------
    floats
        The activity coefficients of both species.

    """
    ###########################################################################
    # TODO 5: Complete this function to calculate the activity coefficients
    #         of both species in the mixture.
    #
    #         When you are done, run the test in main() to ensure your function
    #         is working correctly.
    ###########################################################################

    return


def model_value(a, tau12, tau21, P1_vap, P2_vap):
    """
    This function will calculate values of P, x, and y using the regressed
    model parameters.

    Parameters
    ----------
    a : float
        The alpha parameter for the NRTL model.
    tau12, tau21 : floats
        The interaction parameters for the NRTL model
    P1_vap : float
        The vapor pressure of species 1.
    P2_vap : float
        The vapor pressure of species 2.

    Returns
    -------
    ndarray
        Calculated pressure values using the model.
    ndarray
        A vector of x values.
    ndarray
        Calculated y-values using the model.

    """
    ###########################################################################
    # TODO 6: Create a vector of x values from 0 to 1 using 51 data points.
    ###########################################################################

    ###########################################################################
    # TODO 7: Determine the pressures for each value of your x vector.
    ###########################################################################

    ###########################################################################
    # TODO 8: Determine the y values for each value of your x vector.
    #
    #         After you complete this function, you can compare the figure
    #         created using make_plot to the figure included in the download.
    ###########################################################################

    return


def make_plot(P, x, y, P_m, x_m, y_m):

    fig, ax = plt.subplots()

    ax.scatter(x, P)
    ax.scatter(y, P)
    ax.plot(x_m, P_m)
    ax.plot(y_m, P_m)
    ax.tick_params(direction="in")
    ax.set_xlabel("mole fraction 1")
    ax.set_ylabel("P (mmHg)")
    ax.set_xlim(0, 1)


main()

