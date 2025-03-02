"""Sample tests for programming assignment:
Generate a Gem Puzzle board"""
from tasks.board import generate_board


def test_generate_board_from_tiles():
    # Sample test 1
    expected_board = [
        [2, 1, 7, 4],
        [10, 13, None, 12],
        [9, 5, 3, 14],
        [8, 6, 15, 11]
    ]
    assert generate_board(
        size=4,
        tiles=[2, 1, 7, 4, 10, 13, None, 12, 9, 5, 3, 14, 8, 6, 15, 11]
    ) == expected_board

    # Sample test 2
    expected_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, None],
    ]
    assert generate_board(
        size=3, tiles=list(range(1, 9)) + [None]
    ) == expected_board
