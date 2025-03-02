"""Sample tests for 'tasks.heap_sort' module."""
from typing import List

from tasks.heap_sort import min_heapify, heap_sort


def _check_heap(h: List[int]):
    for i, x in enumerate(h):
        if 2 * i + 1 < len(h):
            assert x <= h[2 * i + 1]
        if 2 * i + 2 < len(h):
            assert x <= h[2 * i + 2]


def test_heap_sort_sample():
    """Sample tests for heap_sort and min_heapify functions."""
    # Example 1
    data = [6, 4, 2, 1, 6, 3]

    h = min_heapify(data)
    assert len(h) == len(data)
    assert set(data) == set(h)
    _check_heap(h)

    assert heap_sort(data) == [1, 2, 3, 4, 6, 6]

    # Example 2
    data = [1000, 100, 1, 10]

    h = min_heapify(data)
    assert h in [
        [1, 10, 100, 1000],
        [1, 100, 10, 1000],
        [1, 10, 1000, 100],
    ]

    assert heap_sort(data) == [1, 10, 100, 1000]
