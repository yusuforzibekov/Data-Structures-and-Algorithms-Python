from typing import List, Tuple

EPS = 1e-8
Matrix = List[List[float]]


def plu_decomposition(matrix: Matrix) -> Tuple[Matrix, Matrix, Matrix]:
    n = len(matrix)
    # Initialize P as identity matrix
    P = [[float(i == j) for i in range(n)] for j in range(n)]
    L = [[0.0] * n for _ in range(n)]
    U = [row[:] for row in matrix]

    for i in range(n):
        # If pivot is zero, find a row below that has a non-zero pivot and swap
        if abs(U[i][i]) < EPS:
            pivot_row = -1
            for r in range(i + 1, n):
                if abs(U[r][i]) > EPS:
                    pivot_row = r
                    break
            if pivot_row == -1:
                raise ValueError("Matrix is singular")
            # Swap rows in U
            U[i], U[pivot_row] = U[pivot_row], U[i]
            # Swap rows in P
            P[i], P[pivot_row] = P[pivot_row], P[i]
            # Swap rows in L up to column i
            for j in range(i):
                L[i][j], L[pivot_row][j] = L[pivot_row][j], L[i][j]

        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    # Set diagonal of L to 1
    for i in range(n):
        L[i][i] = 1.0

    return P, L, U


def get_inverse_matrix(matrix: Matrix) -> Matrix:
    """Returns the inverse for a given matrix.

    NOTE: Use the `plu_decomposition` function from the previous coding exercise.
    NOTE: It is guaranteed that a given matrix is square.
    NOTE: It is guaranteed that the PLU decomposition exists.
    NOTE: To avoid issues with precision, use EPS=1e-8 to detect zeros:
        |x| < EPS => We assume that x is zero.

    Args:
        matrix: Matrix, a given square matrix for which we want to get the inverse matrix.

    Returns:
        Matrix, the inverse matrix.
    """
    n = len(matrix)
    P, L, U = plu_decomposition(matrix)

    # Helper function to solve LY = B
    def forward_substitution(L, B):
        Y = [0.0] * n
        for i in range(n):
            Y[i] = B[i] - sum(L[i][j] * Y[j] for j in range(i))
        return Y

    # Helper function to solve UX = Y
    def backward_substitution(U, Y):
        X = [0.0] * n
        for i in reversed(range(n)):
            X[i] = (Y[i] - sum(U[i][j] * X[j]
                    for j in range(i + 1, n))) / U[i][i]
        return X

    inverse_matrix = []
    for i in range(n):
        e = [P[j][i] for j in range(n)]  # P^T * e_i
        Y = forward_substitution(L, e)
        X = backward_substitution(U, Y)
        inverse_matrix.append(X)

    # Transpose the result to get the correct format
    inverse_matrix = list(map(list, zip(*inverse_matrix)))
    return inverse_matrix
