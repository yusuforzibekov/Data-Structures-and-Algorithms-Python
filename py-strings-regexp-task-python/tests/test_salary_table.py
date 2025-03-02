"""Sample tests for 'tasks.salary_table' module."""
from tasks.salary_table import make_salary_table_string


def test_make_salary_table_string():
    # Sample test
    humans_and_salaries = [
        ('John', 'Johnson', 100000),
        ('Tom', 'Thompson', 90000)
    ]
    expected_output = '\n'.join([
        '    # | Person Name          |    Annual Salary     |    Monthly Salary   ',
        '--------------------------------------------------------------------------',
        '    1 | Johnson J.           |       100,000$       |       8,333.3$      ',
        '    2 | Thompson T.          |       90,000$        |       7,500.0$      ',
    ])
    assert make_salary_table_string(humans_and_salaries) == expected_output
