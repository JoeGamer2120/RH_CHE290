"""
Complete this problem by following the TODOs and referencing the equations
provided in the problem statement.

YOUR NAME:
"""

import numpy as np
from scipy import optimize
import pandas as pd
import matplotlib.pyplot as plt


def main():
    a = 0.3
    P, x, y, P1_vap, P2_vap = get_data()
    G_exp = G_data(P, x, y, P1_vap, P2_vap)
    tau_12, tau_21 = regress_parameters(a, x, G_exp)
    # test_regression(tau_12, tau_21)
    # test_NRTL()
    P_m, x_m, y_m = model_value(a, tau_12, tau_21, P1_vap, P2_vap)
    make_plot(P, x, y, P_m, x_m, y_m)


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
    # P_f = excel.iloc[1:16, 0:1]
    # x1_f = excel.iloc[1:16, 1:2]
    # y1_f = excel.iloc[1:16, 2:3]
    # P1_vap_f = excel.iloc[16:17, 0:1]
    # P2_vap_f = excel.iloc[0:1, 0:1]
    
    # P = P_f.to_numpy()
    
    # x1 = x1_f.to_numpy()
    
    # y1 = y1_f.to_numpy()
    
    # P1_vap = P1_vap_f.to_numpy()
    # P2_vap = P2_vap_f.to_numpy()
    
    data = excel.to_numpy()
    P = data[1:16, 0]
    x1 = data[1:16, 1]
    y1 = data[1:16, 2]
    P1_vap = data[16, 0]
    P2_vap = data[0, 0]

    return P, x1, y1, P1_vap, P2_vap


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
    x2 = 1 - x
    y2 = 1 - y
    
    gamma_1 = y*P / (x*P1_vap)
    gamma_2 = y2*P / (x2*P2_vap)  

    return x*np.log(gamma_1) + x2*np.log(gamma_2)


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
    x2 = 1 - x
    G12 = np.exp(-a*tau[0])
    G21 = np.exp(-a*tau[1])
    
    G_model = x*x2*((tau[1]*G21 / (x + x2*G21)) + (tau[0]*G12 / (x2 + x*G12)))
    
    G_resid = G_exp - G_model

    return G_resid


def regress_parameters(a, x, G_exp):
    ###########################################################################
    # TODO 4: Complete this function to solve the problem using least squares.
    #
    #         Use 1 for the initial guesses of both parameters.
    #
    #         When you are done, run the test in main() to ensure your function
    #         is working correctly.
    ###########################################################################
    results = optimize.least_squares(G_resid, (1, 1), args = (a, x, G_exp))
    coeff = results.x

    return coeff


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
    x1 = x
    x2 = 1 - x
    G12 = np.exp(-a*tau12)
    G21 = np.exp(-a*tau21)
    
    gam1 = np.exp(x2**2 * (tau21 * (G21 / (x1 + x2*G21))**2 + (tau12*G12 / (x2 + x1*G12)**2)))
    gam2 = np.exp(x1**2 * (tau12 * (G12 / (x2 + x1*G12))**2 + (tau21*G21 / (x1 + x2*G21)**2)))

    return gam1, gam2


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
    x1 = np.linspace((0, 1), 51)
    ###########################################################################
    # TODO 7: Determine the pressures for each value of your x vector.
    ###########################################################################
    x2 = 1 - x1
    gam1, gam2 = NRTL(x1, a, tau12, tau21)
    P = x1*gam1*P1_vap + x2*gam2*P2_vap
    ###########################################################################
    # TODO 8: Determine the y values for each value of your x vector.
    #
    #         After you complete this function, you can compare the figure
    #         created using make_plot to the figure included in the download.
    ###########################################################################
    y = x1*gam1*P1_vap/P
    return P, x1, y


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
    plt.show()


main()

