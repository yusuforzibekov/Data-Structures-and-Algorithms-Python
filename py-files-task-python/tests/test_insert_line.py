"""Sample tests for programming assignment: Insert a line into a file"""
# A handy class to manage file paths regardless of the underlying OS
from pathlib import Path
# A handy class able to create temporary directories
from tempfile import TemporaryDirectory
from typing import List
from tasks.insert_line import insert_line_into_file


def _test_one_example(
    input_file_lines: List[str],
    reference_file_lines: List[str],
    line_to_insert: str,
    position: int
) -> None:

    with TemporaryDirectory() as temp_dir:
        test_file_path = Path(temp_dir, 'file.txt')

        with open(test_file_path, 'w') as f:
            f.writelines([
                line + '\n' if (
                    i < len(input_file_lines)
                    and not line.endswith('\n')
                ) else line
                for i, line in enumerate(input_file_lines)
            ])

        insert_line_into_file(test_file_path, line_to_insert, position)

        with open(test_file_path, 'r') as f:
            output_lines = f.readlines()

    assert len(output_lines) == len(reference_file_lines)
    for output_line, reference_line in zip(output_lines, reference_file_lines):
        assert output_line.rstrip('\n') == reference_line


def test_insert_line():
    input_file_lines, line_to_insert = ['Line one', 'Line two'], 'Insert Line'

    # Sample test 1
    reference_lines = ['Line one', line_to_insert, 'Line two']
    _test_one_example(input_file_lines, reference_lines, line_to_insert, 1)

    # Sample test 2
    _test_one_example(input_file_lines, reference_lines, line_to_insert, -1)

    # Sample test 3
    reference_lines = [line_to_insert, 'Line one', 'Line two']
    _test_one_example(input_file_lines, reference_lines, line_to_insert, 0)

    # Sample test 4
    reference_lines = ['Line one', 'Line two', line_to_insert]
    _test_one_example(input_file_lines, reference_lines, line_to_insert, 2)
