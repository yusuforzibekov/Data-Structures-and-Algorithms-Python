"""Template for programming assignment: Find errors in logs"""
from typing import Tuple, List
import re


def parse_error_messages(log: str) -> List[Tuple[int, int, int, int, int, int, str]]:
    """
    Finds all ERROR-level log messages and parses them into tuples
    (year, month, day, hours, minutes, seconds, message).

    Args:
        log: str, multiline string, each line follows the format
             <LOG_LEVEL> - YYYY-MM-DD hh:mm:ss - <LOG_MESSAGE>
    Returns:
        List[Tuple[int, int, int, int, int, int, str]],
            list of parsed error-level log messages.
    """
    error_pattern = r"ERROR - (\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}) - (.+)"
    result = []
    for line in log.splitlines():
        if line.startswith("ERROR"):
            match = re.match(error_pattern, line)
            if match:
                year, month, day, hour, minute, second, message = match.groups()
                result.append((
                    int(year), int(month), int(day),
                    int(hour), int(minute), int(second),
                    message
                ))
    return result
