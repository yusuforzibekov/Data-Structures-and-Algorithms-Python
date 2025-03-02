"""Template for programming assignment:
Move tiles around the Gem Puzzle board"""
from typing import List, Set, Tuple, Optional
from tasks.board import generate_board


MOVE_UP = 'UP'
MOVE_DOWN = 'DOWN'
MOVE_LEFT = 'LEFT'
MOVE_RIGHT = 'RIGHT'


def find_unoccupied_position(
    board: List[List[Optional[int]]]
) -> Tuple[int, int]:
    """
    Finds the indices of the None value in the list of lists
    corresponding to the unoccupied position on the board
    for the Gem Puzzle game.

    Args:
        board: List[List[int or None]], a two-dimensional array
            corresponding to the board and tiles of the Gem Puzzle game.

    Returns:
        Tuple[int, int], zero-based row and column indices of
        the None value in the two-dimensional `board` array.
    """
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val is None:
                return (i, j)
    raise ValueError("No unoccupied position found")


def find_available_moves(
    board: List[List[Optional[int]]]
) -> Set[Tuple[Tuple[int, int], int, str]]:
    """
    Finds all available moves for the current state of the Gem Puzzle
    game board. Every tile adjacent to the unoccupied position can be
    moved to this position by making its previous position unoccupied.

    NOTE: Please re-use the find_unoccupied_position function and the
    constants MOVE_UP = "UP", MOVE_DOWN = "DOWN", MOVE_LEFT = "LEFT", and
    MOVE_RIGHT = "RIGHT" defined in the module file to denote the moves.

    Args:
        board: List[List[int or None]], a two-dimensional array
            corresponding to the board and tiles of the Gem Puzzle game.

    Returns:
        List[Tuple[Tuple[int, int], int, str]], the list of tuples
        ((`i`, `j`), `tile`, `move`), where (`i`, `j`) are zero-based
        indices of the tile that can be moved, `tile` is the number
        written on the tile, and `move` is one of the constants denoting
        the move that can be done (MOVE_UP, MOVE_DOWN, MOVE_LEFT,
        MOVE_RIGHT).
    """
    moves = set()
    n = len(board)
    i, j = find_unoccupied_position(board)
    # Tile to the left of blank moves RIGHT.
    if j > 0:
        moves.add(((i, j-1), board[i][j-1], MOVE_RIGHT))
    # Tile to the right of blank moves LEFT.
    if j < n - 1:
        moves.add(((i, j+1), board[i][j+1], MOVE_LEFT))
    # Tile above blank moves DOWN.
    if i > 0:
        moves.add(((i-1, j), board[i-1][j], MOVE_DOWN))
    # Tile below blank moves UP.
    if i < n - 1:
        moves.add(((i+1, j), board[i+1][j], MOVE_UP))
    return moves


def move_tile(board: List[List[Optional[int]]], move_direction: str) -> None:
    """
    Makes a move in the Gem Puzzle game, i.e. modifies the board for
    the Gem Puzzle game in-place by swapping the unoccupied position
    with some of the adjacent tiles according to the move direction
    specified.

    NOTE: Please re-use the find_available_moves function here.

    Args:
        board: List[List[int or None]], a two-dimensional array
            corresponding to the board and tiles of the Gem Puzzle game.
        move_direction: str from {"UP", "DOWN", "RIGHT", "LEFT"},
            direction in which the tile adjacent to the unoccupied
            the position should be moved; if no tile can be moved in
            the specified direction, do nothing.

    Returns:
        None, but the `board` should be modified in-place to reflect
        the new state after the move.
    """
    assert move_direction in {MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT}
    available = find_available_moves(board)
    for (ti, tj), tile, move in available:
        if move == move_direction:
            ui, uj = find_unoccupied_position(board)
            board[ui][uj], board[ti][tj] = board[ti][tj], board[ui][uj]
            break


def check_game_over(board: List[List[Optional[int]]]) -> bool:
    """
    Checks to see if the tiles are in ascending order with a single
    unoccupied position in the lower-right corner of the board
    for the Gem Puzzle game (i.e., the game is over).

    Args:
        board: List[List[Optional[int]]], a two-dimensional array
            corresponding to the board and tiles of the Gem Puzzle game.

    Returns:
        bool, whether the tails of the `board` are located in
        ascending order with a single unoccupied position in the
        lower-right corner or not.
    """
    n = len(board)
    expected = list(range(1, n * n)) + [None]
    flat = [cell for row in board for cell in row]
    return flat == expected
