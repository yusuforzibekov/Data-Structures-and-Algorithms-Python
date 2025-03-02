# [Python] Functions II

## Purpose

These coding exercises are designed to test your knowledge of the following concepts:

- Use class-related decorators (`@classmethod`, `@staticmethod`, `@property`)

## Overview

The coding exercises cover the following practical problems:

- Segments
- Lines

## Coding exercises

### Exercise 1: Segments

Consider a Cartesian coordinate system where every point is represented
as a pair of two coordinates *x* and *y*. In such a plane, a segment is defined
by its two endpoints.

Your task is to complete the class `Segment` (please use the template
`tasks/segment.py` for the implementation) by implementing its property
`length`, which should calculate the length of the segment. Note that the
supplementary class `Point` is already implemented for you in `tasks/point.py`.

```python
from tasks.point import Point

class Segment:
    """Represents segments in a plane by their two endpoints"""
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def length(self) -> float:
        """Calculates the length of the segment"""
        pass
```

#### Example 1:
```commandline
Input: p1 = Point(-1, 0), p2 = Point(1, 0)
Output: 2
```

#### Example 2:
```commandline
Input: p1 = Point(0, 3), p2 = Point(4, 0)
Output: 5
```


### Exercise 2: Lines

Consider a Cartesian coordinate system where every point is represented
as a pair of two coordinates *x* and *y*. In such a plane, a line can be defined
by a linear equation in the format a *x* + b *y* + c = 0.

Your task is to complete the class `Line` (please use the template
`tasks/line.py` for the implementation) by implementing two of its methods:
- The static method `are_parallel` should check whether two lines are parallel.
- The class method `from_two_points` should create a line based on two points
through which the line should pass.

Note that the supplementary class `Point` is already implemented for you
in `tasks/point.py`.

Also, note that a line can be represented by multiple
equivalent equations (these can be obtained by multiplying all coefficients
of the equation by the same number). So, there will be no unique correct output for
a fixed input passed to the function `from_two_points`. Thus, an equality operator
has been implemented for you that checks whether two lines are the
same by checking if their respective equations are equivalent. It is used in
tests to check if the output of a function is correct.

```python
from tasks.point import Point

class Line:
    """
    Represents lines in a plane by their linear
    equations in the format: a * x + b * y + c = 0
    """
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def are_parallel(l1: 'Line', l2: 'Line') -> bool:
        """Checks that two lines are parallel"""
        pass

    @classmethod
    def from_two_points(cls, p1: Point, p2: Point) -> 'Line':
        """Constructs a Line object based on two points
        through which the line should pass"""
        pass
```

#### Example 1:
```commandline
Method: are_parallel
Input: l1 = Line(1, 0, 1), l2 = Line(1, 0, 2)
Output: True
Explanation: lines x = -1 and x = -2 are parallel
```

#### Example 2:
```commandline
Method: are_parallel
Input: l1 = Line(1, -1, 0), l2 = Line(1, 0, 1)
Output: True
Explanation: lines y = x and x = -1 are not parallel
```

#### Example 3:
```commandline
Method: from_two_points
Input: p1 = Point(-1, 0), p2 = Point(-1, 1)
Output: Line(1, 0, 1)
Explanation: line x = -1 passes through the points mentioned.
```

#### Example 4:
```commandline
Method: from_two_points
Input: p1 = Point(-1, 0), p2 = Point(0, 1)
Output: Line(1, -1, 1)
Explanation: line y = x + 1 passes through the points mentioned.
```
