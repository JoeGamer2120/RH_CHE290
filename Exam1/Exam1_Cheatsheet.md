# Vectors
## Creating Vectors
Vectors with Predefined Elements

`np.array([list of numbers separated by commas])`


Vectors along a set range

`np.arange(start, stop, increment)`

> [!NOTE]
> `stop` is **non-inclusive**

Vectors with *equally* seperated elements 

`np.linspace(start, stop, number of points)`

> [!NOTE]
> `stop` in **inclusive**

 Zero & One Vectors

`np.zeros(number of points)`

`np.ones(number of points)`

# Matrices
## Creating Matricies
### Method 1

`np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )`

*extra spaces are included for viewing*
### Method 2 

`a = np.arange(1, 4)`

`b = np.arrange(4, 7)`

`c = np.arrange(7, 10)`

`M = np.array([a, b, c])`

### Method 3

`variable_name.reshape(#rows, #columns)`

Example

`a = np.arange(1, 10)
M = a.reshape(3, 3)`

### Special
Zero Matrix

`M = np.zeros((3,4))`

Identity Matrix

`np.identity(size)`

# Indexing
Grab the specific element 

`my_vector[2]`  *retrieves the 3rd element of vector*

`my_matrix[2]`  *retrieves all values in 3rd row*

`my_matrix[2, 1]`   *retrieves 2nd value in 3rd row*

# Data Types
int     integer
float   floating point number
complex complex number
str     string; collection of character
bool    Boolean; logical operation
list    list; mutable
tuple   tuple; immutable

# Print Formatting
Syntax: `.format()`

Examples

`print("The price is {:.2f} dollars." .format(45))`

## Formatting Types
:e  Scientific format   Ex: {:.2f}
:f  Fix point number format     Ex: {:e}
:%  Percentage format   Ex: {:.0%}

