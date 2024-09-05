# Basic sorting algorithms

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:
* The selection sort algorithm
* The insertion sort algorithm
* The bubble sort algorithm

## Overview

The coding exercises cover the following practical problems:
* Implementing and analyzing the selection sort algorithm
* Implementing and analyzing the insertion sort algorithm
* Implementing and analyzing the bubble sort algorithm

## Coding exercises

### Exercise 1: Partial Selection Sort

Your task is to implement the following function for partial sorting of a given array using `the selection sort algorithm` and a given number of iterations:

```python
def partial_selection_sort(data: List[int], k: int) -> List[int]:
    """Returns the partially sorted array after 'k' iterations of the Selection Sort algorithm.

    NOTE: after the first 'i' iterations - the first 'i+1' elements of the array should be ordered.  
    NOTE: 0 <= k < |data| 

    Args:
        data: List[int], a given list of values to order.
        k: int, the required number of selection sort iterations
    Returns:
        List[int], the result partially sorted array.
    """
    pass
```

**Example 1:**

`data`=[4,8,6,2,5]

`k`=1

Expected output: [**2**,8,6,4,5]


**Example 2:**

`data`=[4,8,6,2,5]

`k`=2

Expected output: [**2**,**4**,6,8,5]


**Example 3:**

`data`=[4,8,6,2,5]

`k`=3

Expected output: [**2**,**4**,**5**,8,6]


**Example 4:**

`data`=[4,8,6,2,5]

`k`=4

Expected output: [**2**,**4**,**5**,**6**,8]

<br>

Please use the template `tasks/sorting.py:partial_selection_sort` for the implementation.

### Exercise 2: Partial Insertion Sort

Your task is to implement the following function for partial sorting of a given array using `the insertion sort algorithm` and a given number of iterations:

```python
def partial_insertion_sort(data: List[int], k: int) -> List[int]:
    """Returns the partially sorted array after 'k' iterations of the Insertion Sort algorithm.

    NOTE: after the first 'i' iterations - the first 'i+1' elements of the array should be ordered.  
    NOTE: 0 <= k < |data| 

    Args:
        data: List[int], a given list of values to order.
        k: int, the required number of insertion sort iterations
    Returns:
        List[int], the result partially sorted array.
    """
    pass
```

**Example 1:**

`data`=[4,8,6,2,5]

`k`=1

Expected output: [**4**,**8**,6,2,5]


**Example 2:**

`data`=[4,8,6,2,5]

`k`=2

Expected output: [**4**,**6**,**8**,2,5]


**Example 3:**

`data`=[4,8,6,2,5]

`k`=3

Expected output: [**2**,**4**,**6**,**8**,5]


**Example 4:**

`data`=[4,8,6,2,5]

`k`=4

Expected output: [2,4,5,6,8]

<br>

Please use the template `tasks/sorting.py:partial_insertion_sort` for the implementation.

### Exercise 3: Partial Bubble Sort

Your task is to implement the following function for partial sorting of a given array using `the bubble sort algorithm` and a given number of **swaps**:

```python
def partial_bubble_sort(data: List[int], k: int) -> List[int]:
    """Returns the intermediate state of a given array after 'k' swaps of the Bubble Sort algorithm.

    NOTE: if 'k' exceeds the number of swaps required (and an array can be sorted
    in less than 'k' swaps) - just ignore the other 'potential' swaps and return the sorted array.

    Args:
        data: List[int], a given list of values to order.
        k: int, the required number of bubble sort swaps
    Returns:
        List[int], the result intermediate array after 'k' swaps.
    """
    pass
```

**Example 1:**

`data`=[4,8,6,2,5]

`k`=1

Expected output: [4,**6**,**8**,2,5]


**Example 2:**

`data`=[4,8,6,2,5]

`k`=2

Expected output: [4,6,**2**,**8**,5]


**Example 3:**

`data`=[4,8,6,2,5]

`k`=3

Expected output: [4,6,2,**5**,**8**]


**Example 4:**

`data`=[4,8,6,2,5]

`k`=4

Expected output: [4,**2**,**6**,5,8]

**Example 5:**

`data`=[4,8,6,2,5]

`k`=5

Expected output: [4,2,**5**,**6**,8]

**Example 6:**

`data`=[4,8,6,2,5]

`k`=6

Expected output: [**2**,**4**,5,6,8]

<br>

Please use the template `tasks/sorting.py:partial_bubble_sort` for the implementation.
