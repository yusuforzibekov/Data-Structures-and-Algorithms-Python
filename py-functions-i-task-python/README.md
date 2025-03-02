# [Python] Functions I

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

- Defining and calling functions in Python
- Keyword and positional arguments of Python functions
- Documenting functions with docstrings

## Overview

The coding exercises cover the following practical problems:

- Generate a Gem Puzzle board
- Visualize a Gem Puzzle board
- Move tiles around the Gem Puzzle board

## Coding exercises

A [**15 Puzzle**](https://en.wikipedia.org/wiki/15_puzzle), or a **Gem Puzzle**
(or ***N* Puzzle** in general), has been a popular game across generations.
It is a sliding puzzle with 15 square tiles numbered 1–15 in a frame
that is four tiles high and four tiles wide (in general, *n*^2 - 1 tiles numbered
from 1 to *n*^2 - 1 in an *n* x *n* frame), leaving one unoccupied tile position.
The object of the game is to put the tiles in order from 1 to 15 so that the blank
space is in the lower-right corner.

By completing these coding exercises you will implement the 15 puzzle game in the command line.
These coding exercises decompose the larger task into smaller, easier subtasks.

### Exercise 1: Generate a Gem Puzzle board

Your task is to implement a function that generates a Gem Puzzle board.
The board will be reflected in code as two-dimensional array (a list of lists)
of the shape *n* x *n*, whose elements are numbers from 1 to *n*^2 - 1 and one `None`
value, which corresponds to the unoccupied position on the board.

The function should have two keyword arguments:
- `size` refers to the size of the board (4 by default)
- `tiles` (if passed) refer to the permutation of numbers from 1 to the `size`
squared minus one, and one `None` to be placed on the board from left to right
and from top to bottom. Defaults to `None`, which means the numbers should be
randomly placed on the board.

Please use the template in `tasks/board.py` for your implementation.

*Hint*: To generate a random board, you can randomly shuffle the list of numbers
from 1 to *n*^2 - 1 and `None`, and reshape it to an array of the size *n* x *n*
the same way you did in one of the previous exercises. Python has the standard
function `shuffle` from the `random` package for random shuffling.
It can be called `random.shuffle(my_list)`. It does not return anything;
it shuffles the `my_list` in-place. The `random` package is already imported
into your module; feel free to use it.

```python
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
    pass
```
#### Example 1
```
Input: size = 4, tiles = [2, 1, 7, 4, 10, 13, None, 12, 9, 5, 3, 14, 8, 6, 15, 11]
Output:  [
    [2, 1, 7, 4],
    [10, 13, None, 12],
    [9, 5, 3, 14],
    [8, 6, 15, 11]
]
```

#### Example 2
```
Input: size = 3, tiles = [1, 2, 3, 4, 5, 6, 7, 8, None]
Output:  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]
```

#### Example 3
```
Input: size = 4, tiles = None
Output: a random 4 x 4 array with numbers from 1 to 15 and one None value.
```

### Exercise 2: Visualize a Gem Puzzle board

Your task is to implement two functions related to the visualization of the Gem Puzzle board:
the main function `format_board` and the auxiliary function `format_board_row`.

1. `format_board_row` should format the board row as a string as follows:
    - every tile number must occupy two characters
      (if it occupies fewer characters, pad it with a whitespace on the left),
    - the unoccupied position must be printed with two whitespaces
    - tile numbers must be separated by " | ",
    - the row string must start with "| " and end with " |".
   See an example below.
2. `format_board` should print the Gem Puzzle board to a string in a "pretty" way.
    Each row must be printed using the `format_board_row` function. A dashed line must
    separate two subsequent rows, and it must also be displayed before the first and
    after the last row of the board. Note that the function printing the dashed line
    is called `format_board_row_separator` and has already been implemented for you
    (please re-use it).

Please use the template in `tasks/visualization.py` for your implementation.

```python
from typing import List, Set, Tuple, Optional


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
    pass


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
    pass
```

#### Example 1 (format_board_row)
```
Input: row = [1, 11, None, 9]
Output: "|  1 | 11 |    |  9 |"
```
#### Example 2 (format_board_row)
```
Input: row = [1, 2, 3, 4]
Output: "|  1 |  2 |  3 |  4 |"
```
#### Example 3 (format_board)
```
Input: board = [[2, 1, 7, 4],
                [10, 13, 3, 12],
                [9, 5, None, 14],
                [8, 6, 15, 11]]

Output: a formatted string being printed looks like the following:
 -------------------
|  2 |  1 |  7 |  4 |
 -------------------
| 10 | 13 |  3 | 12 |
 -------------------
|  9 |  5 |    | 14 |
 -------------------
|  8 |  6 | 15 | 11 |
 -------------------
```

#### Example 4 (format_board)
```
Input: board = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, None]]

Output: a formatted string being printed looks like the following:
 -------------------
|  1 |  2 |  3 |  4 |
 -------------------
|  5 |  6 |  7 |  8 |
 -------------------
|  9 | 10 | 11 | 12 |
 -------------------
| 13 | 14 | 15 |    |
 -------------------
```

### Exercise 3: Move tiles around the Gem Puzzle board

Now it is time to implement the core functions of the game:
- The `find_unoccupied_position` function should find the row and column indices of the
  `None` value in the list of lists corresponding to the unoccupied position on the Gem Puzzle board.
- The `find_available_moves` function should find all available moves for the current state of 
  the Gem Puzzle board. Every tile adjacent to the unoccupied position can be moved to this
  position by making its previous position unoccupied. *Note*: Please use the `find_unoccupied_position`
  function in your implementation of this function.
- `move_tile` should make a move in the Gem Puzzle game, i.e. modify the board for Gem puzzle game
  in-place by swapping the unoccupied position with some of the adjacent tiles according to the move
  direction specified. *Note*: Please use the `find_available_moves` function in your implementation
  of this function.
- `check_game_over` should check to see if the tiles are in ascending order with a single
  unoccupied position in the lower-right corner of the Gem Puzzle board (i.e., the game is over).

Please use the template in `tasks/game.py` for your implementation.

```python
from typing import List, Set, Tuple, Optional


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
    pass


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
    pass


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
    pass


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
    pass
```

#### Example 1 (find_unoccupied_position)
```
Input: board = [
    [2, 1, 7, 4],
    [10, 13, None, 12],
    [9, 5, 3, 14],
    [8, 6, 15, 11]
]
Output: (1, 2)
```
#### Example 2 (find_unoccupied_position)
```
Input: board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, None]
]
Output: (3, 3)
```
#### Example 3 (find_available_moves)
```
Input: board = [
    [2, 1, 7, 4],
    [10, 13, None, 12],
    [9, 5, 3, 14],
    [8, 6, 15, 11]
]
Output: {
    ((1, 1), 13, "RIGHT"), ((1, 3), 12, "LEFT"),
    ((0, 2), 7, "DOWN"), ((2, 2), 3, "UP")
}
```
#### Example 4 (find_available_moves)
```
Input: board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, None]
]
Output: {
    ((3, 2), 15, "RIGHT"), ((2, 3), 12, "DOWN")
}
```
#### Example 5 (move_tile)
```
Input: move = "RIGHT", board = [[2, 1, 7, 4],
                                [10, 13, None, 12],
                                [9, 5, 3, 14],
                                [8, 6, 15, 11]]
Output: [
    [2, 1, 7, 4],
    [10, None, 13, 12],
    [9, 5, 3, 14],
    [8, 6, 15, 11]
]
```
#### Example 6 (move_tile)
```
Input: move = "DOWN", board = [[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, None]]
Output: [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, None],
    [13, 14, 15, 12]
]
```
#### Example 7 (move_tile)
```
Input: move = "LEFT", board = [[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, None],
                                [13, 14, 15, 12]]
Output: [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, None],
    [13, 14, 15, 12]
]
```
#### Example 8 (check_game_over)
```
Input: board = [[2, 1, 7, 4],
                [10, 13, None, 12],
                [9, 5, 3, 14],
                [8, 6, 15, 11]]
Output: False
```
#### Example 9 (check_game_over)
```
Input: board = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, None]]
Output: True
```

### Bonus
Run the `python play.py` command from the root of your repository and play the
Python version of the game you just implemented. Enjoy! :)
