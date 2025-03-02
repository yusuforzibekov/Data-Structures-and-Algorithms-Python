"""Sample tests for programming assignment:
Move tiles around the Gem Puzzle board"""
from tasks.game import (
    find_unoccupied_position, find_available_moves,
    move_tile, check_game_over,
    MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT)


def test_find_unoccupied_position():
    # Sample test 1
    board = [
        [2, 1, 7, 4],
        [10, 13, None, 12],
        [9, 5, 3, 14],
        [8, 6, 15, 11]
    ]
    assert find_unoccupied_position(board) == (1, 2)

    # Sample test 2
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, None]
    ]
    assert find_unoccupied_position(board) == (3, 3)


def test_find_available_moves():
    # Sample test 1
    board = [
        [2, 1, 7, 4],
        [10, 13, None, 12],
        [9, 5, 3, 14],
        [8, 6, 15, 11]
    ]
    assert find_available_moves(board) == {
        ((1, 1), 13, MOVE_RIGHT), ((1, 3), 12, MOVE_LEFT),
        ((0, 2), 7, MOVE_DOWN), ((2, 2), 3, MOVE_UP)
    }

    # Sample test 2
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, None]
    ]
    assert find_available_moves(board) == {
        ((3, 2), 15, MOVE_RIGHT), ((2, 3), 12, MOVE_DOWN)
    }


def test_move_tile():
    # Sample test 1
    board = [
        [2, 1, 7, 4],
        [10, 13, None, 12],
        [9, 5, 3, 14],
        [8, 6, 15, 11]
    ]
    move_tile(board, MOVE_RIGHT)
    assert board == [
        [2, 1, 7, 4],
        [10, None, 13, 12],
        [9, 5, 3, 14],
        [8, 6, 15, 11]
    ]

    # Sample test 2
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, None]
    ]
    expected_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, None],
        [13, 14, 15, 12]
    ]
    move_tile(board, MOVE_DOWN)
    assert board == expected_board

    # Sample test 3
    move_tile(board, MOVE_LEFT)
    assert board == expected_board  # board should not change


def test_check_game_over():
    # Sample test 1
    board = [
        [2, 1, 7, 4],
        [10, 13, None, 12],
        [9, 5, 3, 14],
        [8, 6, 15, 11]
    ]
    assert check_game_over(board) is False

    # Sample test 2
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, None]
    ]
    assert check_game_over(board) is True
