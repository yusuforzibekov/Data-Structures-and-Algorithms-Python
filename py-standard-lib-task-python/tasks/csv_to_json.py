"""Template for programming assignment: Convert CSV to JSON"""
import csv
import json
import os
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def convert_csv_to_json(input_path: PathLike, output_path: PathLike) -> None:
    """
    Converts a CSV file to a JSON file in the format specified below.

    Assume the first row of the input CSV file contains the column
    names. Each row in the CSV file should be mapped to a dictionary
    in the following form:
    {
        "<column_1>": <value_1>,
        "<column_2>": <value_2>,
        ...
    }
    The output JSON should be a list of such dictionaries that
    correspond to the rows of the input CSV.

    For example, consider the following CSV:
    col1,col2
    a,1
    b,2

    The output JSON for it should look as follows:
    [
        {"col1": "a", "col2": "1"},
        {"col1": "b", "col2": "2"}
    ]
    Args:
        input_path: Path-like
            A path to the input CSV file
        output_path: Path-like
            A path to the output JSON file
    Returns:
        None
    """
    with open(input_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
