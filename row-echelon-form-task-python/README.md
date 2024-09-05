# Row-echelon form and equivalent operations

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:

* Row echelon and reduced row-echelon forms of a matrix
* Equivalent matrix operations
* The rank of a matrix

## Overview

The coding exercises cover the following practical problems:
* Checking whether a given matrix is in row-echelon form
* Converting a given matrix into reduced row-echelon form
* Finding a rank of a given square matrix


## Coding exercises

### Exercise 1: Check whether a given matrix is in row-echelon form

Your task is to implement the following function to verify whether a matrix is in row-echelon form:

```python
def check_row_echelon_form(matrix: List[List[float]]) -> bool:
    """Checks whether a given matrix is in row-echelon form.

    NOTE: To avoid issues with precision, use EPS=1e-8 to detect zeros:
        |x| < EPS => We assume that x is zero.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        Bool, whether a given matrix is in row-echelon form.
    """
    pass
```

**Example 1:**
```math
matrix = \left(\begin{array}{} 
1 & 2\\
3 & 4
\end{array}\right)
```

Expected output: false.

**Example 2:**
```math
matrix = \left(\begin{array}{} 
1 & 1 & 2 & 1\\
0 & 1 & 3 & 12\\
0 & 0 & 1 & 8\\
0 & 0 & 0 & 1
\end{array}\right)
```

Expected output: true.

**Example 3:**
```math
matrix = \left(\begin{array}{} 
1 & 1 & 2 & 1 & 1\\
0 & 2 & 3 & 12 & 3\\
0 & 0 & 0 & 8 & 4\\
0 & 0 & 0 & 0 & 2
\end{array}\right)
```

Expected output: true.

<br/>

Please use the template `tasks/row_echelon:check_row_echelon_form` for the implementation.


### Exercise 2: Convert a given matrix into reduced row-echelon form

Your task is to implement the following function to convert matrices into reduced row-echelon form:

```python
def convert_into_rref(matrix: List[List[float]]) -> List[List[float]]:
    """Returns the reduced row-echelon form of a given matrix.

    NOTE: Reduced row-echelon form of a matrix is unique and does not depend on the algorithm used to compute it.

    NOTE: You are not allowed to permute rows or columns.

    NOTE: To avoid issues with precision, use EPS=1e-8 to detect zeros:
        |x| < EPS => We assume that x is zero.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        List[List[float]], the reduced row-echelon form of a given matrix.
    """
    pass
```

**Example 1:**
```math
matrix = \left(\begin{array}{} 
1 & 5 & 1\\
2 & 11 & 5
\end{array}\right)

result = \left(\begin{array}{} 
1 & 0 & -14\\
0 & 1 & 3
\end{array}\right)
```

**Example 2:**
```math
matrix = \left(\begin{array}{} 
1 & 5 & 6\\
2 & 4 & 7\\
3 & 5 & 9
\end{array}\right)

result = \left(\begin{array}{} 
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{array}\right)
```

**Example 3:**
```math
matrix = \left(\begin{array}{} 
1 & 5 & 6\\
5 & 0 & 4\\
1 & 2 & 5\\
4 & 2 & 4
\end{array}\right)

result = \left(\begin{array}{} 
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
0 & 0 & 0
\end{array}\right)
```

<br/>

Please use the template `tasks/row_echelon:convert_into_rref` for the implementation.

### Exercise 3: Find the rank of a given square matrix

Your task is to implement the following function to find the ranks of square matrices:

```python
def get_rank_of_square_matrix(matrix: List[List[float]]) -> int:
    """Returns the rank of a given square matrix.

    NOTE: You may use the 'convert_into_rref' function here.

    NOTE: To avoid issues with precision, use EPS=1e-8 to detect zeros:
        |x| < EPS => We assume that x is zero.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        int, the rank of a given square matrix.
    """
    pass
```

**Example 1:**
```math
matrix = \left(\begin{array}{} 
1 & 5 & 6\\
2 & 4 & 7\\
3 & 5 & 9
\end{array}\right)
```

Expected output: 3

**Example 2:**
```math
matrix = \left(\begin{array}{} 
1 & 2 & 4\\
2 & 4 & 3\\
2 & 4 & 2
\end{array}\right)
```

Expected output: 2

**Example 3:**
```math
matrix = \left(\begin{array}{} 
1 & 2 & 4 & 0\\
0 & 0 & 0 & 0\\
2 & 4 & 2 & 0\\
5 & 2 & 1 & 0
\end{array}\right)
```

Expected output: 3

<br/>

Please use the template `tasks/row_echelon:get_rank_of_square_matrix` for the implementation.
