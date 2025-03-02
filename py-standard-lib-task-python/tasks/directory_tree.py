"""Template for programming assignment: Print directory tree"""
import os
from argparse import ArgumentParser
from typing import Iterator, Union

PathLike = Union[str, bytes, os.PathLike]

def depth_first_walk(root_dir: PathLike) -> Iterator[os.DirEntry]:
    """
    Iterates over all inner files and folders under the root
    directory and returns them in depth-first order.

    The depth-first order means the iteration starts at the root
    directory and goes as far as possible for each subfolder before
    backtracking to the next subfolder and remaining files. At each
    depth level, subfolders should be listed first in alphabetical
    order. Then, files should also be listed in alphabetical order.

    For example, suppose the root folder contains the folder "folder_a"
    and the file "file_a.txt". Also, suppose the folder contains the
    subfolder "folder_b" and the file "file_b.txt". Finally, suppose
    "folder_b" contains the file "file_c.txt". Such folder
    structure can be represented visually as follows:

    folder_a/
      folder_b/
        file_c.txt
      file_b.txt
    file_a.txt

    In such an example, the contents of the root folder should be
    iterated in the following order:

    folder_a/
    folder_a/folder_b/
    folder_a/folder_b/file_c.txt
    folder_a/file_b.txt
    file_a.txt

    Hint: please write a recursive function that applies os.scandir
    to list the contents of a directory.

    Args:
        root_dir: Path-like
            A root directory, the starting point for the iteration
    Yields:
        os.DirEntry, objects of the same type that the os.scandir
        function returns
    """
    entries = sorted(os.scandir(root_dir), key=lambda e: (not e.is_dir(), e.name))
    for entry in entries:
        yield entry
        if entry.is_dir():
            yield from depth_first_walk(entry.path)

def print_directory_tree(root_dir: PathLike, indent: int = 1, level: int = 0) -> None:
    """
    Prints the directory tree of a specified root folder.

    Directories should be printed in alphabetical order first, and
    then files should be printed in alphabetical order. Subfolders
    and inner files should be printed the same way under the line
    with the folder containing them, indented by the specified number
    of spaces relative to that line's indentation. Lines with directory
    names must end with a forward slash in the output string.

    For example, suppose the root folder contains the folder `folder_a`,
    which contains two files – `file_a.txt` and `file_b.txt` – and the
    file `file_c.txt`. If the indentation is with two spaces, the output
    must look as follows:
    '''
    folder_a/
      file_a.txt
      file_b.txt
    file_c.txt
    '''

    Args:
        root_dir: Path-like
            A root directory whose contents should be presented in
            the output string
        indent: int
            The Number of spaces to indent lines with subfolders and inner
            files (one space, by default)
        level: int
            The current level of indentation (used internally for recursion)

    Returns: None.
    """
    entries = sorted(os.scandir(root_dir), key=lambda e: (not e.is_dir(), e.name))
    
    # First print directories
    for entry in entries:
        if entry.is_dir():
            print(f"{' ' * (indent * level)}{entry.name}/")
            print_directory_tree(entry.path, indent, level + 1)
    
    # Then print files
    for entry in entries:
        if not entry.is_dir():
            print(f"{' ' * (indent * level)}{entry.name}")

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Directory tree printer',
        description='Prints the directory tree of a specified root folder.',
    )
    parser.add_argument('root_dir', help='Root directory to print')
    parser.add_argument('--indent', type=int, default=1, help='Number of spaces for indentation')
    args = parser.parse_args()
    print_directory_tree(args.root_dir, args.indent)
