# Basic matrix operations

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:

* Matrix transposition
* Matrix addition
* Matrix multiplication

## Overview

The coding exercises cover the following practical problems:
* Transposition of a given matrix
* Calculating the result of given matrices addition
* Calculating the result of given matrices multiplication

## Coding exercises


### Exercise 1: Transpose a given matrix

Your task is to implement the following function to transpose matrices:

```python
def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Returns a view of a given matrix with axes transposed.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        The transposed matrix.
    """
    pass
```

**Example 1:**
```math
matrix = \left(\begin{array}{} 
1 & 2\\
3 & 4
\end{array}\right)

\\
transposed\_matrix = \left(\begin{array}{} 
1 & 3\\
2 & 4
\end{array}\right)
```

**Example 2:**
```math
matrix = \left(\begin{array}{} 
1 & 2 & 3\\
4 & 5 & 6
\end{array}\right)

\\
transposed\_matrix = \left(\begin{array}{} 
1 & 4\\
2 & 5\\
3 & 6
\end{array}\right)
```

<br/>

Please use the template `tasks/matrix_operations:transpose` for the implementation.

### Exercise 2: Add two given matrices

Your task is to implement the following function to add two given matrices:

```python
def add_matrices(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    """Returns a sum of two given matrices.

    Args:
        matrix_a: List[List[float]], the first numeric matrix.
        matrix_b: List[List[float]], the second numeric matrix.

    Returns:
        The sum of two given matrices.

    Raises:
        ValueError: if the matrices are not compatible (dimensions differ in size).
    """
    pass
```
 
**Example 1:**
```math
\left(\begin{array}{} 
1 & 2\\
3 & 4
\end{array}\right)+\left(\begin{array}{} 
1 & 1\\
1 & 2
\end{array}\right)=\left(\begin{array}{} 
2 & 3\\
4 & 6
\end{array}\right)
```

**Example 2:**
```math
\left(\begin{array}{} 
1 & 2 & 3\\
3 & 4 & 1
\end{array}\right)+\left(\begin{array}{} 
1 & 1 & 0\\
1 & 1 & -10
\end{array}\right)=\left(\begin{array}{} 
2 & 3 & 3\\
4 & 5 & -9
\end{array}\right)
```

<br/>

Please use the template `tasks/matrix_operations:add_matrices` for the implementation.

### Exercise 3: Multiply two given matrices

Your task is to implement the following function to multiply two given matrices:

```python
def multiply_matrices(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    """Returns the product (result of multiplication) of two given matrices.

    Args:
        matrix_a: List[List[float]], the first numeric matrix.
        matrix_b: List[List[float]], the second numeric matrix.

    Returns:
        The product of two given matrices.

    Raises:
        ValueError: if the matrices are not compatible.
    """
    pass
```
 
**Example 1:**
```math
\left(\begin{array}{} 
1 & 2\\
3 & 4
\end{array}\right)*\left(\begin{array}{} 
1 & 1\\
1 & 2
\end{array}\right)=\left(\begin{array}{} 
3 & 5\\
7 & 11
\end{array}\right)
```

**Example 2:**
```math
\left(\begin{array}{} 
1 & 2 & 3\\
3 & 4 & 1
\end{array}\right)*\left(\begin{array}{} 
1 & 2\\
2 & 1\\
1 & 1
\end{array}\right)=\left(\begin{array}{} 
8 & 7\\
12 & 11
\end{array}\right)
```

<br/>

Please use the template `tasks/matrix_operations:multiply_matrices` for the implementation.
