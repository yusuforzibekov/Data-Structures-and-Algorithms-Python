"""Sample tests for 'tasks.plu' module."""
import copy
from tasks.plu import get_inverse_matrix, plu_decomposition, Matrix


def assert_matrices_equal(a: Matrix, b: Matrix):
    assert len(a) == len(b)
    assert all([len(a_line) == len(b_line) for a_line, b_line in zip(a, b)])

    for row in range(len(a)):
        for col in range(len(b)):
            assert abs(a[row][col] - b[row][col]) < 1e-8


def test_plu_decomposition_sample():
    """Sample tests for plu_decomposition function."""
    p, l, u = plu_decomposition(
        matrix=[
            [1, 2, 1],
            [1, 2, 2],
            [2, 1, 1],
        ]
    )
    # Expected shapes
    assert len(p) == 3 and all([len(p_line) == 3 for p_line in p])
    assert len(l) == 3 and all([len(l_line) == 3 for l_line in l])
    assert len(u) == 3 and all([len(u_line) == 3 for u_line in u])
    # L - lower triangular
    for row in range(3):
        for col in range(row + 1, 3):
            assert abs(l[row][col]) < 1e-8
    # U - upper triangular
    for row in range(3):
        for col in range(row - 1):
            assert abs(u[row][col]) < 1e-8
    # P - permutation matrix
    assert all([sum([p[row][col] for col in range(3)]) == 1 for row in range(3)])
    assert all([sum([p[row][col] for row in range(3)]) == 1 for col in range(3)])

    assert_matrices_equal(
        p,
        [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
        ]
    )
    assert_matrices_equal(
        l,
        [
            [1, 0, 0],
            [2, 1, 0],
            [1, 0, 1],
        ]
    )
    assert_matrices_equal(
        u,
        [
            [1, 2, 1],
            [0, -3, -1],
            [0, 0, 1],
        ]
    )


def test_get_inverse_matrix_sample():
    """Sample tests for get_inverse_matrix function."""
    a = [
        [1, 2, 1],
        [1, 2, 2],
        [2, 1, 1],
    ]
    a_inv = get_inverse_matrix(
        matrix=copy.deepcopy(a)
    )
    # Expected shape
    assert len(a_inv) == 3 and all([len(_) == 3 for _ in a_inv])
    
    identity = [
        [
            sum([a[i][k] * a_inv[k][j] for k in range(3)])
            for j in range(3)
        ]
        for i in range(3)
    ]

    assert_matrices_equal(
        identity,
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
