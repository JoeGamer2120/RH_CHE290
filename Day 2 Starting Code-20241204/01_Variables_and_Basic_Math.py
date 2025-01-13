"""
Variables are names used to store specific pieces of information. This file 
explains the following:
    - How to declare a variable (i.e., assign information to a variable name).
    - The basic mathematical operations that are built into Python.
    - Reassigning the information contained in a variable.
"""
##############################################################################
# VARIABLE DECLARATION
#
# Variable declaration occurs when you assign a value to a variable name.
# When declaring variables, the variable name is written first followed by =
# then the numeric value (or, possibly, other information).
# 
# Example:
#   a = 5
#   Here, the value 5 is ASSIGNED to the variable a. In this case, the equal
#   sign is an ASSIGNMENT operator.
#
# TODO 1: In the space below, assign the numeric value of your age to a 
#         variable named my_age. Then print the message: My age is XX, where 
#         the XX is replaced with the value from the my_age variable.
##############################################################################

my_age = 20
print('My age is {}' .format(my_age))
print()

##############################################################################
# MATHEMATICAL OPERATIONS
#
# The following mathematical operations are pre-defined in Python:
#    +, -, *, /
#
# Examples:
#   result_plus = 2 + 2
#   result_minus = 2 - 2
#   result_times = 2 * 2
#   result_divide = 2 / 2
#
# If you want to raise a value to a power without the use of a library,
# you need to use **.
#
# Example:
#   result_power = 3**3
#
# You can also perform mathematical operations using variables that have
# values assigned to them.
#
# Example:
#   a = 1
#   b = 2
#   c = a + b
#   In this case, the variable c now contains the value 3 (1 + 2 = 3)
#
# TODO 2: In the space below, perform a calculation using the Pythagorean
#         theorem by doing the following: 
#           - On one line, assign the value 3 to a. 
#           - On the next line assign the value of 4 to b. 
#           - Next, calculate the value of c using the formula 
#             (a^2 + b^2 = c^2). Remember that the square root is equivalent 
#             to raising a value to 1/2 power. If needed, you can create an
#             intermediate value from the calculation of a^2 + b^2 before
#             performing the final calculation on the next line.
#           - Finally, print the result on the following line. You may include
#             a statement, or just print the variable.
##############################################################################

a = 3
b = 4
c = (a**2 + b**2)**0.5

print('The result is c = {}' .format(c))
print()

##############################################################################
# FLOOR DIVISION AND MODULUS
#
# Two more operations that are useful in programming are floor division and
# the modulus operator.
#
#   Floor division returns the truncated integer value of a division operation.
#   Its operator is //.
#       Example: 18 // 7 evaluates to 2.
#
#   The modulus operator returns the integer remainder of a division operation.
#   Its operator is %.
#       Example: 18 % 7 evaluates to 4
#
# TODO 3: In the space below this TODO, write lines of code that perform these
#         operations (you can use the provided example values) and print the
#         results.
##############################################################################

print("Floor division of 18//7 is", 18 // 7)
print("18 mod 7 (18%7) is", 18 % 7)
print()


##############################################################################
# VARIABLE REASSIGNMENT
#
# If a subsequent assignment is used to an existing variable, the variable will
# contain the value of the last assignment.
#
# TODO 4: Uncomment the lines below this section and run the code. You should
#         notice that the first print result shows that my_var is 10. After
#         the reassignment, the value of my_var is changed to 5.
##############################################################################

my_var = 10
print("The current value of my_var is", my_var)
my_var = 5
print("The new value of my_var is", my_var)

##############################################################################
# VARIABLE REASSIGNMENT (cont)
#
# Because of the order of execution when assigning a value to a variable, the
# variable of interest may be located on both sides of the assignment.
#
# Example:
#   my_age = 18
#   my_age = my_age + 1
#   In the 2nd line, the right-hand side gets calculated first with the current
#   value my_age. One gets added to that value, then the new value (19) gets
#   reassigned to my_age. The variable my_age now contains 19.
#
# TODO 5: In the space below this TODO, assign a value of 2.5 to a variable
#         named my_var. Next, assign a value of 3 to a variable named 
#         my_factor. On the next line, multiply my_var by my_factor and assign 
#         the result to my_var. Finally, print the result.
##############################################################################

print()
my_var = 2.5
my_factor = 3
my_var = my_var * my_factor

print(my_var)



