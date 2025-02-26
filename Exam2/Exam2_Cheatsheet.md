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

    function: function of the DE to be solved. Must be in the form independent then dependent
    t_span: list or tuple for the initial and final vlaues of t (eg. [t_start, t_stop])
    y_0: a list or tuple containing the initial conditions
    t_eval: range which the DE will be solve acrossed (if not specified, results can be off)
        t_range: typically and np.linspace across t_span
    args: additional input arguments needed in the DE
### Additional Help
See Day 15 for additional help








