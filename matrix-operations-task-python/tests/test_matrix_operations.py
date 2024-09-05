"""Sample tests for 'tasks.matrix_operations' module."""

import pytest

from tasks.matrix_operations import add_matrices, multiply_matrices, transpose


def test_transpose_sample():
    """Sample tests for transpose function."""
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    

def test_add_matrices_sample():
    """Sample tests for add_matrices function."""
    assert add_matrices(
        [[1, 2], 
         [3, 4]],
        [[1, 1],
         [1, 2]]
    ) == [[2, 3],
          [4, 6]]
    assert add_matrices(
        [[1, 2, 3], 
         [3, 4, 1]],
        [[1, 1, 0],
         [1, 1, -10]]
    ) == [[2, 3, 3],
          [4, 5, -9]]
    
    with pytest.raises(ValueError):
        _ = add_matrices([[1, 2]], [[1, 2], [1, 4]])
    with pytest.raises(ValueError):
        _ = add_matrices([[1, 2, 3]], [[1, 2]])


def test_multiply_matrices_sample():
    """Sample tests for multiply_matrices function."""
    assert multiply_matrices(
        [[1, 2], 
         [3, 4]],
        [[1, 1],
         [1, 2]]
    ) == [[3, 5],
          [7, 11]]
    assert multiply_matrices(
        [[1, 2, 3], 
         [3, 4, 1]],
        [[1, 2],
         [2, 1],
         [1, 1]]
    ) == [[8, 7],
          [12, 11]]
    
    with pytest.raises(ValueError):
        _ = multiply_matrices([[1, 2]], [[1, 2]])
    with pytest.raises(ValueError):
        _ = multiply_matrices([[1, 2, 3]], [[1, 2, 3, 4], [1, 2, 3, 4]])
