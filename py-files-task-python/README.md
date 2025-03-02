# [Python] File handling. Context management

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

- Using files to work with permanent data in Python
- Context management in Python

## Overview

The coding exercises cover the following practical problems:

- Finding a string in files
- Inserting a line into a file
- Rotating a file

## Coding exercises

### Exercise 1: Finding a string in files

Your task is to implement the function `find_string_in_files` to find the
first text file in a list that contains a specified string and return
that file path along with the first position in the file where the specified
string begins. The position is described by the line number and the position
within that line. If none of the files contains a string, a `ValueError`
should be raised.

```python
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
    pass
```

See the `tests/test_find_string.py` file and the `tests/resources/find_string/`
folder for examples.

### Exercise 2: Inserting a line into a file

Your task is to implement the function `insert_line_into_file` to insert a
specified line into a file at a specified position. Position is equivalent
to an index in a Python array. If this position is negative, the
insertion position is counted from the end of the file. If it is
positive and greater than or equal to the number of lines in the input file,
the specified string should be inserted at the end of the file without a
trailing newline character. If the position is negative and its absolute value
is greater than or equal to the number of lines in the input file, the
specified string should be inserted at the beginning of the file.

*Note*: Feel free to open the input file twice, for both reading and
writing. The input will be such that it fits into the memory.

```python
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
    pass
```

See the `tests/test_insert_line.py` file for examples.

### Exercise 3: Rotating a file

Your task is to implement the context manager class `RotatingFile` for file-like
objects that behaves as follows:

- Content is written to the file until the number of characters 
  in it reaches the specified limit, in which case a rollover is performed.
- Upon rollover, the contents of the current file are copied to a new
  backup file in almost the same path, but with the suffix ".1" at
  the end. In this case, a new file is silently opened for writing at the
  current path.
- When the length of the current file reaches the limit again, the
  rollover is repeated, and the existing backup files are renamed so
  that the file with the suffix ".1" will have the suffix ".2," the
  file with the suffix ".2" will have the suffix ".3," etc.
- When the number of backup files exceeds another specified limit,
  the file with the maximum number in the path suffix is removed.

For example, with a limit on the number of backups of 5 and a base file
name of `app.txt`, you would get `app.txt`, `app.txt.1`, and `app.txt.2`,
up to `app.txt.5`. The file being written to is always `app.txt`. When
this file is filled, it is closed and renamed `app.txt.1`, and if the files
`app.txt.1`, `app.txt.2`, etc., exist, they are renamed `app.txt.2`,
`app.txt.3`, etc., respectively.

Please implement the methods `read`, `write`, and `rollover`. Complete the
implementation of the `__init__` methods and see their docstrings for more
information. The methods `__enter__` and `__exit__` are already implemented for you.

```python
class RotatingFile:
    """
    The context manager class for file-like objects behaves
    as follows:
    - Content is written to the file until the number of characters
      in it reaches the specified limit, in which case a rollover is
      performed.
    - Upon rollover, the contents of the current file are copied to a new
      backup file in almost the same path, but with the suffix ".1" at
      the end. In this case, a new file is silently opened for writing
      at the current path.
    - When the length of the current file reaches the limit again, the
      rollover is repeated, and the existing backup files are renamed so
      that the file with the suffix ".1" will have the suffix ".2," the
      file with the suffix ".2" will have the suffix ".3," etc.
    - When the number of backup files exceeds another specified limit,
      the file with the maximum number in the path suffix is removed.

    For example, with a limit on the number of backups of 5 and a base file
    name of app.txt, you would get app.txt, app.txt.1, and app.txt.2, up to
    app.txt.5. The file being written to is always app.txt. When this
    file is filled, it is closed and renamed app.txt.1, and if the files
    app.txt.1, app.txt.2, etc., exist, they are renamed app.txt.2,
    app.txt.3, etc., respectively.
    """
    def __init__(
        self,
        filepath: str,
        mode: str,
        max_size: int,
        max_backups: int
    ) -> None:
        """
        Args:
            filepath: List[PathLike],
                Path to the main file
            mode: str,
                The mode in which the file is opened
            max_size: int,
                The maximum number of characters in the main file.
                When a write operation is such that the resulting file
                length exceeds this limit, a rollover must be performed
            max_backups: int,
                The maximum number of backup files that can be
                generated during rollover operations
        """
        self.file = open(filepath, mode)
        pass

    def read(self) -> str:
        """
        Reads the text stored in all files (including the backup files),
        starting with the main file and ending with the last backup
        file. The contents of different files must be separated by a
        newline character.
        """
        pass

    def rollover(self) -> None:
        """
        Performs the rollover
        For example, with a limit on the number of backups of 5 and a base file
        name of app.txt, you would get app.txt, app.txt.1, and app.txt.2, up to
        app.txt.5. The file being written to is always app.txt. When this
        file is filled, it is closed and renamed app.txt.1, and if the files
        app.txt.1, app.txt.2, etc., exist, they are renamed app.txt.2,
        app.txt.3, etc., respectively.

        NOTE: you can use os.remove function to remove a file, and os.rename
        function to rename a file.
        """
        pass

    def write(self, s: str) -> None:
        """
        Writes a string to the main file and does the rollover if
        the string being written adds so many characters that the
        length of the main file exceeds the `max_size` limit.
        If the length of the input string exceeds the `max_size`
        limit, an exception must be raised.
        """
        pass
```

See the `tests/test_rotating_file.py` file for examples.
