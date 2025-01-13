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
    practice_problem_1()
    # practice_problem_2()

def practice_problem_1():
    """
    TODO 1: Complete this function to create the figue described for
            practice problem 1 in the handout.
    """
    t = np.arange(0, 50.1, 0.5)
    Cao = 2 # M
    k1 = 0.5 # min^-1
    k2 = 0.08 # min^-1
    
    Cb = (k1 * t * Cao) / (1 + k1*t + k2*t)
    
    fig, ax = plt.subplots()
    
    ax.set_xlabel('Residence time (min)')
    ax.set_ylabel('Product Concentration (M)')
    ax.set_xlim(-2, 52)
    ax.set_ylim(0, 1.75)
    ax.tick_params(direction = 'in')
    ax.plot(t, Cb, color = 'black', lw = '4', ls = ':')
    
    plt.show()



def practice_problem_2():
    """
    TODO 2: Complete this function to create the figue described for
            practice problem 2 in the handout.
    """

    
main()