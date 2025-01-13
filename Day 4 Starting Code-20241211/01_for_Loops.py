"""
This file describes the basic syntax associated with for loops.
"""
###############################################################################
# FOR LOOPS
#
# A loop contains a sequence of commands that are to be executed until the loop
# stops. The most basic type of loop is a for loop. A for loop is executed a
# prescribed number of times. The syntax for a for loop is:
#
#    for index in range(start, stop, increment):
#
# User specified quantities:
#   - index: the user specifies the index, which a variable that stores the 
#            current value specified by the range statement.
#   - start: the initial value to be used to start the loop. If only a single
#            single value is included in the range statement, that number
#            specifies the number of times the loop is executed. In this
#            instance, the index starts at 0 and ends at stop - 1.
#   - stop:  (optional) if a stop value is specified, the loop will start the
#            index at the value of 'start' and end the loop when it reaches
#            stop - 1. (The 'stop' value is non-inclusive.)
#   - increment:
#            (optional) if an increment is specified, it designates how the
#            index will be increased (or decreased) from start to stop. If no
#            increment is included, the default is 1.   
#
# Any code to be executed within the for loop must be indented one tab.
# Indentation is the way that Python distinguishes portions of code.
###############################################################################

###############################################################################
# TODO 1: Run this program. There are 3 separate example for loops with
#         each demonstrating different ways of writing a for loop. The print
#         statement is included to illustrate how the index (in each case, i)
#         is incremented each time through the loop. Make sure you understand
#         how each syntax is different and how the incrementing works each time
#         through the loop. Once you feel comfortable with each statement,
#         go to the next TODO.
###############################################################################

# print("Single argument range statement:")
# for i in range(5):
#     print("The current index is", i)

# print()
# print("Two argument print statement:")
# for i in range(1,5):
#     print("The current index is", i)

# print()
# print("Three argument print statement:")
# for i in range(1,5,2):
#     print("The current index is", i)
    
##############################################################################
# TODO 2: Comment out the 3 examples above so that they do not print every time
#         you run the program.
###############################################################################

##############################################################################
# TODO 3: Assume that you create an account and deposit $1000 into that
#         account. Interest gets compounded annually at a rate of 5%. After
#         each year (after the interest has been added to the account), you 
#         deposit another $1000.
# 
#         Write code using a for loop that will determine how much money you 
#         will have in youraccount after each year for 5 years, and print the 
#         results. You do not have to worry about round off; however, your  
#         print statementsshould be formatted to only include 2 decimal places.
# 
#         Your output should be formatted as:
# 
#           Year     Balance
#             1      1050.00
#             2      2152.50
#             3      3310.12
#             4      4525.63
#             5      5801.91
###############################################################################

# balance = 1000
# print("Year     Balance")

# for y in range(1,6):
#     balance *= 1.05
#     print(" ", y,"     {:0.2f}" .format(balance))
#     balance += 1000
    

##############################################################################
# TODO 4: Write a for loop that uses stars and spaces to create the figure
#         below:
#                   *
#                  **
#                 ***
#                ****
#               *****
# 
#         If it helps, you can define a variable using a string (a string can
#         also be a space). Recall that if you multiply a string by N (an int), 
#         the string will be repeated N times.
###############################################################################

# for i in range(6):
#     print((5 - i) * " " + i * "*")
    
##############################################################################
# TODO 5: Write a for loop that uses stars and spaces to create the figure
#         below:
#                   *
# 
#                  ***
# 
#                 *****
# 
#                *******
###############################################################################



def tree(height):
    
    for i in range(1, height + 1):
        if (i % 2) != 0:
            space = int((height - i) / 2)
            print(space * " " + i * "*")
            
        else:
            print()
            
tree(7)
