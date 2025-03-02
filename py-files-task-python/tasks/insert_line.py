"""Template for programming assignment: Insert a line into a file"""
import os
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def insert_line_into_file(filepath: PathLike, line: str, position: int) -> None:
    """
    Inserts the specified line into the file at the specified position.
    Position is equivalent to an index in a Python array. If the position
    is negative, the insertion position is counted from the end of the file.
    If it is positive and greater than or equal to the number of lines
    in the input file, the specified string should be inserted at the end
    of the file without a trailing newline character. If the position is
    negative and its absolute value is greater than or equal to the number
    of lines in the input file, the specified string should be inserted at
    the beginning of the file.

    NOTE: Feel free to open the input file twice, for both reading and
        writing. The input will be such that it fits into the memory.

    Args:
        filepath: List[PathLike],
            The path of the file to be edited
        line: str,
            The string to be inserted
        position: int,
            The position of the string in the output (zero-based,
            similar to Python slicing indices, which can be negative)
    Returns:
        Nothing, but modifies the input file in-place
    """
    # Read all lines
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Handle line endings
    lines = [l.rstrip('\n') for l in lines]
    
    # Handle position
    if position < 0:
        position = max(0, len(lines) + position)
    if position >= len(lines):
        position = len(lines)
    
    # Insert the line
    lines.insert(position, line)
    
    # Write back to file
    with open(filepath, 'w') as f:
        for i, l in enumerate(lines):
            if i < len(lines) - 1:
                f.write(l + '\n')
            else:
                f.write(l)
