"""
This file provides practice on nested for loops.

"""

def main():
    """
    Uncomment the test calls below as needed.
    """
    my_savings(5)
    test_double_sum()
    test_rows_of_nums()

def test_double_sum():
    expected = 100
    actual = double_sum(4, 4)
    print("Test 1:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = 15
    actual = double_sum(1, 5)
    print("\nTest 2:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
    expected = 126
    actual = double_sum(3, 6)
    print("\nTest 3:")
    print("--------")
    print("Expected:", expected)
    print("Actual:", actual)
    
def test_rows_of_nums():
    
    r = 4
    maxnum = 3
    print("For", r, "rows with a maxnum of", maxnum)
    rows_of_nums(r, maxnum)

    r = 3
    maxnum = 7
    print("\nFor", r, "rows with a maxnum of", maxnum)
    rows_of_nums(r, maxnum) 

    r = 2
    maxnum = 8
    print("\nFor", r, "rows with a maxnum of", maxnum)
    rows_of_nums(r, maxnum)    
    
##############################################################################
# TODO 1: Recall the investment practice problem from Day 4 (01_for_Loops, TODO
#         3). Now assume that the bank compounds the interest every month. The
#         reported interest rate is 5% (for simplicity, this means that to 
#         calculate the interest rate each month, you will use (5/12)%). At the 
#         beginning of each year, you deposit another $1000.
# 
#         Write code using a nested for loop that will determine how much money
#         you will have in your account after each year for n years, and print 
#         the results. You do not have to worry about round off; however, your  
#         print statements should be formatted to only include 2 decimal places.
# 
#         After you have completed the function, run the call to the function
#         in main() with n = 5.
#
#         Your output should be formatted as (with the corresponding values
#         for n = 5):
# 
#           Year     Balance
#             1      1051.16
#             2      2156.10
#             3      3317.58
#             4      4538.47
#             5      5821.83
###############################################################################
def my_savings(n):
    """
    Complete this function according to the specifications in the TODO.

    Parameters
    ----------
    n : int
        The number of years for investing.

    Returns
    -------
    None.

    """
# This problem was done in class
    rate = 0.05
    deposit = 1000
    balance = 0
    
    print("Year     Balance") # 5 Spaces
    
    for i in range(n):
        balance += deposit
        
        for j in range(12):
            balance *= (1+rate/12) # balance = balance*rate/12 + balance
            
        print(" ", i+1, "     {:0.2f}" .format(balance))

###############################################################################
# TODO 2: Complete the function (double_sum) below according to the 
#         specifications in the doc-string. Test your function by
#         uncommenting test_double_sum() in main().
###############################################################################

def double_sum(m, n):
    """
    Assume you have an m by n matrix, where each element contains r*c (where
    r = row and c = column). For the purposes of this problem, it does not
    matter which value corresponds to rows.
    
    n is the column
    m is the row
    
    Example Matrix:
        for m = n = 3
        
                column 1  column 2  column 3
        row 1    1x1 = 1   1x2 = 2   1x3 = 3
        row 2    2x1 = 2   2x2 = 4   2x3 = 6
        row 3    3x1 = 3   3x2 = 6   3x3 = 9
    
    The function will use a nested for loop to sum the elements of the 
    hypothetical matrix.
    
    For the example matrix above:
        1 + 2 + 3 + 2 + 4 + 6 + 3 + 6 + 9 = 36

    Parameters
    ----------
    m : int
        One dimension of the matrix.
    n : int
        The other dimension of the matrix.

    Returns
    -------
    int
        A sum of the elements of the hypothetical m by n matrix.

    """
    tot = 0
    
    for i in range(n):
        for j in range(m):
            tot += (i + 1) * (j + 1)
        
    return tot
        

###############################################################################
# TODO 3: Complete the function (row_of_nums) below according to the 
#         specifications in the doc-string. Test your function by
#         uncommenting test_rows_of_nums() in main().
###############################################################################

def rows_of_nums(r, maxnum):
    """
    This function will print r rows of numbers where each number gets repeated
    by its value up to maxnum (e.g., one 1, two 2s, three 3s, etc.). See the
    examples for illustration.
    
    Example 1:
        for r = 4 and maxnum = 3
        
        1 22 333
        1 22 333
        1 22 333
        1 22 333
        
    Example 2:
        for r = 3 and maxnum = 7
        
        1 22 333 4444 55555 666666 7777777
        1 22 333 4444 55555 666666 7777777
        1 22 333 4444 55555 666666 7777777

    Parameters
    ----------
    r : int
        The number of rows to print.
    maxnum : int
        The maximum number to be used in each row.

    Returns
    -------
    None.

    """
    for i in range(r):
        print()
        for j in range(1, 1 + maxnum):
            print(j * str(j * 1), end=" ")
            
            
    
main()
        
        