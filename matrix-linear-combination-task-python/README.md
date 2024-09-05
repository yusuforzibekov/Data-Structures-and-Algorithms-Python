# Linear combination

## Purpose

The following coding exercise is designed to test your knowledge of the following concepts:
* Linear combination of vectors

## Overview

The coding exercise covers the following practical problem:
* Computing a linear combination of columns for a given matrix

## Coding exercises

### Exercise 1: Compute a linear combination

Your task is to implement the following function to return the linear combination of columns for a given matrix:

```python
def linear_combination(matrix: List[List[float]], weights: List[float]) -> List[float]:
    """Returns a linear combination of columns for a given matrix using a list of corresponding weights.

    Args:
        matrix: List[List[float]], a given numeric matrix.
        weights: List[float], a list of weights that correspond to the columns of the matrix

    Returns:
        The resulting linear combination.

    Raises:
        ValueError: If the given matrix and weights are not compatible (dimensionalities don't match).
    """
    pass
```

**Example 1:**

```math
matrix=\begin{pmatrix}
   3 & 4 \\
   2 & 1
\end{pmatrix}

weights=\begin{pmatrix}
   2 \\
   3 
\end{pmatrix}
```


Expected output: 

```math
2\times\begin{pmatrix}
   3 \\
   2 
\end{pmatrix}
+3\times
\begin{pmatrix}
   4 \\
   1 
\end{pmatrix}=
\begin{pmatrix}
   6 + 12\\
   4 + 3
\end{pmatrix}=
\begin{pmatrix}
   18\\
   7
\end{pmatrix}
```

**Example 2:**

```math
matrix = \begin{pmatrix}
   1 & 0 \\
   0 & 1
\end{pmatrix}

weights = \begin{pmatrix}
   2 \\
   3 
\end{pmatrix}
```

Expected output: 

```math
\begin{pmatrix}
   2\\
   3
\end{pmatrix}
```

**Example 3:**

```math
matrix = \begin{pmatrix}
   1 & 0 \\
   0 & 1
\end{pmatrix}

weights = \begin{pmatrix}
   2
\end{pmatrix}
```

Expected output: The `ValueError` exception is raised because the matrix and the weights are not compatible.

Please use the template `tasks/linear_combination:linear_combination` for the implementation.
