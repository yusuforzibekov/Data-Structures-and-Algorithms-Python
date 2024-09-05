from typing import List

EPS = 1e-8

def find_sle_solution(A: List[List[float]], b: List[float]) -> List[float]:
    """Returns the solution of a given system of linear equations (Ax=b).

    NOTE: It is guaranteed that the given matrix A is square.
    NOTE: It is guaranteed that only one solution exists.
    NOTE: The Gauss elimination should be extended with partial pivoting, as this helps to reduce rounding errors; you are less likely to add/subtract with a very small number (or a very large number).
    NOTE: To avoid issues with precision, use EPS=1e-8 to detect zeros:
        |x| < EPS => we assume that x is zero.

    Args:
        A: List[List[float]], a matrix with coefficients (a11 * x1 + ... + a1k * xk) of a given system (the left part).
        b: List[float], a list with values of a given system's equations (the right part, b1 = a11 * x1 + ... + a1k * xk).

    Returns:
        List[float], the solution of a given system of linear equations.
    """
    n = len(A)

    # Forward Elimination with Partial Pivoting
    for i in range(n):
        # Partial Pivoting: Find the row with the maximum element in column i
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Swap the maximum row with the current row
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            if abs(A[i][i]) < EPS:
                raise ValueError("Matrix is singular or nearly singular")
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # Back Substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        if abs(A[i][i]) < EPS:
            raise ValueError("Matrix is singular or nearly singular")
        x[i] = b[i] / A[i][i]
        for k in range(i-1, -1, -1):
            b[k] -= A[k][i] * x[i]

    return x
