"""
This file illustrates nested for loop (i.e., a for loop inside of a for loop).
"""

def main():
    """
    Uncomment the function calls below to run each example.

    """
    # example_1(5)
    # example_2(3, 5)
    example_3(5)

##############################################################################
# TODO 1: Below are 3 examples of nested for loops. Uncomment the call to each
#         example individually to see the result of the code.
###############################################################################

def example_1(n):
    for i in range(n):
        print("\nRow", i+1, end=":  ")
        for j in range(n):
            print(j, end ="  ")
        

def example_2(r, c):
    count = 0
    for i in range(r):
        for j in range(c):
            count += 1
            if count < 10:
                print(count, end="   ")
            else:
                print(count, end="  ")
        print()

def example_3(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()


main()