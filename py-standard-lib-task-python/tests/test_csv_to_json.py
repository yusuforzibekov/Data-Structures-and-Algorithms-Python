"""Sample tests for programming assignment: Convert CSV to JSON"""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from tasks.csv_to_json import convert_csv_to_json


TESTS_ROOT = Path('tests', 'resources', 'csv_to_json')


def run_test_case(i: int, temp_dir: str) -> None:
    test_file_path = Path(TESTS_ROOT, f'case_{i}.csv')
    expected_file_path = Path(TESTS_ROOT, f'case_{i}.json')
    output_file_path = Path(temp_dir, f'output_{i}.json')

    convert_csv_to_json(test_file_path, output_file_path)

    with open(output_file_path, 'r') as fout, \
            open(expected_file_path, 'r') as fexp:

        output = json.load(fout)
        expected = json.load(fexp)
        assert output == expected, \
            f'Test case {i} failed.\n' \
            f'Output:\n{output}\n' \
            f'Expected:\n{expected}\n'


def test_convert_csv_to_json():
    with TemporaryDirectory() as temp_dir:
        # Sample tests
        run_test_case(1, temp_dir)
        run_test_case(2, temp_dir)
