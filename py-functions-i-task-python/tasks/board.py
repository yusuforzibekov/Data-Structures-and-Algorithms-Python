"""Template for programming assignment: Generate a Gem Puzzle board"""
import random
from typing import List, Optional


def generate_board(
    size: int = 4,
    tiles: List[Optional[int]] = None
) -> List[List[Optional[int]]]:
    """
    Generates a board for the Gem Puzzle game from the list of its tiles.
    If the list of tiles is not passed, generates a random board.
    By default, 4 x 4 board for classic 15 puzzle game should be
    generated.

    The board should be two-dimensional array (list of lists)
    of the shape `size` x `size` that contains some permutation of
    numbers from 1 to `size` squared minus one (e.g. from 1 to 15
    for size = 4) and exactly one None value corresponding to the
    unoccupied position.

    Args:
        size: int
            Size of the board for the Gem Puzzle game (defaults to 4).
        tiles: List[int or None]
            The permutation of the numbers from 1 to `size` squared minus
            one and a single None value. If None is passed, a random
            permutation should be generated.

    Returns: List[List[int or None]]
        The board for a Gem Puzzle game represented as a list of `size`
        lists, each of the length `size`, and containing the numbers 1 to
        `size` squared minus one and one None value.
    """
    if tiles is None:
        tiles = list(range(1, size * size)) + [None]
        random.shuffle(tiles)
    board = []
    for i in range(size):
        board.append(tiles[i * size:(i + 1) * size])
    return board
