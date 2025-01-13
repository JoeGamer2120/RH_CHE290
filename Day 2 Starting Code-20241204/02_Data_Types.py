"""
Data types indicates the type of information associated with a piece (or
collection) of information. You can determine the data type of the information
contained in a variable using the type() command, or you see it in the listing
within the Variable Explorer to the right. This file describes the following 
data types in Python:
    - int
    - float
    - complex
    - str
    - bool
    - list
    - tuple
"""
##############################################################################
# NUMERIC DATA TYPES
#
# Every piece of data has a TYPE that is associated with it. The following are
# single-value, numeric data types in Python:
#    int: integer
#    float: floating point number
#    complex: complex number
#
# TODO 1: Uncomment the three lines below and run the program. You should see 
#         that each 'type' will be displayed in the console. Note the
#         difference between using 1 and 1.0.
print(type(1))
print(type(1.0))
print(type(1 + 1j))
print()
#
# Note about complex numbers: if you only want the real or imaginary part of a
# a variable, you can use the syntax <variable name>.real or 
# <variable name>.imag
#
# TODO 2: Uncomment the 3 lines below to see how you can access the real and
#         imaginary parts of a complex number.
complex_number = 3 - 4j
print(complex_number.real, type(complex_number.real))
print(complex_number.imag, type(complex_number.imag))
print()
#
# NOTE: you can see the Type (and size) of any defined variable in the Variable
#       Explorer.
##############################################################################

##############################################################################
# CHARACTER DATA TYPE
#
# A variable can also be a collection of characters. The type associated with
# this type of information is a STRING (str). When creating a string, the 
# characters must be enclosed in "" or '' (just like print statements)
#
# TODO 3: Uncomment the 3 lines below and run the program. Note that you can 
#         assign a string of characters to a variable.
my_string = "It was the best of times, it was the worst of times..."
print(my_string)
print(type(my_string))
print()
##############################################################################

##############################################################################
# BOOLEANS
#
# Booleans are typically the result of a logical operation. In Python, the 
# Boolean 'values' are True and False (first letters capitalized), and they 
# have the data type 'bool'.
#
# TODO 4: Uncomment the 2 lines below and run the program.
print(type(True)) 
print(type(False))
print()
##############################################################################

##############################################################################
# COLLECTIONS OF INFORMATION
#
# More that one piece of information can be stored in a variable. There are two
# separate data types (for now) associated with a collection: lists and tuples
# (pronounced two-pull). 
#
# The main difference between these two data types is that lists are MUTABLE, 
# which means that you can change them, while tuples are IMMUTABLE, which means 
# they cannot be altered once defined. 
#
# Lists are defined using brackets while tuples are defined used paratheses.
#
# You can use lists and tuples similar to vectors and matrices/arrays. However, 
# in this class we will use a separate data type (to be defined later) that is 
# more amenable to numerical calculations. 
#
# TODO 5: Uncomment 7 lines below and run the program. 
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(my_list)
print(type(my_list))
print()
print(my_tuple)
print(type(my_tuple))
print()
##############################################################################

##############################################################################
# MUTABILITY
# 
# TODO 6: Uncomment the 5 lines below this TODO and run the program. (Make sure
#         that the list and tuple definitions ABOVE are not commented out.)
print(my_list)
print(my_tuple)
my_list[0] = 5
#my_tuple[0] = 5
print(my_list)
print()
# 
# You should have received a TypeError. In two lines of the code above, we are
# attempting to reassign new values contained in the first location of the list
# and the tuple. The error results from the fact that once you have defined a 
# tuple, you cannot 'mutate' (i.e., alter) the information it contains.
# 
# NOTE: Notice that the first value in the list and tuple has an index = 0.
#       Python starts a collection with an index of 0.
# 
# TODO 7: Comment out the line that attempts to mutate my_tuple[0] and re-run
#         the program. Notice that the first value in the list has changed
#         for the 2nd print statement.
##############################################################################

##############################################################################
# CHANGING DATA TYPES
# 
# There may be occasions where you need to alter the data type of a variable.
# One example is where you have a float but it must be an int to be used in a
# different part of the code. You can use the type descriptor to make this 
# change.
# 
# TODO 8: Uncomment the 4 lines below this TODO and run the program. Notice
#         that we are forcing b to be an integer based on the value stored. The
#         last line illustrates that you can also take advantage of the floor
#         division operator to achieve the same result.
a = 100/3
b = int(a)
print(type(b), b)
print(type(100//3), 100//3)
print(type(a), a)
##############################################################################