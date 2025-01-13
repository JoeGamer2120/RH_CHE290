"""
This file provides a description of comparison and logical operators with
examples.

Comparison operators include: >, >=, <, <=, ==, !=
Logical operators include: and, or, not
"""

##############################################################################
# COMPARISON OPERATORS
#
# Comparison operators are used to compare two values to one another. The
# result of the comparison is a Boolean type of True or False. The following is
# a list of basic comparison operators:
#   >   greater than
#   >=  greater than or equal to
#   <   less than
#   <=  less than or equal to
#   ==  equal to (note that for comparison we use ==)
#   !=  not equal to
##############################################################################

##############################################################################
# TODO 1: Uncomment the 8 lines below this TODO. Inside of each print
#         statement is a comparison of two numbers that results in a Boolean.
#         The resulting Boolean then gets printed. Read each comparison and
#         determine whether the comparison is True or False. Then run the
#         program to verify the results.
##############################################################################

# print(1 == 2)
# print(1 != 2)
# print(2 == 2)
# print(2 != 2)
# print(1 > 2)
# print(1 < 2)
# print(2 > 2)
# print(2 >= 2)

##############################################################################
# LOGICAL OPERATORS
#
# Logical operators are typically used when you want to evaluate more than one
# comparison. Two such operators are:
#   and (both comparisons are True)
#   or (either comparison is True)
##############################################################################

##############################################################################
# TODO 2: Uncomment the 3 lines below this TODO. Inside of each print
#         statement are two comparisons with a logical operator. Each
#         comparison is evaluated independently, then the logical is 
#         evaluated based on the results of the comparison to result in a 
#         single Boolean result for the full statement. The resulting Boolean 
#         then gets printed. Read each statement and determine whether it is 
#         True or False. Then run the program to verify the results.
##############################################################################

# x = 11
# print(x > 0 and x < 10)
# print(x > 0 or x < 10)

##############################################################################
# LOGICAL OPERATORS (cont)
#
# A third type of logical operator that is less common is 'not'. Not
# effectively changes the result of a comparison.
# 
# The 'not' operator can be confusing. I recommend you only use it if 
# necessary.
##############################################################################

##############################################################################
# TODO 3: Uncomment the 6 lines below this TODO. Read each statement and 
#         determine whether it is True or False. Then run the program to verify 
#         the results.
##############################################################################

# x = 11
# print(not x > 0)
# print(not x < 10)
# print(not x > 0 and x < 10)
# print(not x < 10 and x > 0)
# print(not (x > 0 and x < 10))

##############################################################################
# NOTE: The last 3 statements show how use of 'not' can create confusion. 
#       Without the use of parentheses, the 3rd and 4th statements get
#       evaluated differently.
# 
#       Third example:
#           11 > 0 --> True; therefore not(11 > 0) --> False
#           11 < 10 --> False
#           (False and False) --> False
# 
#       Fourth example:
#           11 < 10 --> False; therefore not(11 < 10) --> True
#           11 > 0 --> True
#           (True and True) --> True
#
#       Fifth example:
#           11 > 0 --> True
#           11 < 10 --> False
#           (True and False) --> False
#           not(True and False) --> True
# 
#       You could create numerous such scenarios that become difficult to 
#       evaluate. If you planned/needed to use 'not' for those scenarios,
#       you should clearly think through the logic of each statement to
#       ensure that it gets evaluated properly.
##############################################################################