# [Python] Control Flow Statements

## Purpose

The coding exercises are designed to test knowledge of the following concepts:

* Conditional instructions in Python
* Loops in Python and related generators 

## Overview

The coding exercises cover the following practical problems:

* Sum two long numbers
* Reshape the matrix
* Convert roman number to integer number
* Convert integer number to roman number

## Coding exercises

### Exercise 1: Add two long numbers

Your task is to implement a function that adds two long integers represented as lists of digits.
Your function should return the list of digits (ints) of the number that is the sum of the
function arguments.

```Python
from typing import List


def sum_long_integers(number_1: List[int], number_2: List[int]) -> List[int]:
    """Returns the sum of two long numbers represented as
    lists of their digits in the same form.

    Examples:
        [2, 1] + [3, 6] = [5, 7], since 21 + 36 = 57
        [1, 2] + [9] = [2, 1], since 12 + 9 = 21
        [3, 6] + [1, 6, 3] = [1, 9, 9], since 36 + 163 = 199

    Args:
        number_1: List[int], the list of digits of the first term
        number_2: List[int], the list of digits of the second term
    Returns:
        List[int], the list of digits of the sum of input terms
    """
    pass
```

#### Example 1:
```
Input: number_1 = [2, 1], number_2 = [3, 6]
Output: [5, 7]
Explanation: 21 + 36 = 57
```

#### Example 2:
```
Input: number_1 = [1, 2], number_2 = [9]
Output: [2, 1]
Explanation: 12 + 9 = 21
```

#### Example 3:
```
Input: number_1 = [3, 6], number_2 = [1, 6, 3]
Output: [1, 9, 9]
Explanation: 36 + 163 = 199
```

### Exercise 2: Reshape a matrix

Reshaping is an operation that writes a matrix in other dimensions while preserving the order of its elements.

You are given an `m x n` `matrix` and two integers, `r`, and `c`, which represent the number of rows and
columns of the reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing
order as before.

If the reshape operation with the given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

```Python
from typing import List


def reshape_matrix(matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
    """Returns the reshaped version of the input matrix, i.e.
    the matrix written in other dimensions while preserving the
    row-traversing order of its elements.

    Examples:
        reshape_matrix([[1, 2], [3, 4]], 1, 4) -> [[1, 2, 3, 4]]
        reshape_matrix([[1, 2], [3, 4], [5, 6]], 2, 3) -> [[1, 2, 3], [4, 5, 6]]
        reshape_matrix([[1, 2], [3, 4]], 2, 4) -> [[1, 2], [3, 4]]

    Args:
        matrix: list of lists of ints, input matrix
        r: int, number of rows in the output matrix
        c: int, number of columns in the output matrix
    Returns:
        list of lists of ints, the reshaped matrix
    """
    pass
```

#### Example 1:
```
Input: matrix = [[1, 2], [3, 4]], r = 1, c = 4
Output: [[1, 2, 3, 4]]
```

#### Example 2:
```
Input: matrix = [[1, 2], [3, 4], [5, 6]], r = 2, c = 3
Output: [[1, 2, 3], [4, 5, 6]]
```

#### Example 3:
```
Input: matrix = [[1, 2], [3, 4]], r = 2, c = 4
Output: [[1, 2], [3, 4]]
```

### Exercise 3: Convert Roman numbers to integers

Seven symbols are used to represent Roman numerals: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, `2` is written `II`, which represents two ones added together.
`12` is written `XII`, or `X + II`. The number `27` is written `XXVII`, or `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`.
Because the one is before the five, it is subtracted to make four.
The same principle applies to the number nine, which is written `IX`.

There are six instances where subtraction is used:

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Convert a given Roman numeral to an integer.

```Python
def roman_to_integer(roman: str) -> int:
    """Converts a Roman numeral to an integer.

    Examples:
        "III" -> 3
        "LVIII" -> 58
        "MCMXCIV" -> 1994

    Args:
        roman: str, Roman numeral
    Returns:
        int, integer representation of a Roman numeral
    """
    pass
```

#### Example 1:
```
Input: roman = "III"
Output: 3
Explanation: III = 3
```

#### Example 2:
```
Input: roman = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3
```

#### Example 3:
```
Input: roman = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4
```

### Exercise 4: Convert an integer to Roman numeral

Seven symbols are used to represent Roman numerals: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, `2` is written `II`, which represents two ones added together.
`12` is written `XII`, or `X + II`. The number `27` is written `XXVII`, or `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`.
Because the one is before the five, it is subtracted to make four.
The same principle applies to the number nine, which is written `IX`.

There are six instances where subtraction is used:

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Convert a given integer to a Roman numeral.

```Python
def integer_to_roman(integer: int) -> str:
    """Converts an integer to a Roman numeral.

    Examples:
        3 -> "III"
        58 -> "LVIII"
        1994 -> "MCMXCIV"

    Args:
        integer: str, integer number
    Returns:
        str, string representation of a Roman numeral
    """
    pass
```

#### Example 1:
```
Input: integer = 3
Output: "III"
Explanation: 3 is represented as 3 ones
```

#### Example 2:
```
Input: integer = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3
```

#### Example 3:
```
Input: integer = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4
```
