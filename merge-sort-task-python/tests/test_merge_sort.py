"""Sample tests for 'tasks.merge_sort' module."""
from tasks.merge_sort import merge_sorted_subarrays, merge_sort_algorithm


def test_merge_sort_algorithm_sample():
    """Tests for merge_sorted_subarrays and merge_sort_algorithm functions."""
    # Sample test for `merge_sorted_subarrays``.
    data = [1, 3, 5, 2, 4, 6]
    merge_sorted_subarrays(data, 0, 2, 5)
    assert data == [1, 2, 3, 4, 5, 6]

    # Example 1
    assert merge_sort_algorithm([3, 2, 1]) == ([1, 2, 3], 27)
    # Example 2
    assert merge_sort_algorithm([5, 3, 1, 5, 2]) == ([1, 2, 3, 5, 5], 83)
    # Example 3
    assert merge_sort_algorithm([5, 3, 6, 2, 1, 7, 3, 2]) == ([1, 2, 2, 3, 3, 5, 6, 7], 153)
    # Example 4
    assert merge_sort_algorithm([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 315)
