"""Sample tests for programming assignment: Find a string in files"""
import pytest
# A handy class to manage file paths regardless of the underlying OS
from pathlib import Path
from tasks.find_string import find_string_in_files


TESTS_ROOT = Path('tests', 'resources', 'find_string')


def test_find_string_in_files():
    # Sample tests
    files = [
        str(TESTS_ROOT / 'test1.txt'),
        str(TESTS_ROOT / 'test2.txt'),
        str(TESTS_ROOT / 'test3.txt')
    ]
    assert find_string_in_files(files, 'test') == (files[0], 0, 9)
    assert find_string_in_files(files, 'ipsum') == (files[1], 0, 6)
    assert find_string_in_files(files, 'ipsum.') == (files[2], 1, 6)
    with pytest.raises(ValueError):
        assert find_string_in_files(files, 'Python')
