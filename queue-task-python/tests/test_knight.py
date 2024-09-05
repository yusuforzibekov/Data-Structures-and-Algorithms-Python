"""Sample tests for 'tasks.knight' module."""
from tasks.knight import get_minimum_knight_moves


def test_get_minimum_knight_moves_sample():
    """Sample tests for get_minimum_knight_moves function."""
    assert get_minimum_knight_moves(
        [
            list('K.......'),
            list('........'),
            list('........'),
            list('........'),
            list('........'),
            list('........'),
            list('........'),
            list('.....D..')
        ]
    ) == 4

    assert get_minimum_knight_moves(
        [
            list('K...O...'),
            list('.....O..'),
            list('.O..OO..'),
            list('.O......'),
            list('...O.O..'),
            list('O.OOO...'),
            list('O.......'),
            list('O....D..')
        ]
    ) == 6
