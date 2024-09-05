"""Sample tests for 'tasks.row_echelon' module."""
from tasks.row_echelon import check_row_echelon_form, convert_into_rref, get_rank_of_square_matrix


def test_check_row_echelon_form_sample():
    """Sample tests for check_row_echelon_form function."""
    assert not check_row_echelon_form(
        [[1, 2],
         [3, 4]]
    )

    assert check_row_echelon_form(
        [[1, 1, 2, 1],
         [0, 1, 3, 12],
         [0, 0, 1, 8],
         [0, 0, 0, 1]]
    )

    assert check_row_echelon_form(
        [[1, 1, 2, 1, 1],
         [0, 2, 3, 12, 3],
         [0, 0, 0, 8, 4],
         [0, 0, 0, 0, 2]]
    )


def test_convert_into_rref_sample():
    """Sample tests for convert_into_rref function."""
    assert convert_into_rref(
        [
            [1, 5, 1],
            [2, 11, 5]
        ]
    ) == [
        [1, 0, -14],
        [0, 1, 3]
    ]

    assert convert_into_rref(
        [
            [1, 5, 6],
            [2, 4, 7],
            [3, 5, 9]
        ]
    ) == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    assert convert_into_rref(
        [
            [1, 5, 6],
            [5, 0, 4],
            [1, 2, 5],
            [4, 2, 4]
        ]
    ) == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]
    ]


def test_get_rank_of_square_matrix_sample():
    """Sample tests for get_rank_of_square_matrix function."""
    assert get_rank_of_square_matrix(
        [
            [1, 5, 6],
            [2, 4, 7],
            [3, 5, 9]
        ]
    ) == 3

    assert get_rank_of_square_matrix(
        [
            [1, 2, 4],
            [2, 4, 3],
            [2, 4, 2]
        ]
    ) == 2

    assert get_rank_of_square_matrix(
        [
            [1, 2, 4, 0],
            [0, 0, 0, 0],
            [2, 4, 2, 0],
            [5, 2, 1, 0]
        ]
    ) == 3
