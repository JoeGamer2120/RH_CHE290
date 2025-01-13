"""
This file illustrates two acceptable ways to execute while loops.
"""

def main():
    """
    Calls to the example functions


    """
    sum_of_values_1()
    sum_of_values_2()  

###############################################################################
# WHILE LOOPS
#
# A second type of loop is a 'while' loop. Where a 'for' loop has a pre-defined 
# number of iterations through the loop, a 'while' loop only stops based on
# conditions set by the programmer.
#
# One way of writing a 'while' loop is:
#   
#     while conditional_statement:
#        
# In this case, the while loop will continue as long as the conditional
# statement is True. There are two implications of this type of while loop:
#     1. You must ensure that the conditional statement is True before the loop
#        is encountered (assuming you want the loop to be executed).
#     2. The only way for the loop to break is for something to change inside 
#        of the loop that eventually results in the conditional being False.
###############################################################################

###############################################################################
# TODO 1: Uncomment and run the example below. The code is written to find the
#         integer value of x where 1/x is less than 0.04.
# x = 1
# while 1/x >= 0.04:
#     x += 1
# print("1/x is less than 0.04 when x =", x)
###############################################################################

###############################################################################
# WHILE LOOPS (CONT)
#
# Another way of writing a 'while' loop is:
#
#     while True:
#    
# In this case, the loop will automatically execute because its condition is 
# defined as True. The only way to end the loop is for the code to contain a
# conditional that will 'break' the loop.
#
###############################################################################

###############################################################################
# TODO 2: Uncomment and run the example below. The example is analogous to the
#         code above, but uses a "while True" statement instead.
# x = 0
# while True:
#     x += 1
#     if 1/x < 0.04:
#         break
# print("1/x is less than 0.04 when x =", x)
###############################################################################


###############################################################################
# WHILE LOOP FORMS
#
# Case 2 Note: if the loop is part of a function, a possible alternative to
#              'break' the loop is to 'return' from the function. This option
#              is dependent on the nature of the function.
#
# Either syntax is acceptable. Personal preference may partially dictate which
# form you will use. However, some problem types may lend themselves better to
# one form over the other. 
###############################################################################    

###############################################################################
# TODO 3: The two functions below perform the same task of adding together user
#         input integers. The first function uses a while with a conditional,
#         while the function uses a while True statement. 
#
#         Uncomment the function call to the first example at the bottom of the
#         file. Enter the following values in order: 1, 2, 3, 4, 0. The total
#         should be 10.
# 
#         After you have completed the first example, comment out the function
#         function call, uncomment the function call to the second example and
#         run the program with the same values.
#
#         Examine the differences between the structure of the code that allow
#         function to work properly based on the while loop form used.
###############################################################################

def sum_of_values_1():
    total = 0
    
    new_value = 1
    
    while new_value != 0:
        print("Enter 0 to end the loop.")
        new_value = int(input("Enter the next value to add: "))
        total += new_value
    
    print("The total of your values is", total)
    
def sum_of_values_2():
    total = 0
    
    while True:
        print("Enter 0 to end the loop.")
        new_value = int(input("Enter the next value to add: "))
        
        if new_value == 0:
            break
        
        total += new_value
    
    print("The total of your values is", total)


main()







