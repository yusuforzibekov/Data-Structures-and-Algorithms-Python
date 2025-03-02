"""Template for programming assignment: reshape the matrix"""
from typing import List


def reshape_matrix(matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
    """Returns the reshaped version of the input matrix, i.e.
    the matrix written in other dimensions while preserving the
    row-traversing order of its elements.

    Examples:
        reshape_matrix([[1, 2], [3, 4]], 1, 4) -> [[1, 2, 3, 4]]
        reshape_matrix([[1, 2], [3, 4], [5, 6]], 2, 3) -> [[1, 2, 3], [4, 5, 6]]
        reshape_matrix([[1, 2], [3, 4]], 2, 4) -> [[1, 2], [3, 4]]

    Args:
        matrix: list of lists of ints, input matrix
        r: int, number of rows in the output matrix
        c: int, number of columns in the output matrix
    Returns:
        list of lists of ints, the reshaped matrix
    """
    if not matrix or len(matrix) * len(matrix[0]) != r * c:
        return matrix

    # Flatten matrix
    flat = sum(matrix, [])

    # Create new matrix
    return [flat[i : i + c] for i in range(0, len(flat), c)]
