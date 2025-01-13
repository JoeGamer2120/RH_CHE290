"""
This files explains how we can make decisions within a program by using
conditional statements (if/elif/else structures).
"""

###############################################################################
# BASIC CONDITIONALS
#
# Conditional statements are used to make decisions within a program. The most 
# basic form of a conditional uses an 'if' statement. The syntax of an if
# statement is:
#   if (conditional expression):
#       code
#
# The conditional expression is created using comparison and, if necessary, 
# logical operators.  
#
# The result of checking a conditional expression will be either True or False
# (the result is not printed). If the result is True, the portion of the code
# associated with the if statement (the code with a single indention from the
# word 'if') is executed. If the result is False, the if statement code is 
# skipped.
###############################################################################

###############################################################################
# TODO 1: Suppose that we want to determine whether a user-provided integer
#         is positive. 
#
#         Uncomment the lines below, then run the code. Use a variety of 
#         positive and negative values (and even 0) to verify that the code is 
#         working properly.
#
# user = int(input("Enter an integer value and I will tell you if it's positive: "))
# if user > 0:
#     print()
#     print(user, "is a positive number.")
###############################################################################


###############################################################################
# MORE CONDITIONALS
#
# The previous conditional example only used an if statement. In that instance
# code was only executed when the conditional was True. If, on the other hand,
# we want one set of commands to be executed when the conditional is True and
# a different set of commands to be executed when the conditional is False, we
# we can use an if/else statement.
###############################################################################

###############################################################################
# TODO 2: Now assume that we want print one statement if the value is positive
#         and a separate statement if the value is not positive.
#
#         Uncomment the lines below, then run the code. Use a variety of 
#         positive and negative values (and even 0) to verify that the code is 
#         working properly.
# 
# print("Enter an integer value and")
# user = int(input("I will tell you whether or not it's positive: "))
# if user > 0:
#     print()
#     print(user, "is a positive number.")
# else:
#     print()
#     print(user, "is not a positive number.")    
###############################################################################
    
###############################################################################
# Notice how we do not need to use a conditional statement on the 'else' line
# because the term 'else' encompasses any scenario that was not true for the
# 'if' statement (i.e., if 3 is not even, it must be odd).
###############################################################################

###############################################################################
# EVEN MORE CONDITIONALS
#
# When more that two options are possible, an if/elif/else statement can be
# used. The term 'elif' means 'else if', which essentially means that if the
# initial if statement is False (else) but a second conditional expression is
# True, then execute the commands associated with elif. elif REQUIRES a
# conditional expression.
###############################################################################

###############################################################################
# TODO 3: Now assume that we want print one statement if the value is positive
#         a separate statement if the value is negative, and a third
#         statement if the value is 0.
# 
#         Uncomment the lines below, then run the code. Use a variety of 
#         positive and negative values (and even 0) to verify that the code is 
#         working properly.
# 
# print("Enter an integer value and I will tell you whether")
# user = int(input("it's positive, negative, or zero: "))
# if user > 0:
#     print()
#     print(user, "is a positive number.")
# elif user < 0:
#     print()
#     print(user, "is a negative number.")   
# else:
#     print()   
#     print("You entered 0.")
###############################################################################

###############################################################################
# ONE MORE POINT ABOUT CONDITIONALS
#
# As else statement is not a requirement of the decision structure. If nothing
# is supposed to happen for situations where if and elifs are all False, else
# can be excluded.
###############################################################################

###############################################################################
# TODO 4: Uncomment and run the code below this TODO. The code is a
#         modification of the previous TODO, but with the scenario for
#         user entering 0 being left off.
#
# print("Enter an integer value and I will tell you whether")
# user = int(input("it's positive or negative: "))
# if user > 0:
#     print()
#     print(user, "is a positive number.")
# elif user < 0:
#     print()
#     print(user, "is a negative number.")   
###############################################################################

