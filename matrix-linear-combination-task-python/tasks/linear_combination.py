from typing import List


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
    num_rows = len(matrix)
    if num_rows == 0:
        return []

    num_cols = len(matrix[0])

    if num_cols != len(weights):
        raise ValueError("The number of weights must match the number of columns in the matrix.")

    # Initialize the result vector with zeros
    result = [0.0] * num_rows

    # Compute the linear combination
    for col_index in range(num_cols):
        weight = weights[col_index]
        for row_index in range(num_rows):
            result[row_index] += matrix[row_index][col_index] * weight

    return result
