"""Template for programming assignment: Visualize a Gem Puzzle board"""
from typing import List, Optional, Set, Tuple


def format_board_row_separator(row_string: str) -> str:
    """
    Prints separator line between two board rows to a string.

    Args:
        row_string: str, board row formatted as a string
    Returns:
        str, string of the same length as `row_string`
        consisting of dashes and two whitespaces at its borders.
    """
    return ' ' + '-' * (len(row_string) - 2) + ' '


def format_board_row(row: List[Optional[int]]) -> str:
    """
    Formats the board row as a string as follows:
    - every tile number must occupy two characters
      (if it occupies fewer characters, pad it with a whitespace
      on the left),
    - the unoccupied position must be printed with two whitespaces
    - tile numbers must be separated by " | ",
    - the row string must start with "| " and end with " |".

    For, example, for row = [1, 11, None, 9], its formatted string
    should look like the following: "|  1 | 11 |    |  9 |".

    Args:
        row: List[int or None], row of the board for Gem Puzzle game
    Returns:
        str, formatted string corresponding to the row.
    """
    formatted = [("  " if tile is None else str(tile).rjust(2)) for tile in row]
    return "| " + " | ".join(formatted) + " |"


def format_board(board: List[List[Optional[int]]]) -> str:
    """
    Prints the board for the Gem Puzzle game to a string in a "pretty" way.
    Each row must be printed using the format_board_row function.
    A dashed line must separate two subsequent rows that must be
    printed using the format_board_row_separator function. It must
    also be displayed before the first board row and after the last row.

    See an example of a correctly printed 4 x 4 board below:
     -------------------
    |  2 |  1 |  7 |  4 |
     -------------------
    | 10 | 13 |  3 | 12 |
     -------------------
    |  9 |  5 |    | 14 |
     -------------------
    |  8 |  6 | 15 | 11 |
     -------------------

    Args:
        board: List[List[int or None]], two-dimensional array
            corresponding to the board and tiles of the Gem Puzzle game.
    Returns:
        str, a formatted string of the board.
    """
    rows = [format_board_row(row) for row in board]
    sep = format_board_row_separator(rows[0])
    result = []
    for r in rows:
        result.extend([sep, r])
    result.append(sep)
    return "\n".join(result)


def format_available_moves(
    moves: Set[Tuple[Tuple[int, int], int, str]]
) -> str:
    """
    Prints available moves for the current state of the Gem puzzle game
    in the following format:
    "Available moves: {tile_number} -> {move_direction}, ..."

    For example, for the state of the board at the end of the game, the
    following line must be printed:
    "Available moves: 15 -> RIGHT, 12 -> DOWN"

    Args:
         moves: List[Tuple[Tuple[int, int], int, str]],
            the list of tuples ((`i`, `j`), `tile`, `move`), where
            (`i`, `j`) are zero-based indices of the tile that can
            be moved, `tile` is the number written on the tile, and
            `move` is one of the constants denoting the move that
            can be done (UP, DOWN, LEFT, RIGHT).

    Returns:
        str, formatted string of available moves.
    """
    return 'Available moves:' + ', '.join(
        [f'{tile} -> {move}' for _, tile, move in moves])
