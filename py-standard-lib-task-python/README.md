# [Python] Standard library overview

## Purpose

These coding exercises are designed to test your knowledge of the following concepts:

- Operating system-related modules of the standard library (e.g., `os`, `pathlib`, `glob`)
- Runtime-related modules of the standard library (e.g., `sys`, `argparse`)
- File format-related modules of the standard library (e.g., `csv`, `json`, `zipfile`)
- Mathematical modules of the standard library (e.g., `math`, `random`)
- Date and time-related modules of the standard library (e.g., `datetime`, `time`, `timeit`)
- Advanced iterators and data structures provided by the standard library (e.g., by `itertools`, `collections`)

## Overview

The coding exercises cover the following practical problems:

- Print directory tree
- Convert CSV to JSON
- Calculate biorhythm

## Coding exercises

### Exercise 1: Print directory tree

Your task is to implement a script that prints the directory tree of a specified folder.
Please solve this exercise in three steps.

#### Step 1

First, implement the helper generator function `depth_first_walk`.
It should iterate over all inner files and folders under
the root directory and return them in depth-first order.

The depth-first order means the iteration starts at the root directory
and goes as far as possible for each subfolder before backtracking
to the next subfolder and remaining files. At each  depth level,
subfolders should be listed first in alphabetical order. Then, files
should also be listed in alphabetical order.

For example, suppose the root folder contains the folder `folder_a`
and the file `file_a.txt`. Also, suppose the folder contains the subfolder
`folder_b` and the file `file_b.txt`. Finally, suppose `folder_b` contains
the file `file_c.txt`. Such folder structure can be represented visually as follows:
```
folder_a/
  folder_b/
    file_c.txt
  file_b.txt
file_a.txt
```

In such an example, the contents of the root folder should be iterated
in the following order:
```
folder_a/
folder_a/folder_b/
folder_a/folder_b/file_c.txt
folder_a/file_b.txt
file_a.txt
```

*Hint*: Please write a recursive function that applies `os.scandir`
to list the contents of a directory. 

#### Step 2

Now implement the function `print_directory_tree` for printing
the directory tree of a specified root folder.

Directories should be printed in alphabetical order first, and then
files should be printed in alphabetical order. Subfolders and inner files
should be printed the same way under the line with the folder containing them,
indented by the specified number of spaces relative to that line's indentation.
Lines with directory names must end with a forward slash in the output string.

For example, suppose the root folder contains the folder `folder_a`, which
contains two files – `file_a.txt` and `file_b.txt` – and the file `file_c.txt`.
If the indentation is with two spaces, the output must look as follows:
```
folder_a/
  file_a.txt
  file_b.txt
file_c.txt
```

#### Step 3

Finally, implement a command-line interface to your script using the `argparse` module.

Add one positional argument `root_dir` and one keyword argument `--indent`,
which only accepts integer values (1, by default).

Examples of invoking your script could be the following:
```commandline
python tasks/directory_tree.py tests/resources/directory_tree/case_1
python tasks/directory_tree.py tests/resources/directory_tree/case_2 --indent 4
```

```python
import os
from argparse import ArgumentParser
from typing import Iterator, Union

PathLike = Union[str, bytes, os.PathLike]

def depth_first_walk(root_dir: PathLike) -> Iterator[os.DirEntry]:
    pass

def print_directory_tree(root_dir: PathLike, indent: int = 1) -> None:
    pass


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Directory tree printer',
        description='Prints the directory tree of a specified root folder.',
    )
    pass
```

Please use the template `tasks/directory_tree.py` for the implementation.

### Exercise 2: Convert JSON to CSV

Your task is to implement the function `convert_csv_to_json` for converting
a CSV file to a JSON file in the format specified below.

Assume the first row of the input CSV file contains the column names.
Each row in the CSV file should be mapped to a dictionary in the following form:
```
{
    "<column_1>": <value_1>,
    "<column_2>": <value_2>,
    ...
}
```
The output JSON should be a list of the dictionaries that correspond
to the rows of the input CSV.

For example, consider the following CSV:
```
col1,col2
a,1
b,2
```

The output JSON for it should look as follows:
```json
[
    {"col1": "a", "col2": "1"},
    {"col1": "b", "col2": "2"}
]
```

```python
"""Template for programming assignment: Convert CSV to JSON"""
import csv
import json
import os
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def convert_csv_to_json(input_path: PathLike, output_path: PathLike) -> None:
    pass
```

Please use the template `tasks/csv_to_json.py` for the implementation.

### Exercise 3: Calculate biorhythm

Your task is to implement the function `calculate_biorhythm` for calculating
biorhythm cycles on a given date based on birthdate.

Biorhythm cycles are three values that are calculated using the following formulas:

```
Physical = 100 * sin(2 * PI * t / 23)
Emotional = 100 * sin(2 * PI * t / 28)
Intellectual = 100 * sin(2 * PI * t / 33)
```

where *t* is the number of days since birth.
Please round them to the nearest integers before returning an output.

For more information on biorhythms, please read the corresponding
[Wikipedia article](https://en.wikipedia.org/wiki/Biorhythm_(pseudoscience)).

```python
"""Template for programming assignment: Calculate biorhythm"""
import math
from datetime import datetime
from collections import namedtuple

# Replace None with the initialization of a namedtuple with three properties:
# "physical", "emotional" and "intellectual"
BiorhythmCycles = None

def calculate_biorhythm(birth_date: str, current_date: str) -> 'BiorhythmCycles':
    pass
```

#### Example 1
```
Input: birth_date = "1990-10-15", current_date = "2023-02-22"
Output: BiorhythmCycles(-89, 43, 69)
```

#### Example 2
```
Input: birth_date = "1974-01-29", current_date = "2011-12-14"
Output: BiorhythmCycles(40, 22, 91)
```

Please use the template `tasks/biorhythm.py` for the implementation.