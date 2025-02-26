# Commonly Used Libaries
- numpy
- scipy
    - scipy.integrate
    - scipy.optimize
- matplotlib.pyplot
- pandas

# Initial Value Problems (IVP)
Import Library

`from scipy.integrate import solve_ivp`

Syntax

`sol = solve_ivp(function, t_span, y_0, t_eval = t_range, args = (1, ))`

where

    function: function of the DE to be solved. Must be in the form independent then dependent
    t_span: list or tuple for the initial and final vlaues of t (eg. [t_start, t_stop])
    y_0: a list or tuple containing the initial conditions
    t_eval: range which the DE will be solve acrossed (if not specified, results can be off)
        t_range: typically and np.linspace across t_span
    args: additional input arguments needed in the DE
### Additional Help
See Day 15 for additional help

# Second Order IVPs
Similar to normal first-order IVP
See Handout and Day 16 python files

# Boundary Value Problems
Import Library

`from scipy.integrate import solve_bvp`

Syntax

`sol = solve_bvp(f, bc, x, y)`

where

    f: the function containing the system of n equations to solve
    bc: function of the residuals of the BC
    x: a vector of m x-values to evaluate the system of equations
    y: an initial *n x m* array of initial guesses

### Aditional Help
Seey BVP handout and Day 17 work

# Numerical Integration
Import Library

`from scipy import integrate`

or 

`from scipy.integrate import [quad | trapezoid | simpson]`

## Function Integration
Syntax

`I, err = quad(fun, a, b, args = (1, ))`

where

    I: Result of integration
    err: estimated error of result
    fun: function to be integrated
    a, b: lower and upper limits of integration
    args: additional inputs for the function

## Data Integration
Syntax
trapezoid

`I = trapezoid(y, x)`

where 

    I: Result of integration
    y: dependent variable of data set
    x: independent variable of data set

simpson

`I = simpson(y, x = , dx =)

where

    I: Result of integration
    y: dependent variable of the data set
    x: indpendent variable, must provide a vector of x values
    dx (optional): specificy a spacing between data points
        x = None

### Additiona Help
Day 18 for data Integration