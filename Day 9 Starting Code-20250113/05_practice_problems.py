"""
Complete the practice problems based on the descriptions provided in the
separate pdf.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Uncomment the function calls below to test your code.
    """
    # practice_problem_1()
    practice_problem_2()


def practice_problem_1():
    """
    TODO 1: Complete this function to create the figue described for
            practice problem 1 in the handout.
    """
    t = np.arange(0, 50.1, 0.5)
    Cao = 2  # M
    k1 = 0.5  # min^-1
    k2 = 0.08  # min^-1

    Cb = (k1 * t * Cao) / (1 + k1 * t + k2 * t)

    fig, ax = plt.subplots()

    ax.set_xlabel("Residence time (min)")
    ax.set_ylabel("Product Concentration (M)")
    ax.set_xlim(-2, 52)
    ax.set_ylim(0, 1.75)
    ax.tick_params(direction="in")
    ax.plot(t, Cb, color="black", lw="4", ls=":")

    plt.show()


def practice_problem_2():
    """
    TODO 2: Complete this function to create the figue described for
            practice problem 2 in the handout.
    """
    # Create Dataset for Eqn 1
    x1 = np.arange(-5, 5.01, 0.01)
    y1 = (1 / 3) * (5 - x1**2)

    # Create Dataset for Eqn 2
    y2 = np.arange(-4, 4.01, 0.01)
    x2 = 2 - y2**2

    # Initialize plot
    fig, ax = plt.subplots()

    ax.plot(x1, y1, color="blue", lw="2", ls="-")
    ax.plot(x2, y2, color="red", lw="2", ls="--")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-5, 5)
    ax.tick_params(direction="in")

    plt.show()


main()
