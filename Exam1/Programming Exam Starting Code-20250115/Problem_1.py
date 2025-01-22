import numpy as np


def main():
    test_problem_1()


def test_problem_1():
    ex_count = 1
    ex_total = 0.9353
    act_count, act_total = problem_1(1, 7, 2)
    print("Test 1:")
    print("-------")
    print("Expected:", ex_count, ex_total)
    print("Actual:", act_count, act_total)

    ex_count = 3
    ex_total = 1.837
    act_count, act_total = problem_1(0, 2 * np.pi, np.pi / 4)
    print("\nTest 2:")
    print("-------")
    print("Expected:", ex_count, ex_total)
    print("Actual:", act_count, act_total)

    ex_count = 12
    ex_total = 0.4365
    act_count, act_total = problem_1(3, 12, 0.5)
    print("\nTest 3:")
    print("-------")
    print("Expected:", ex_count, ex_total)
    print("Actual:", act_count, act_total)


def problem_1(m, n, p):
    """
    This function has the input arguments m, n, and p. The function will
    determine values of sin(x) where x ranges from m to n using an increment
    of p. It will then determine how many times sin(x) < 0 and return the
    value in count. For instances where sin(x) > 0.5, the program will sum
    those values and return the value in total.

    The program must return count and total in that order.

    Example:

        For m = 1, n = 7, and p = 2:

        sin(1) = 0.84147    sin(1) > 0.5    sin(1)/1 = 0.84147
        sin(3) = 0.14112
        sin(5) = -0.95892   sin(5) < 0
        sin(7) = 0.65699    sin(7) > 0.5    sin(7)/7 = 0.09386

    For this example:
        count = 1
        total = 0.84147 + 0.09386 = 0.93533


    Program Notes

    - You may assume n > m and p > 0.
    - You MUST use a for loop.


    Parameters
    ----------
    m : float
        The lower limit on the range
    n : float
        The upper limit on the range
    p : float
        The step to use between m and n

    Returns
    -------
    count : int
        The number of instances that sin(x) < 0.
    total : float
        The total sum of sin(x)/x when sin(x) > 0.5.

    """
    tot = 0.0
    count = 0
    val = np.arange(m, n + p, p)

    for x in range(len(val)):

        if np.sin(val[x]) < -(10**-10):
            count += 1

        elif np.sin(val[x]) > 0.5:
            tot = tot + (np.sin(val[x]) / (x + 1))

    return count, tot

    # for x in range(m, n + 1, p):
    #     if np.sin(x) > 0.5:
    #         tot += np.sin(x) / x
    #
    #     elif np.sin(x) < 0:
    #         count += 1
    #
    # return count, tot


main()
