"""Sample tests for programming assignment: Rotating file"""
import os
import pytest
# A handy class to manage file paths regardless of the underlying OS
from pathlib import Path
# A handy class able to create temporary directories
from tempfile import TemporaryDirectory
from typing import List

from tasks.rotating_file import RotatingFile


def test_rotating_file_read():
    # Utility function
    def add_file(text: str, folder: str, i: int = 0):
        p = str(Path(folder, f'file.{i}' if i else 'file'))
        with open(p, 'w') as f:
            f.write(text)

    with TemporaryDirectory() as temp_dir:
        path = str(Path(temp_dir, 'file'))

        # Sample test 1: just one file
        add_file('abcd', temp_dir, i=0)
        with RotatingFile(path, 'r', max_size=5, max_backups=2) as rf:
            assert rf.read() == 'abcd'

        # Sample test 2: main file + one backup
        add_file('efghj', temp_dir, i=1)
        with RotatingFile(path, 'r', max_size=5, max_backups=2) as rf:
            assert rf.read() == 'efghj\nabcd'


def test_rotating_file_write():
    # Utility function
    def check_files(folder: str, file_contents: List[str]):
        assert len(os.listdir(folder)) == len(file_contents)
        for filename, content in zip(sorted(os.listdir(folder)), file_contents):
            with open(Path(folder, filename), 'r') as f:
                assert f.read() == content

    with TemporaryDirectory() as temp_dir:
        path = str(Path(temp_dir, 'file'))

        # Sample test 1: just one file
        with RotatingFile(path, 'a+', max_size=5, max_backups=2) as rf:
            rf.write('ab')
        check_files(temp_dir, ['ab'])

        # Sample test 2: again just one file
        with RotatingFile(path, 'a+', max_size=5, max_backups=2) as rf:
            rf.write('cd')
        check_files(temp_dir, ['abcd'])

        # Sample test 3: again just one file, but big input string for writing
        with pytest.raises(Exception):
            with RotatingFile(path, 'a+', max_size=5, max_backups=2) as rf:
                rf.write('abcdefghigjklmnop')

        # Sample test 4: main file + one backup
        with RotatingFile(path, 'a+', max_size=5, max_backups=2) as rf:
            rf.write('efghj')
        check_files(temp_dir, ['efghj', 'abcd'])
