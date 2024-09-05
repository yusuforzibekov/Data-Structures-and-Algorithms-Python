from typing import List

EPS = 1e-8


def check_row_echelon_form(matrix: List[List[float]]) -> bool:
    """Checks whether a given matrix is in row-echelon form.

    NOTE: To avoid issues with precision, use EPS=1e-8 to detect zeros:
        |x| < EPS => We assume that x is zero.

    Args:
        matrix: List[List[float]], a given numeric matrix.

    Returns:
        Bool, whether a given matrix is in row-echelon form.
    """
    if not matrix:
        return False

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    prev_pivot_col = -1

    for i in range(num_rows):
        pivot_found = False
        for j in range(num_cols):
            if abs(matrix[i][j]) >= EPS:
                if j <= prev_pivot_col:
                    return False
                pivot_found = True
                prev_pivot_col = j
                break

        if not pivot_found:
            # This row is all zeros. Ensure all subsequent rows are also all zeros.
            continue

        # Check below the pivot element
        for k in range(i + 1, num_rows):
            if prev_pivot_col < num_cols and abs(matrix[k][prev_pivot_col]) >= EPS:
                return False

    return True

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
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    lead = 0

    for r in range(num_rows):
        if lead >= num_cols:
            return matrix
        i = r
        while abs(matrix[i][lead]) < EPS:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if num_cols == lead:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]
        if abs(matrix[r][lead]) > EPS:
            matrix[r] = [mrx / matrix[r][lead] for mrx in matrix[r]]
        for i in range(num_rows):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv*rv for rv,
                             iv in zip(matrix[r], matrix[i])]
        lead += 1

    return matrix


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
    rref_matrix = convert_into_rref(matrix)
    rank = 0
    for row in rref_matrix:
        if any(abs(entry) > EPS for entry in row):
            rank += 1
    return rank
