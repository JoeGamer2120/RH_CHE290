"""
This file explains the various ways to perform accumulation patterns.
"""

###############################################################################
# ACCUMULATING SUMS
#
# Adding together subsequent values in a series is one type of accumulation.
# The process will use a for loop to add the next value to a variable
# containing the current total.
#
###############################################################################

###############################################################################
# TODO 1: uncomment the lines within this TODO and run the code. After reading
#         through the code and the output, go to the explanation below.
#
# total = 0

# for i in range(5):
#     total = total + i
#     print("The current value of total is", total)
# #
# print("\nThe final value of total is", total)
###############################################################################

###############################################################################
# ACCUMULATING SUMS EXPLANATION
#
# In the above example, we start by INITIALIZING a variable, in this case
# 'total'. NOTE: we avoid naming the variable 'sum' because sum is a built in
# function that will sum together the values in a list.
#
# After we have ensured that the starting point of total is 0, we run a for
# loop that will start at 0 and go through 4. The current value of i will be
# added to the current value of total each time through the for loop. A print
# statement is added to show how total changes each time through the loop.
# After the loop is complete, there is a final print statement that shows the
# final value of total.
#
# NOTE: a shorter way to accumulate the above total is: total += i
#       This syntax is equivalent to total = total + i
###############################################################################

###############################################################################
# ACCUMULATING PRODUCTS
#
# Muliplying together subsequent values in a series is another type of 
# accumulation. The process will use a for loop to multiply the next value to a 
# variable containing the current total.
#
###############################################################################

###############################################################################
# TODO 2: uncomment the lines within this TODO and run the code. After reading
#         through the code and the output, go to the explanation below.
#
# total = 1

# print()  
# for i in range(1, 5):
#     total *= i
#     print("The current value of total is", total)

# print("\nThe final value of total is", total)
#
###############################################################################

###############################################################################
# ACCUMULATING PRODUCTS EXPLANATION
#
# In the above example, we start by INITIALIZING a variable, in this case
# 'total'. However, unlike when summing where we start at 0, we initilize total
# to 1 when multiplying (because starting with 0 will result in a final value
# of 0 since 0 * any number = 0).
#
# After we have ensured that the starting point of total is 1, we run a for
# loop that will start at 1 and go through 4. The current value of i will be
# multiplied with the current value of total each time through the for loop. A 
# print statement is added to show how total changes each time through the 
# loop. After the loop is complete, there is a final print statement that shows 
# the final value of total.
###############################################################################

###############################################################################
# COUNTING
#
# If you want to count the number of times an instance of something occurs, you
# will perform a counting accumulator. Each time the instance is encountered, 
# you will increment the total count by 1.
###############################################################################

###############################################################################
# TODO 3: uncomment the lines within this TODO and run the code. After reading
#         through the code and the output, go to the explanation below.
#
# count = 0
#
# for i in range(1, 30):
#     if i%3 == 0:
#         count += 1 
#         print(i, "is divisible by 3. The current count is", count)
#
# print("\nThe final count is", count)
#
###############################################################################

###############################################################################
# COUNTING EXPLANATION
#
# In the above example, we start by INITIALIZING a variable, in this case
# 'count'. As with a summing assumulator, we start at 0. 
#
# After we have ensured that the starting point of total is 0, we run a for
# loop that will start at 1 and go through 29. We then check to see if the
# modulus of i with 3 is 0. Every time that a factor of 3 is encountered, count 
# is incremented by 1 and a statement is printed. After the loop is complete, 
# there is a final print statement that shows the final value of count.
###############################################################################
