"""
This file contains practice problems for today's topics. If you do not complete
the TODOs during class, you should finish them outside of class. This is the 
only file that you will turn in for this week's "weekly code" assignment.

You should ask questions when you have them. Feel free to work with a friend,
but you will be responsible for understanding the concepts.
"""
import numpy as np
##############################################################################
# TODO 1: In the space below this TODO, perform a calculation that determines 
#         the temperature and the work for compression when the pressure is 
#         10 atm. The governing equations can be found in the provided pdf.
#         You should define the following parameters (their values are also
#         provided in the pdf):
#         
#           P, Po, To, g, Cp, m_air
#
#         If you want to include units with a quantity, you can place those
#         units directly after a # on the same line as the variable
#         declaration. For example:
#           P = 10 # atm
# 
#         Perform the calculations for T and W. Remember that you should
#         refer to the variables containing the numeric information. In
#         other words, your equation will be symbolic. The calculation will
#         be performed properly because the variables will contain numeric 
#         information.
# 
#         After the lines performing the calculation, write the code that 
#         will print the following statements on their own lines:
#           The temperature is XX K.
#           The work is XX kJ.
# 
#         For the XX, you should use the variable that contains the 
#         corresponding quantity. It is up to you whether to format the numeric
#         information. The answers that you get should be (about):
#           T = 675.644 K
#           W = 1496.63 kJ
##############################################################################

P = float(input("What pressure (in atm) is compression occuring: "))
Po = 1 # atm
To = 350 # K
g = 1.4 # unitless
Cp = 1.021 # kJ/kg*K
m_air = 4.5 # kg

# Temp Calculation
exp = (g-1) / g
pre = P / Po
T = To * pre**exp
print('The temperature is {:0.3f} K' .format(T))

# Work Calculation
W = m_air * Cp * (T-To)
print("The work necessary for this compression is {:0.2f} kJ" .format(W))

##############################################################################
# TODO 2: Modify the previous problem that will prompt the user for a value of 
#         P instead of defining it in the code. You may use any wording that
#         is appropriate for the message. Try the problem with different values
#         of P.
##############################################################################

##############################################################################
# TODO 3: In the space below this TODO, perform a calculation that determines 
#         the vapor pressure of water at a given temperature. The equation for
#         the vapor pressure can be found in the provided pdf. You should 
#         define the following parameters using the values provided in the pdf:
#         
#           A, B, C
# 
#         Perform the calculation for T = 100 C and store the result in a
#         variable called p_vap. Define a conversion factor for the 
#         pressure from units of torr to bar. You may call the variable 
#         whatever you want. The conversion is 1.01325 bar = 760 torr.
#         Convert the vapor pressure from torr to bar.
# 
#         After the lines performing the calculation, write the code that 
#         will print the following statement on its own lines:
#           The vapor pressure of water at XX C is XX bar.
# 
#         For the XX, you should use the variable that contains the 
#         corresponding quantity. It is up to you whether to format the numeric
#         information. The answers that you get should be (about):
#           Pvap = 1.013 bar
##############################################################################

A = 8.05573
B = 1723.64
C = 233.076

T = float(input("What temperature (degree C) is the system at? "))

num = A - B / (T+C)
Pvap = 10 ** num # torr
Pvap = Pvap * (1.01325/760) # bar

print('The vapor pressure of water at {:0.3f} C is {:0.3f} bar.' .format(T,Pvap))



##############################################################################
# TODO 4: Modify the previous problem that will prompt the user for a value of 
#         T instead of defining it in the code. You may use any wording that
#         is appropriate for the message. Try the problem with different values
#         of T.
##############################################################################

##############################################################################
# TODO 5: In the space below this TODO, determine the angle (in degrees) when
#         sin(theta) = 2^(1/2)/2, and print the result. Remember that you can 
#         use the DOT TRICK to find the function in NumPy for the arcsin. You 
#         can complete this task in as many steps as needed. (For a challenge,
#         try to complete this TODO in one line.)
#         
#         As a reminder, there are pi radians in 180 degrees.
##############################################################################

theta = np.arcsin(2**(0.5) / 2) # rad
theta = theta * (180/np.pi) # deg
print(theta)

##############################################################################
# TODO 6: Assume that you create an account and deposit $1000 into that
#         account. Interest gets compounded annually at a rate of 5%. Assume
#         the interest gets added at the end of the year, and you deposit 
#         another $1000 at the beginning of each year.
#
#         As a reminder, the accumulated interest on a balance is:
#               interest = balance*interest_rate   
# 
#         Write code that will determine how much money you will have in your
#         account after 5 years, and print the result. You do not have to worry
#         about round off; however, your print statement should be formatted
#         to only include 2 decimal places.
# 
#         You should get $5801.91 
# 
#         NOTE 1: If you are familiar with loops, DO NOT use a loop to 
#                 complete this problem. We will return to this problem
#                 after we learn about loops.
# 
#         NOTE 2: While a formula exists to complete this calculation in one
#                 step, you must perform the calculation step-by-step.
##############################################################################

years = 5
rate = 0.05

# Year 1
bal = 1000
interest = bal * rate
bal = bal + interest

# Year 2
bal = bal + 1000
interest = bal * rate
bal = bal + interest

# Year 3
bal = bal + 1000
interest = bal * rate
bal = bal + interest

# Year 4
bal = bal + 1000
interest = bal * rate
bal = bal + interest

# Year 5
bal = bal + 1000
interest = bal * rate
bal = bal + interest

print ('After 5 years, the total balance will be {:0.2f}' .format(bal))


