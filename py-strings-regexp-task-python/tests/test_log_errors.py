"""Sample tests for 'tasks.log_errors' module."""
from tasks.log_errors import parse_error_messages


def test_parse_error_messages():
    # Sample test 1
    test_log = '\n'.join([
        'DEBUG - 2022-01-14 14:58:02 - Request sent to the server',
        'WARNING - 2022-01-14 15:00:01 - Request is processed to long',
        'ERROR - 2022-01-14 15:00:59 - Server does not respond',
        'ERROR - 2022-01-14 15:01:30 - Unexpected error',
    ])
    expected_errors = [
        (2022, 1, 14, 15, 0, 59, 'Server does not respond'),
        (2022, 1, 14, 15, 1, 30, 'Unexpected error'),
    ]
    assert parse_error_messages(test_log) == expected_errors

    # Sample test 2
    test_log = '\n'.join([
        'DEBUG - 2022-01-14 14:58:02 - Request sent to the server',
        'WARNING - 2022-01-14 15:00:01 - Request is processed to long',
        'DEBUG - 2022-01-14 15:00:10 - Got the response 200 OK',
    ])
    assert parse_error_messages(test_log) == []
