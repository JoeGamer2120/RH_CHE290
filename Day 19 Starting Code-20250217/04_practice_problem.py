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



