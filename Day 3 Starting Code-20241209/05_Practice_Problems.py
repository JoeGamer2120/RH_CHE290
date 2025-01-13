"""
This file contains practice problems for today's topics. If you do not complete
the TODOs during class, you should finish them outside of class. This is not
a homework assignment. You WILL NOT turn in your work.

You should ask questions when you have them. Feel free to work with a friend,
but you will be responsible for understanding the concepts.
"""

import numpy as np

def main():
    "calls to unit tests"
    # test_surface_area()
    # test_volume()
    # test_my_401k() 
    
def test_surface_area():
    """
    Tests the surface_area function.

    Returns
    -------
    None.

    """
    expected = 4.0
    actual = surface_area(1/np.sqrt(np.pi))
    print("------------------------")
    print("Test 1:")
    print("Expected (about):", expected)
    print("Actual: ", actual)
    print()
    
    expected = 12.5664
    actual = surface_area(1)
    print("\n------------------------")
    print("Test 2:")
    print("Expected (about):", expected)
    print("Actual: ", actual)
    print()
    
def test_volume():
    """
    Tests the volume function

    Returns
    -------
    None.

    """
    expected = 4/3
    actual = volume(1/np.pi**(1/3))
    print("------------------------")
    print("Test 1:")
    print("Expected (about):", expected)
    print("Actual: ", actual)
    print()
    
    expected = 4.1888
    actual = volume(1)
    print("\n------------------------")
    print("Test 2:")
    print("Expected (about):", expected)
    print("Actual: ", actual)
    print()
    
def test_my_401k():
    """
    Tests the my_401k function.

    Returns
    -------
    None.

    """
    my_expected = 1500.0
    match_expected = 1500.0
    my_actual, match_actual = my_401k(15000)
    print("------------------------")
    print("Test 1: 15k")
    print("Expected max savings:", my_expected)
    print("Actual max savings: ", my_actual)
    print("\nExpected max match:", match_expected)
    print("Actual max match: ", match_actual)    

    my_expected = 3500.0
    match_expected = 3250.0
    my_actual, match_actual = my_401k(35000)
    print("\n------------------------")
    print("Test 2: 35k")
    print("Expected max savings:", my_expected)
    print("Actual max savings: ", my_actual)
    print("\nExpected max match:", match_expected)
    print("Actual max match: ", match_actual)
    
    my_expected = 7200.0
    match_expected = 4500.0
    my_actual, match_actual = my_401k(75000)
    print("\n------------------------")
    print("Test 3: 75k")
    print("Expected max savings:", my_expected)
    print("Actual max savings: ", my_actual)
    print("\nExpected max match:", match_expected)
    print("Actual max match: ", match_actual) 
    
    my_expected = 9200.0
    match_expected = 4500.0
    my_actual, match_actual = my_401k(100000)
    print("\n------------------------")
    print("Test 4: 100k")
    print("Expected max savings:", my_expected)
    print("Actual max savings: ", my_actual)
    print("\nExpected max match:", match_expected)
    print("Actual max match: ", match_actual)
    
    my_expected = 9200.0
    match_expected = 0
    my_actual, match_actual = my_401k(120000)
    print("\n------------------------")
    print("Test 5: 120k")
    print("Expected max savings:", my_expected)
    print("Actual max savings: ", my_actual)
    print("\nExpected max match:", match_expected)
    print("Actual max match: ", match_actual)
    
###############################################################################
# TODO 1: Complete the function below that determines the surface area of a 
#         sphere of radius r.
# 
#         Once you have completed the function, uncomment the CALL to the 
#         testing function (test_surface_area) at the bottom of this file.
#         Add at least one more test case to the testing function.
###############################################################################

def surface_area(r):
    """
    Determines the surface area of a sphere.
    
    Recall that for a sphere: A = 4*pi*r^2

    Parameters
    ----------
    r : float
        the radius of a sphere.

    Returns
    -------
    float
        the surface area of a sphere with radius r.

    """
    return 4 * np.pi * r ** 2


###############################################################################
# TODO 2: Complete the function below that determines the volume of a sphere
#         of radius r.
# 
#         Once you have completed the function, uncomment the CALL to the 
#         testing function (test_volume) at the bottom of this file.
#         Add at least one more test case to the testing function.
###############################################################################
    
def volume(r):
    """
    Determines the volume of a sphere.

    Recall that for a sphere: V = 4/3*pi*r^3

    Parameters
    ----------
    r : float
        the radius of a sphere.

    Returns
    -------
    float
        the volume of a sphere with radius r. 

    """
    return 4 / 3 * np.pi * r**3
    


###############################################################################
# TODO 3: Many companies provide some form of a matching contribution to an
#         employees 401(k) contribution. This problem illustrates a
#         fictitious example of one company's structure.
# 
#         Income            Max Savings                Max Company Match
#         --------------------------------------------------------------------
#         $0 - $30k            10%                             10%
# 
#         $30k - $60k          10%                     10% for first $30k
#                                                      5% for amount above $30k
# 
#         $60k - $100k     10% up to $60k              10% for first $30k
#                          8% for amount above $60k    5% for amount above $30k
#                                                      nothing above $60k
# 
#         above $100k      10% up to $60k              $0 (employee receives
#                          8% for amount between           stock options)
#                                $60k and $100k
#                          nothing for amount above $100k
# 
#         Complete the function below, my_401k, that will receive the 
#         employee's income and determine the employee's max savings
#         and the company's max match. The function will then return both
#         values. Assume that the upper limits on the income ranges are 
#         inclusive.
# 
#         Once you have completed the function, uncomment the CALL to the 
#         testing function (test_my_401k) at the bottom of this file. You do
#         not have to create a test case.
###############################################################################

def my_401k(income):
    """
    Determines the maximum employee contribution and employer match based on
    the employee's income.

    Parameters
    ----------
    income : float
        The employee's income in dollars.

    Returns
    -------
    Two floats. One value will be the employee's max and the other will be 
    the company's max match. They should be returned in that order.

    """
    if income > 0 and income <= 30000:  # Income between 0 and 30000
        max_saving = income * 0.1
        max_match = income * 0.1 
        
    elif income > 30000 and income <= 60000: # Income between 30k and 60k
        max_saving = income * 0.1 
        max_match = 30000 * 0.1 + (income - 30000) * 0.05
        
    elif income > 60000 and income <= 100000: # Income between 60k and 100k
        max_saving = 60000 * 0.1 + (income - 60000) * 0.08
        max_match = 30000 * 0.1 + 30000 * 0.05
        
    elif income > 100000:                   # Income over 100k
        max_saving = 60000 * 0.10 + (100000-60000) * 0.08
        max_match = 0
        
    else:
        print("Income must be positive.")
        
    return max_saving, max_match


    

###############################################################################
# TODO 4: Suppose that we want to determine if a user-provided integer is
#         positive. The easist way to determine if a number is even is to
#         calculate the modulus of that number with 2. If the modulus (i.e.,
#         the remainder) is 0, then the number is even.
#
#         In the lines below this TODO, write the code that will ask the user
#         to provide an integer value and print a statement if that integer is
#         even.
###############################################################################

# num = int(input("Number to check even or odd: "))

# mod = num % 2
# if mod == 0 :
#     print("Your number is even.")
# else:
#     print("Your number is odd.")
###############################################################################
# TODO 5: Using the same idea in TODO 1, in the lines below this TODO, write 
#         the code that will ask the user to provide an integer value. The code
#         will then print a statement about whether the provided value is odd
#         or even.
###############################################################################

###############################################################################
# There are usually a variety of ways to achieve the same goal within a
# program. Whenever possible, the most efficient (i.e., computationally
# inexpensive) path should be chosen, though efficiency is typically
# developed through experience. Beyond that, however, every coder has their
# own preferences for style, aesthetics, structure, etc. The last 2 TODOs 
# illustrate two ways to perform the same task.
###############################################################################

###############################################################################
# TODO 6: Think back to the example code where we determined whether the user-
#         input value was positive, negative, or zero. Now, we not only want
#         to determine the numbers sign, but also whether it is odd or even.
# 
#         Below this TODO, write the code that will ask the user to enter an
#         integer value and determine whether that number is one of the
#         following possibilities:
#           - zero
#           - positive and even
#           - positive and odd
#           - negative and even
#           - negative and odd
#
#         To complete this TODO, you must "nest" your decisions, where
#         "nesting" means to put something inside of something else.
#         Specifically, here it means to put a decision inside of a decision.
#         In other words, you will NOT use a logical operator.
#
#         Recommendation: Make you "outer" decision structure in based on the
#                         sign. Then, within those decisions make the odd/even
#                         determination.
###############################################################################

num = int(input("Your number is: "))
print()

# if num == 0 :
#     print("Your number is zero.")

# elif (num % 2) == 0 :
#     if num > 0 :
#         print("Your number is postiive and even.")
#     else:
#         print("Your number is negative and even")
        
# else:
#     if num > 0 :
#         print("Your number is postiive and odd.")
#     else:
#         print("Your number is negative and odd.")
    

###############################################################################
# TODO 7: Redo the previous problem except, this time, do not nest your
#         decisions. Instead, use logical operators (as necessary) to complete
#         the task.
###############################################################################

if num == 0:
    print("Your number is zero.")
elif num > 0 and (num % 2) == 0:
    print("Your number is positive and even.")
elif num > 0 and (num % 2) != 0 :
    print("Your number is positive and odd.")
elif num < 0 and (num % 2) == 0 :
    print("Your number is negative and even.")
else:
    print("Your number is negative and odd.")
    

###############################################################################
# CHALLENGE PROBLEM
#
# One last consideration for your code is clarity. Making clear, concise code
# makes it easier for others to understand what you are trying to accomplish.
# (Adding useful comments is also good practice.)
#
# One solution for TODO 7 requires only one logical operator without nesting 
# any decisions. See if you can complete this task as an extra challenge. After
# you have completed the task (if you are able to do so) ask yourself if the 
# increase in efficiency (fewer comparisons = less computation) is too much to 
# the detriment of clarity. (The efficiency is probably not worth the lack of
# clarity.)
###############################################################################



main()