"""Templates for programming assignments: basic matrix operations."""

from typing import List


def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Returns a view of a given matrix with axes transposed.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]


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
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices dimensions do not match.")

    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]


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
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Matrices dimensions are not compatible for multiplication.")

    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result
