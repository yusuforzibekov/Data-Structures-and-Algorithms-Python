"""Sample tests for programming assignment:
Visualize a Gem Puzzle board"""
from tasks.visualization import format_board_row, format_board


def test_format_board_row():
    # Sample tests
    assert format_board_row([1, 11, None, 9]) == '|  1 | 11 |    |  9 |'
    assert format_board_row([1, 2, 3, 4]) == '|  1 |  2 |  3 |  4 |'


def test_format_board():
    # Sample test 1
    board = [
        [2, 1, 7, 4],
        [10, 13, 3, 12],
        [9, 5, None, 14],
        [8, 6, 15, 11],
    ]
    board_string = '\n'.join([
        ' ------------------- ',
        '|  2 |  1 |  7 |  4 |',
        ' ------------------- ',
        '| 10 | 13 |  3 | 12 |',
        ' ------------------- ',
        '|  9 |  5 |    | 14 |',
        ' ------------------- ',
        '|  8 |  6 | 15 | 11 |',
        ' ------------------- ',
    ])
    assert format_board(board) == board_string

    # Sample test 2
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, None],
    ]
    board_string = '\n'.join([
        ' ------------------- ',
        '|  1 |  2 |  3 |  4 |',
        ' ------------------- ',
        '|  5 |  6 |  7 |  8 |',
        ' ------------------- ',
        '|  9 | 10 | 11 | 12 |',
        ' ------------------- ',
        '| 13 | 14 | 15 |    |',
        ' ------------------- ',
    ])
    assert format_board(board) == board_string
