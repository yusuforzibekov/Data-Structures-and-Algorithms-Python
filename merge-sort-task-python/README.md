# The Merge sort algorithm

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The merge sort algorithm
* The divide and conquer paradigm

## Overview

The coding exercises cover the following practical problems:
* Merging two sorted linked lists
* Implementing the merge sort algorithm

## Coding exercises

### Exercise 1: Merge two sorted linked lists

As you should already know, a linked list can be represented in memory using the following data structure for its elements:

```python
class ListNode:
    """Data class for representing singly-linked list's nodes."""

    def __init__(self, value: int = None, next: "ListNode" = None):
        self.value = value
        self.next = next
```

Your task is to implement the following function, which merges two given linked lists (that are already sorted), to obtain a new sorted linked list:

```python
def merge_sorted_lists(list_a: Optional[ListNode], list_b: Optional[ListNode]) -> Optional[ListNode]:
    """Returns a merged (sorted) linked list head using two given (sorted) linked lists.

    NOTE: the expected time complexity is O(n+m), where n=|list_a| and m=|list_b|

    Args:
        list_a: ListNode, the head element of the first sorted linked list
        list_b: ListNode, the head element of the second sorted linked list
    Returns:
        ListNode, the result of merging two given lists
    """
    pass
```

**Example 1:**

`list_a`="(5) -> (11) -> (30)"
`list_b`="(1) -> (6)"

Expected output:

"(1) -> (5) -> (6) -> (11) -> (30)"

**Example 2:**

`list_a`="(5) -> (11) -> (30)"
`list_b`="None"

Expected output:

"(5) -> (11) -> (30)"

**Example 3:**

`list_a`="(5) -> (11) -> (30)"
`list_b`="(5) -> (11) -> (30)"

Expected output:

"(5) -> (5) -> (11) -> (11) -> (30) -> (30)"

<br>

Please use the template `tasks/linked_list.py:merge_sorted_lists` for the implementation.

### Exercise 2: Implement the merge sort algorithm

Your task is to implement the following functions to get the complete merge sort algorithm:

```python
def merge_sorted_subarrays(
    data: List[int],
    left_index: int,
    middle_index: int,
    right_index: int,
):
    """Merges two sorted subarrays of a given list (in-place).
    
    Assume the first ordered subarray is within the [left_index; middle_index] interval
    and the second subarray is within the (middle_index; right_index] interval.

    NOTE: even though this function should work in-place, you can use up to O(n) auxiliary space,
        where n = right_index - left_index + 1
    NOTE: the expected time complexity is O(n), where n = right_index - left_index + 1

    Args:
        data: List[int], a given list that contains two subarrays for merging
        left_index: int, defines the left bound of the first subarray
        middle_index: int, defines the right bound of the first subarray
        right_index: int, defines the right bound of the second subarray
    """
    pass


def merge_sort_algorithm(data: List[int]) -> Tuple[List[int], int]:
    """Returns the sorted array and a `special statistic` that will be defined below.

    The idea is simple: You use the merge sort algorithm to order a given array, and that's it.
    The algorithm is simple: You divide the current subarray, sort both parts, and then merge them.
    
    NOTE: The statistic you need to calculate has the following definition:
    * At the beginning of the algorithm `statistic=0`
    * Each time you use the `merge_sorted_subarrays` function, you should do the following BEFORE and AFTER each call:
        * `statistic += data[left_index]`
        * `statistic += data[middle_index]` (even if left_index == middle_index)
        * `statistic += data[right_index]`
    Ask yourself, "But why?" You know, just to avoid silly stuff like "return sorted(data)".

    NOTE: you are expected to implement `merge_sorted_subarrays` before starting with this function
    NOTE: the expected time complexity is O(n * log n), where n=|data|

    Args:
        data: List[str], a given list of elements to sort (in ascending order)
    Returns:
        Tuple[List[int], int], the sorted array and the `statistic` defined above.
    """
    def _merge_sort(left_index: int, right_index: int) -> int:
        """Sorts a given subarray and returns the corresponding `statistic`."""
        # [YOUR CODE HERE] Check some corner cases...

        # Don't change this!
        middle_index = (left_index + right_index) // 2

        statistic = 0
        # [YOUR CODE HERE] Call _merge_sort a few times and aggregate `statistic` values...

        # [YOUR CODE HERE] Update `statistic`...

        # [YOUR CODE HERE] Call merge_sorted_subarrays

        # [YOUR CODE HERE] Update `statistic` again...

        return statistic

    result_statistic = _merge_sort(0, len(data) - 1)

    return data, result_statistic
```

**Example 1:**

`data`=[3, 2, 1]

Expected output: [1, 2, 3], 27

Explanation:

`merge_sorted_subarrays` was called twice:
* merge_sorted_subarrays(0, 0, 1)
  * `statistic` += 3 + 3 + 2 (Before the call)
  * `statistic` += 2 + 2 + 3 (After the call)
* merge_sorted_subarrays(0, 1, 2)
  * `statistic` += 2 + 3 + 1 (Before the call)
  * `statistic` += 1 + 2 + 3 (After the call)


**Example 2:**

`data`=[5, 3, 1, 5, 2]

Expected output: [1, 2, 3, 5, 5], 83

Explanation:

`merge_sorted_subarrays` was called four times:
* merge_sorted_subarrays(0, 0, 1)
  * `statistic` += 5 + 5 + 3 (Before the call)
  * `statistic` += 3 + 3 + 5 (After the call)
* merge_sorted_subarrays(0, 1, 2)
  * `statistic` += 3 + 5 + 1 (Before the call)
  * `statistic` += 1 + 3 + 5 (After the call)
* merge_sorted_subarrays(3, 3, 4)
  * `statistic` += 5 + 5 + 2 (Before the call)
  * `statistic` += 2 + 2 + 5 (After the call)
* merge_sorted_subarrays(0, 2, 4)
  * `statistic` += 1 + 5 + 5 (Before the call)
  * `statistic` += 1 + 3 + 5 (After the call)


**Example 3:**

`data`=[5, 3, 6, 2, 1, 7, 3, 2]

Expected output: [1, 2, 2, 3, 3, 5, 6, 7], 153

**Example 4:**

`data`=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 315

<br>

Please use the template `tasks/merge_sort.py:merge_sorted_subarrays+merge_sort_algorithm` for the implementation.
