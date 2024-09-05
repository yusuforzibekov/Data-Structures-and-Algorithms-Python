# Queue

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The default queue interface
* Queues that are implemented using two stacks
* Using the queue data structure in practice

## Overview

The coding exercises cover the following practical problems:
* Implementing the default queue interface
* Implementing a queue using two stacks
* Calculating the number of islands in a grid
* Knight traversal


## Coding exercises

### Exercise 1: Implement the default queue interface

The following snippet contains the default interface, which can be used to implement the queue data structure. Of course, the interface can be expanded with additional methods if necessary.

```python
class Queue:
    """Default interface for Queue data structure."""

    def __init__(self):
        pass

    def empty(self) -> bool:
        """Returns True if the queue is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        pass

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        pass
```

Your task is to implement the default interface for the queue above.

<br/>

Please use the template `tasks/queue.py:Queue` for the implementation.

## Exercise 2: Implement a queue using two stacks

Your task is to implement a queue data structure using only two stacks. For this exercise, you should re-use your solution to the first problem from the stack problem set (`Exercise 1: Implement the default stack interface`).
Replace the template `tasks/stack.py:Stack` with your solution.

You should use the following template:
```python
class QueueViaStacks:
    """Default Queue interface implemented with two stacks only.

    NOTE: Stack interface is defined within `tasks/stack.py:Stack`, you may re-use
    the existing implementation (you should have created it at this point).

    NOTE: all methods of Queue interface should be implemented.
    """

    def __init__(self):
        # NOTE: __init__ shouldn't be changed.
        self.first_stack = Stack()
        self.second_stack = Stack()

    def empty(self) -> bool:
        """Returns True if the queue is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        pass

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        pass
```

<br/>

Please use the template `tasks/queue.py:QueueViaStacks` for the implementation.


## Exercise 3: Calculate the number of islands in a grid

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume all four edges of the grid are surrounded by water.

Your task is to implement the following function to solve the problem above:

```python
def get_islands_count(grid: List[List[str]]) -> int:
    """Returns the number of islands in a given grid.

    Hint: you need to go over the grid and 'explore' islands
    one by one, some sort of BFS (using queue) will do.
    """
    pass
```

**Example 1:**

`grid`:
```
000000000
001111100
001101000
001100000
000000000
```

Expected output: 1.

Explanation: there is only one island in the middle.

**Example 2:**

`grid`:
```
000000000
001110000
001100000
001100011
000000011
```

Expected output: 2.

Explanation: there is one island in the middle, and the second one is in the bottom-right corner.

<br/>

Please use the template `tasks/islands.py:get_islands_count` for the implementation.


## Exercise 4: Knight traversal

For a given `chessboard` (`8 x 8` cells), you need to determine the minimum number of moves for the knight (character `K`) to reach the destination cell (character `D`). It is guaranteed that the answer exists.

There are four types of cells available:

* `K` - the knight. It is guaranteed that it exists on the board.
* `D` - the destination cell. It is guaranteed that it exists on the board.
* `O` - obstacles. The knight cannot occupy cells with obstacles.
* `.` - empty cells. The knight can occupy these cells.

**Eligible moves**
![alt text](imgs/knight_moves.png "Eligible knight moves")

Your task is to implement the following function to solve the problem above:

```python
def get_minimum_knight_moves(chessboard: List[List[str]]) -> int:
    """Returns the minimum number of knight moves to reach the destination point."""
    pass
```

**Example 1:**

`chessboard`:
```
K.......
........
........
........
........
........
........
.....D..
```

Expected output: 4.

Explanation:
```
K.......
........
.1......
........
..2.....
........
...3....
.....D..
```

**Example 2:**

`chessboard`:
```
K...O...
.....O..
.O..OO..
.O......
...O.O..
O.OOO...
O.......
O....D..
```

Expected output: 6.

Explanation:
```
K...O...
..1..O..
2O..OO..
.O3.....
...O4O..
O.OOO.5.
O.......
O....D..
```

<br/>

Please use the template `tasks/knight.py:get_minimum_knight_moves` for the implementation.
