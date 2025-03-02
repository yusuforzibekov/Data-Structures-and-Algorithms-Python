"""Template for programming assignment: Find a string in files"""
import os
from typing import List, Tuple, Union

PathLike = Union[str, bytes, os.PathLike]

def find_string_in_files(
    filepaths: List[PathLike],
    s: str
) -> Tuple[PathLike, int, int]:
    """
    Finds the first text file in the list that contains the specified
    string and returns that file path, along with the first position
    in the file where the specified string begins.

    Args:
        filepaths: List[PathLike],
            A list of paths of the text files to search for
            the specified string
        s: str,
            The target string for the search
    Returns:
        filepath: PathLike,
            The path of the first file containing the specified string
        lineno: int,
            The index of the first line in the file containing the
            specified string (zero-based)
        linepos: int,
            The first position in the line where the specified string
            begins
    Raises:
        ValueError: If the string is absent in all files
    """
    for filepath in filepaths:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line_no, line in enumerate(lines):
                pos = line.find(s)
                if pos != -1:
                    return filepath, line_no, pos
    raise ValueError("String not found in any file")
