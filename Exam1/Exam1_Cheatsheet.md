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
> stop in **inclusive**

 Zero & One Vectors
`np.zeros(number of points)
 np.ones(number of points)`

# Matrices
## Creating Matricies
### Method 1
`np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )`
*extra spaces are included for viewing*
### Method 2 
`a = np.arange(1, 4)
b = np.arrange(4, 7)
c = np.arrange(7, 10)`
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


