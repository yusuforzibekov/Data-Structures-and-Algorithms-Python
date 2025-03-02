"""Sample tests for programming assignment: Print directory tree"""
import re
import subprocess
from pathlib import Path


TESTS_ROOT = Path('tests', 'resources', 'directory_tree')


def run_test_case(i: int) -> None:
    root_directory = TESTS_ROOT / f'case_{i}'
    expected_paths = TESTS_ROOT.glob(f'expected_case_{i}_i*.txt')

    for expected_path in expected_paths:
        print(expected_path)
        m = re.match(rf'expected_case_\d+_i(\d+).txt', expected_path.name)
        indent = int(m.group(1))

        output = subprocess.check_output([
            'python',
            str(Path('tasks', 'directory_tree.py')),
            str(root_directory),
            '--indent',
            str(indent),
        ], encoding='utf-8').rstrip()

        expected = open(expected_path, 'r').read().rstrip()

        assert output == expected, \
            f'Test case {i} failed.\n' \
            f'Output:\n"""\n{output}\n"""\n' \
            f'Expected:\n"""\n{expected}\n"""'


def test_print_directory_tree():
    # Sample tests
    run_test_case(1)
    run_test_case(2)
