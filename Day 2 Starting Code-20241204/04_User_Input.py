"""
To make programs useful for a variety of circumstances depending on the user's
needs, you may need to prompt the user for input. This file demonstrates how 
you can get the desired user input based on the program's needs.
"""

##############################################################################
# USER INPUT
#
# If you would like to prompt the user to provide information, you can do so
# using the input command.
#
# Syntax:
#   variable_name = input("message")
#
# The "message" will be displayed in the Console with a prompt for the user to
# enter information, which will then be stored in the variable_name used.
#
# TODO 1: Uncomment the three lines below and run the program. Enter any value
#         at the prompt in the Console. Note that the data type of 'user' is a 
#         string. As a result, notice what happens with user*2 (it prints the
#         string twice).
user = input("Enter a value: ")
print(user, type(user))
print(user*2)
print()
##############################################################################

##############################################################################
# USER INPUT (NUMERIC INFORMATION)
#
# If you would prefer that the user provide numeric information, you can do so
# by forcing a data type on the user input. You do this by enclosing the input
# statement with int() or float().
#
# TODO 2: Uncomment the three lines below and run the program. The first time
#         you run the program, enter any integer value and observe the results.
#         Run the program again and try a float (5.1, for example). You should
#         receive a 'ValueError'. Run the program for a third time a try a
#         string (you do not need to enclose the characters in ""). You should
#         again receive a 'ValueError'.   
user = int(input("Enter a value: "))
print(user, type(user))
print(user*2)
#
# TODO 3: Uncomment the three lines below and run the program. The first time
#         you run the program, enter any float and observe the results.
#         Run the program again and try an int (5, for example). You should
#         not receive an error this time because Python will treat the int as a
#         float. Run the program for a third time a try a string. You should
#         receive a 'ValueError'. 
user = float(input("Enter a value: "))
print(user, type(user))
print(user*2)
##############################################################################
