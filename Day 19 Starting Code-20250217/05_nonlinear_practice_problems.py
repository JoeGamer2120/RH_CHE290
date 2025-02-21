# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:30:11 2025

@author: schlabjb
"""

from scipy.optimize import fsolve
import numpy as np

def f(c, W, Q, K, V):
    return W - Q*c - K*V*np.sqrt(c)

def f2(x):
    f1 = 9*x[0]**2 + 36*x[1]**2 + 4* x[2]**2 - 36
    f2 = x[0]**2 - 2*x[1]**2 - 20*x[2]
    f3 = x[0]**3 + 2*x[1]**2 + 16*x[2]**2 - 16*x[0]
    return f1, f2, f3

c = fsolve(f, 4, args=(2*10**6, 2*10**5, 0.33, 2*10**6))
print(c, f(c, 2*10**6, 2*10**5, 0.33, 2*10**6))

x = fsolve(f2, [0.1, 0.1, 0.1])
print(x, f2(x))