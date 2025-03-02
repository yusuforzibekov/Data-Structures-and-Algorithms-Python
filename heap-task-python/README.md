# Priority Queue. The Heap sort algorithm

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The priority queue data structure as an API on top of a heap
* The heap sort algorithm

## Overview

The coding exercises cover the following practical problems:
* Implementing a basic priority queue API
* Implementing the heap sort algorithm
* Supporting an infinite set with the `pop_minimum` and `insert` operations


## Coding exercises

### Exercise 1: Implement a basic priority queue API

Your task is to implement the following class, which provides the basic `Priority Queue API`:

```python
class PriorityQueue:
    """The basic interface for Priority Queue."""

    def __init__(self):
        pass

    def get_minimum(self) -> int:
        """Returns the minimum in the data structure.

        NOTE: the expected time complexity is O(1).
        """
        pass
    
    def pop(self) -> int:
        """Returns the minimum in the data structure and removes it.
        
        NOTE: the expected time complexity is O(log N), where N is the number of elements in the data structure.
        """
        pass

    def insert(self, value: int):
        """Inserts a given value into the data structure.

        NOTE: the expected time complexity is O(log N), where N is the number of elements in the data structure.
        """
        pass

    def is_empty(self) -> bool:
        """Returns True if there are no elements in the data structure.
        
        NOTE: the expected time complexity is O(1).
        """
        pass
    
    def size(self) -> int:
        """Returns the number of elements in the data structure.
        
        NOTE: the expected time complexity is O(1).
        """
        pass  
```

**NOTE**:
* You cannot use the standard `heapq` library (We will do our best to catch you if you do - don't try us!)


**Example 1:**

```python
pq = PriorityQueue()
assert pq.is_empty() # empty at first

pq.insert(4) # {4}
pq.insert(3) # {3, 4}
pq.insert(2) # {2, 3, 4}
assert pq.size() == 3

assert pq.pop() == 2 # {3, 4}
assert pq.get_minimum() == 3

pq.insert(1) # {1, 3, 4}
assert pq.get_minimum() == 1
```

**Example 2:**

```python
pq = PriorityQueue()
pq.insert(1) # {1}
pq.insert(2) # {1, 2}
pq.insert(3) # {1, 2, 3}
pq.insert(4) # {1, 2, 3, 4}
pq.insert(5) # {1, 2, 3, 4, 5}

assert pq.pop() == 1 # {2, 3, 4, 5}
assert pq.pop() == 2 # {3, 4, 5}
assert pq.pop() == 3 # {4, 5}
assert pq.pop() == 4 # {5}
assert pq.pop() == 5 # {}

assert pq.is_empty()
```

<br>

Please use the template `tasks/priority_queue.py:PriorityQueue` for the implementation.

### Exercise 2: Implement the heap sort algorithm

Your task is to implement the following functions that, when combined, are `the Heap sort algorithm` itself:

```python
def min_heapify(data: List[int]) -> List[int]:
    """Returns the result of running the `heapify` (minimum) operation on a given array of numbers.

    What we know about the `heapify` operation:
    1) The expected time complexity of this operation is O(n), where n=|data|
    2) Here we're considering the "minimum" variation of `heapify`, so for the resulting array, the following
    conditions should hold (let's call the result array H):
        a) H[i] <= H[2 * i + 1], if 2 * i + 1 < n
        b) H[i] <= H[2 * i + 2], if 2 * i + 2 < n

    Basically the resulting array can be used as a base for the heap.

    Args:
        data: List[int], a given array of numbers to `heapify`
    Returns:
        List[int], the result of the `heapify` operation.
    """
    pass


def heap_sort(data: List[int]) -> List[int]:
    """Sorts a given array in ascending order using the heap sort algorithm.

    The idea is simple:
    1) First, use the `min_heapify` to get a heap
    2) Then, iteratively execute the `pop_minimum` operation (almost as in PriorityQueue.pop method) to create an ordered array

    NOTE: the expected time complexity is O(N * log N), where N=|data|

    Args:
        data: List[int], a given array to sort
    Returns:
        List[int], the ordered array
    """
    pass
```

**NOTE**: 
* The basic idea of how to implement `min_heapify` is described [here](https://www.baeldung.com/cs/binary-tree-max-heapify). You just need to adjust it for the *minimum* case.
* You can not use the `sorted` function or the standard `heapq` library (we will search for those words in your code, be cautious).


**Example 1:**

`data`=[6, 4, 2, 1, 6, 3]

Expected result:

`min_heapify(data)`=[1, 3, 2, 6, 6, 4]  # One of the available options

`heap_sort(data)`=[1, 2, 3, 4, 6, 6]


**Example 2:**

`data`=[1000, 100, 1, 10]

Expected result:

`min_heapify(data)`=[1, 10, 1000, 100]  # One of the available options

`heap_sort(data)`=[1, 10, 100, 1000]

<br>

Please use the templates `tasks/heap_sort.py:min_heapify+heap_sort` for the implementation.


### Exercise 3: An infinite set of natural numbers

Suppose you possess all the natural numbers out there: 1, 2, 3, 4, 5, ...

As the owner, you need to support the following operations:
* `pop_minimum()` - You give us the minimum number that you have.
* `insert(x)` - When we are finished playing with the number `x` (which you gave us before), we decide to give it back to you. It is guaranteed that you don't have `x` at that moment.

Your task is to implement the following class, which supports these operations for you:

```python
class InfiniteSet:
    """Emulates a set of all natural numbers."""

    def __init__(self):
        pass

    def pop_minimum(self) -> int:
        """Returns the minimum natural number available and removes it from the set.
        
        NOTE: the expected complexity is O(log K), where K is the total number of `pop_minimum/insert` calls done previously.
        """
        pass

    def insert(self, x: int):
        """Inserts a given number back into the set.

        NOTE: the expected complexity is O(log K), where K is the total number of `pop_minimum/insert` calls done previously.
        """
        pass
```

**Example 1:**

```python
inf_set = InfiniteSet() # {1, 2, 3, 4, 5, ...}
assert inf_set.pop_minimum() == 1 # {2, 3, 4, 5, 6, ...}
assert inf_set.pop_minimum() == 2 # {3, 4, 5, 6, ...}
assert inf_set.pop_minimum() == 3 # {4, 5, 6, ...}
assert inf_set.pop_minimum() == 4 # {5, 6, 7, ...}
assert inf_set.pop_minimum() == 5 # {6, 7, 8, ...}
inf_set.insert(3) # {3, 6, ...}
inf_set.insert(1) # {1, 3, 6, ...}
assert inf_set.pop_minimum() == 1 # {3, 6, 7, ...}
assert inf_set.pop_minimum() == 3 # {6, 7, 8, ...}
assert inf_set.pop_minimum() == 6 # {7, 8, 9, ...}
```


**Example 2:**

```python
inf_set = InfiniteSet() # {1, 2, 3, 4, 5, ...}

# ...
# After 100 .pop_minimum() operations
assert inf_set.pop_minimum() == 101 # {102, 103, 104, ...}
inf_set.insert(35) # {35, 102, 103, ...}
inf_set.insert(23) # {23, 35, 102, ...}
assert inf_set.pop_minimum() == 23 # {35, 102, ...}
assert inf_set.pop_minimum() == 35 # {102, 103, ...}
assert inf_set.pop_minimum() == 102 # {103, 104, ...}
```


<br>

Please use the template `tasks/infinite_set.py:InfiniteSet` for the implementation.
