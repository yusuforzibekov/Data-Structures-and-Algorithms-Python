"""Sample tests for 'tasks.gauss' module."""
from tasks.gauss import find_sle_solution


def test_find_sle_solution_sample():
    """Sample tests for find_sle_solution function."""
    x = find_sle_solution(
        A=[
            [1, 2, 3],
            [4, 5, 2],
            [2, 5, 1],
        ],
        b=[14, 20, 15]
    )
    assert all(abs(x_exp - x_res) < 1e-8 for x_res, x_exp in zip(x, [1, 2, 3]))

    x = find_sle_solution(
        A=[
            [1, 2, -3],
            [4, -5, 2],
            [-2, 5, 1],
        ],
        b=[-4, 0, 11]
    )
    assert all(abs(x_exp - x_res) < 1e-8 for x_res, x_exp in zip(x, [1, 2, 3]))

    x = find_sle_solution(
        A=[
            [1, -2, -3],
            [4, -5, -2],
            [-2, -5, 1],
        ],
        b=[-12, -12, -9]
    )
    assert all(abs(x_exp - x_res) < 1e-8 for x_res, x_exp in zip(x, [1, 2, 3]))
