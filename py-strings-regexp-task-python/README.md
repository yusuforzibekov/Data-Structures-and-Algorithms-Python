# [Python] Strings. Regular Expressions

## Purpose

The coding exercises are designed to test knowledge of the following concepts:

- Built-in string methods
- String formatting
- Regular expressions

## Overview

The coding exercises cover the following practical problems:

- Find errors in logs
- Print salary table
- Make naming consistent

## Coding exercises

### Exercise 1: Find errors in logs

Log files are usually used to monitor software system execution. Log records are chronological,
and every record has an assigned level - for example, a debug, warning, or error message.

Consider a log written in a multiline string in which each line has the following format:
```
<LOG_LEVEL> - <DATE_TIME> - <LOG_MESSAGE>
```
Here,
- `<LOG_LEVEL>`, which takes one of the following values: `DEBUG`, `INFO`, `WARNING` or `ERROR`,
- `<DATE_TIME>`, a date and time log message generated in the format `YYYY-MM-DD hh:mm:ss`, 
for example, `2022-01-14 15:00:59`
- `<LOG_MESSAGE>`, a free-form description of the event that happened.

An example:
```
ERROR - 2022-01-14 15:00:59 - Server does not respond
```

Your task is to find all `ERROR`-level messages in the log and parse them, i.e. return a list of tuples:
```
(year, month, day, hours, minutes, seconds, message)
```
These are `ERROR`-level messages. Here `year`, `month`, `day`, `hours`, `minutes`, `seconds`
must be integers extracted from `<DATE_TIME>`, and the `message` is the same as `<LOG_MESSAGE>` (a string).

```python
from typing import Tuple, List

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
    pass
```

#### Example 1:
```
Input: log = '''
DEBUG - 2022-01-14 14:58:02 - Request sent to the server
WARNING - 2022-01-14 15:00:01 - Request is processed to long
ERROR - 2022-01-14 15:00:59 - Server does not respond
ERROR - 2022-01-14 15:01:30 - Unexpected error
'''
Output: [
    (2022, 1, 14, 15, 0, 59, 'Server does not respond'),
    (2022, 1, 14, 15, 1, 30, 'Unexpected error'),
]
```

#### Example 2:
```
Input: log = '''
DEBUG - 2022-01-14 14:58:02 - Request sent to the server
WARNING - 2022-01-14 15:00:01 - Request is processed to long
DEBUG - 2022-01-14 15:00:10 - Got the response 200 OK
'''
Output: []
```

### Exercise 2: Print a salary table

You are given a list of tuples corresponding to human beings and their annual salary
```
(first_name, last_name, annual_salary)
```
Here, `first_name` and `last_name` are strings, and `annual_salary` is an integer.

Your task is to make a string formatted as a table containing the following columns:
- `#` - index number (starting from 1)
- `Person Name` - last name and the first letter of first name (e.g., for `John Johnson` it will be `Johnson J.`)
- `Annual Salary` - an integer followed by the `$` sign, thousands should be separated with comma (e.g., `100,000$`)
- `Monthly Salary` - annual salary divided by 12 followed by the `$` sign. It should be rounded to the first sign 
after decimal point and thousands should be separated with comma (e.g., `8,333.3$`)

The columns of the table should have the fixed width and alignment specified below:
- `#` - 5 symbols wide, right-aligned,
- `Person Name` - 20 symbols wide, left-aligned
- `Annual Salary` - 20 symbols wide, center-aligned
- `Monthly Salary` - 20 symbols wide, center aligned

It is guaranteed that the length of every input will not exceed the widths mentioned above.

The table should have the following header:
```
    # | Person Name         |    Annual Salary     |    Monthly Salary
-------------------------------------------------------------------------
```
` | ` should be used to separate columns. See an example below.

*Hint*: It is more efficient to make a list of strings corresponding to the table rows and eventually
`join` them, than to concatenate every new row string with the intermediate output.

```python
from typing import Tuple, List

def make_salary_table_string(
        humans_and_salaries: List[Tuple[str, str, int]]) -> str:
    """
    Returns a formatted sting containing the salary table
    described in README.

    Args:
        humans_and_salaries: List[Tuple[str, str, int]],
            list of tuples: human first name, last name and annual salary
    Returns:
        str, formatted sting containing the salary table
    """
    pass
```

#### Example:
```
Input: [('John', 'Johnson', 100000), ('Tom', 'Thompson', 90000)]
Output: the string that being printed looks as follows
    # | Person Name          |    Annual Salary     |    Monthly Salary
-------------------------------------------------------------------------
    1 | Johnson J.           |       100,000$       |       8,333.3$      
    2 | Thompson T.          |       90,000$        |       7,500.0$
```

### Exercise 3: Standardize naming

An *identifier* in Python code is the word that can consist of uppercase and lowercase letters A through Z,
an underscore _ and, except for the first character, the digits 0 through 9. Identifiers denote variables,
names of functions and methods, etc. The reserved words like `for`, `if`, `break`, etc., form a special
class of identifiers called *keywords*.

There are several naming styles for identifiers, including:
- *Camel Case*: An identifier is written in lower case, except for the first letters of its sub-words, which are
in upper case - for example, `someVariableWithLongName`.
- *Snake Case*: An identifier is written in lower case and its sub-words are separated with an underscore -
for example, `some_variable_with_long_name`.

Your input is (possibly multiline) string containing Python code with identifiers written in these two styles.
Your task is to determine the style that the majority of identifiers follow and standardize the naming of all
identifiers to this style.

*Notes*:
1. *Keywords* and single-word identifiers without digits should be ignored when the prevailing naming style
is being determined.<br>
To check if an identifier `s` is a keyword, you can use the method `is_keyword(s)`
from the standard library package `keyword` (it will be imported in your file with solution template).
2. In snake case identifiers, digits should also be separated from letters by an underscore. Otherwise,
the identifier will be considered written in camel case.<br>
For example, `variable_10` is the name of a variable in snake case, while `variable10` is the name of a variable
in camel case.
3. In camel case identifiers, consecutive uppercase letters or digits should be considered one word.
For example, `variableABC` in camel case converts to `variable_abc` in snake case.
4. If the number of snake case identifiers is equal to the number of camel case identifiers,
convert the latter to snake case.

```python
def make_naming_consistent(code: str) -> str:
    """
    Converts the naming of identifiers in Python code
    to the prevailing naming style (snake case or camel case).

    Args:
        code: str, Python code
    Returns:
        str, Python code with consistent naming style
    """
    pass
```

#### Example 1:
```
Input: '''
initNumber = 1
'''
Output: '''
initNumber = 1
'''
Explanation: there is one identifier (initNumber) in camel case,
and one indentifier (1) in an undetermined case, which is ignored.
```

#### Example 2:
```
Input: '''
for a_i, b_i in zip(aList, bList):
    print(a_i, b_i)
'''
Output: '''
for a_i, b_i in zip(a_list, b_list):
    print(a_i, b_i)
'''
Explanation: there are four identifiers in snake case (a_i, b_i, a_i, b_i),
three keywords (for, zip, print) that are ignored, and two indentifiers (aList, bList)
in camel case that are converted to snake case.
```

#### Example 3:
```
Input: '''
_abc_ = 0
variableABC10 = 1
if _abc_ < variableABC10:
    print(_abc_)
'''
Output: '''
_abc_ = 0
variable_abc_10 = 1
if _abc_ < variable_abc_10:
    print(_abc_)
'''
Explanation: there are three identifiers in snake case (_abc_ is repeated
three times), two keywords (if, print) that are ignored, and two indentifiers
in camel case (variableABC10 is repeated twice). variableABC10 converts to
variable_abc_10 since consecutive uppercase letters or digits form a single
word.
```

#### Example 4:
```
Input: '''
_ab__c_ = 0
variableABC10 = 1
if _ab__c_ < variableABC10:
    print(variableABC10)
'''
Output: '''
abC = 0
variableABC10 = 1
if abC < variableABC10:
    print(variableABC10)
'''
Explanation: there are three identifiers in camel case (variableABC10 is
repeated three times), two keywords (if, print) that are ignored, and two
indentifiers in snake case (_ab__c_ is repeated twice). _ab__c_ converts
to abC (multiple and trailing underscores are ignored).
```
