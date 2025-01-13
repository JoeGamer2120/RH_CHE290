"""
This file provides a description of how functions are defined and used.
"""


##############################################################################
# FUNCTION DEFINITION
#
# A function is defined by typing 'def' followed by the name of the function
# followed by parentheses and a colon. If any parameters are to "passed" into 
# the function, they should be inserted between the parentheses and separated
# by commas.
#
# NOTE: "Passing" means information that must be supplied to the function from
#       somewhere else in the program in order for the function to run. Without
#       those parameters being supplied, the function won't run properly.
#
# See the example below for the get_celsius function. Note the doc-string that
# provides documentation stating what the function does, the function 
# parameters, their types and descriptions, and whatever information returns
# from the function.
# 
# Scroll down to TODO 1 towards the bottom of this program.
###############################################################################

def get_celsius(T_in_F):
    """
    Converts the given temperature in Farenheit into Celsius and returns the
    result.
    
    Example: If 32 is passed to the function, it returns 0.

    Parameters
    ----------
    T_in_F : float
        The temperature in Farenheit

    Returns
    -------
    float
        The temperature in Celsius

    """
    return (T_in_F - 32) * (5 /9)

##############################################################################
# FUNCTION DEFINITION (cont)
#
# If you are examining the output of running the program, you may have noticed
# that nothing happened with the function named illustration that is directly 
# below. Any function won't be executed (i.e., it won't do anything) until it
# is called.
#
# To call the function, go to TODO 2 at the bottom of this program. After you
# have completed that TODO, return to the next explanation directly below the
# illustration function.
##############################################################################

def illustration():
    """
    This function illustrates:
        1. A function only runs when called.
        2. That you need not pass information to a function.
        3. That you do not have to return information from the function.

    Returns
    -------
    None.

    """
    print()
    print("This function will only run when called.")

##############################################################################
# ILLUSTRATION FUNCTION EXPLANATION
#
# There are few noteworthy points about the illustration function.
#   1. Nothing needs to be passed to the function. You only include parameters
#      in the function definition when they are needed within the function. 
#      This function just prints a statement; therefore, it doesn't need any
#      additional information.
#   2. The function does not contain a return statement. Python uses
#      indentation to mark "sections" of code. The indentation of the two print
#      statements under the function definition tell Python that those two 
#      line are part of the function. The next actual line of code (below) has
#      the same left-justification as the function definition, which means it
#      is NOT part of the previous function. Since the function doesn't create
#      any information that should be returned, an explicit return statement
#      is optional. When nothing is explicitly returned from a function, it 
#      returns "None".
#
# Go to TODO 3 at the bottom of this program.
###############################################################################

##############################################################################
# RETURNING MULTIPLE VALUES FROM A FUNCTION
#
# When multiple values are to be returned from a function, they should all
# be located on the same line as the return statement and separated by commas.
#
# Go to TODO 4 at the bottom of the code to see this concept illustrated for
# the quadratic function below.
###############################################################################


def quadratic(a, b, c):
    """
    A quadratic equation solver.

    Parameters
    ----------
    a : float
        the coefficient in front of x^2.
    b : float
        the coefficient in front of x.
    c : float
        the constant.

    Returns 
    -------
    The roots of the quadratic

    """
    
    radical = (b**2 - 4*a*c)**0.5
    
    return (-b+radical)/2/a, (-b-radical)/2/a

###############################################################################
# TODO 1: Uncomment the three lines below this TODO and run the program.
#         Notice that the variable name being sent to the function does not
#         have to match the parameter name in the function defintion.
#
#         After you have run the program, change the value of Farenheit
#         and re-run the program. Verify that you get the correct result.
#
#         Once you understand how the function works, go to the section labeled
#         FUNCTION DEFINITION (cont)
###############################################################################

# Farenheit = 32
# T_in_C = get_celsius(Farenheit)
# print(Farenheit,"degrees Farenheit is", T_in_C, "degress Celsius")

###############################################################################
# TODO 2: Uncomment the line below this TODO and run the program.
#         After running the program, you should see the statement from
#         the function printed to the console.
#
#         After verifying that the function is running correctly, return to
#         the additional explanation about the illustration function.
###############################################################################

# illustration()

###############################################################################
# TODO 3: Uncomment the lines below this TODO and run the program.
#         After running the program, you should see that the variable contains
#         the variable None.
#
#         NOTE: You don't have to store the result in a. An alternative would
#               be: print("The value returned from the function is", 
#               illustration())
#
#         After verifying that the function is running correctly, return to
#         "Returning multiple values from a function".
###############################################################################

# a = illustration()
# print("The value returned from the function is", a)

###############################################################################
# TODO 4: In order to store all the information when multiple variables are 
#         returned from a function, your call statement should be preceded
#         by the variables that will contain the information. The order in
#         which the variables are returned will match the same order as they 
#         are placed before the function call.
#         
#         Uncomment the lines below this TODO and run the program.
#
#         NOTE: Notice that the variable names outside the function do not need
#               to match the parameters in the function definition. The values
#               contained in the variables will be passed in the order that is
#               specified by the function call. In this case, the function will
#               store the value 1 to a, -3 to b, and -4 to c. It then returns 
#               two values in the order specified. Those two values are then 
#               stored in the variables a and b OUTSIDE the function. 
#          
###############################################################################

# x = 1
# y = -3
# z = -4
# a, b = quadratic(x, y, z)
# print("The roots to the quadratic are", a, "and", b,".")