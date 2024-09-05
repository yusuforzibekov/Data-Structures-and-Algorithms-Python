"""Sample tests for 'tasks.linear_combination' module."""
import numpy as np

import pytest

from tasks.linear_combination import linear_combination


def test_linear_combination():
    """Sample tests for linear_combination function."""
    assert np.allclose(linear_combination(matrix=[[1, 0], [0, 1]], weights=[2, 3]), [2, 3])
    
    assert np.allclose(linear_combination(matrix=[[1, 1, 1], [1, 2, 3]], weights=[1, 2, 1]), [4, 8])

    with pytest.raises(ValueError):
        _ = linear_combination(matrix=[[1, 1], [1, 1]], weights=[2])

    with pytest.raises(ValueError):
        _ = linear_combination(matrix=[[1, 1], [1, 1]], weights=[2, 3, 4])
    