"""
The relationship between the pressure (P) and volume (V) of the air in a 
cylinder during the upstroke of a piston in an air compressor can be expressed 
as:
    
    P*V^k = C

where k and C are constants. The data for a compression test can be found in
the Excel sheet provided.

Use the least squares function to fit the following function:
    
    P = CV^-k


Once you have the regression parameters, create a plot of P = f(V) that 
compares your regressed parameters to the data. Because of the limited data
points, a plot of the model will look segemented. Therefore, to create a plot
of the model, create a vector of V that ranges from the lowest to the highest
value in the data using a step size of 0.1.
"""
import numpy as np
from scipy.optimize import least_squares
import pandas as pd
import matplotlib.pyplot as plt

### Initial Guesses (given in class)
k0 = 1.5
C0 = 3 * 10**5

def f(c, P, V):
    """
    Definition of the residual for the non linear function above (P = CV^-k)
    where k and C are constants. 
       
    Parameters
    ----------
    c: array
        a list/tuple/np.array of the constatnts k and C
    P : float
        Pressure
    V: float
        Volume
           
    Returns
    -------
    float
        the residual
    """
    return c[0] * V**-c[1] - P

### Import Excel Data
data = pd.read_excel("P-V Data.xlsx")
P = data["P"]
V = data['V']

### Least Squares Regression
result = least_squares(f, (C0, k0), args = (P, V))
con = result.x

### Best Fit Curve
Vmodel = np.arange(17.4, 48.3, 0.1)
Pmodel = con[0] * Vmodel**-con[1]

### Create Figure
fig, ax = plt.subplots()

ax.scatter(V, P, label='data')
ax.plot(Vmodel, Pmodel, label = 'model')
ax.tick_params(direction = 'in')
ax.set_xlabel('Volume')
ax.set_ylabel('Pressure')
ax.legend()
plt.show()


































