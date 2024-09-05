"""Sample tests for 'tasks.sorting' module."""
from tasks.sorting import partial_selection_sort, partial_insertion_sort, partial_bubble_sort


def test_partial_selection_sort_sample():
    """Tests for partial_selection_sort function."""
    assert partial_selection_sort([4, 8, 6, 2, 5], 1) == [2, 8, 6, 4, 5]
    assert partial_selection_sort([4, 8, 6, 2, 5], 2) == [2, 4, 6, 8, 5]
    assert partial_selection_sort([4, 8, 6, 2, 5], 3) == [2, 4, 5, 8, 6]
    assert partial_selection_sort([4, 8, 6, 2, 5], 4) == [2, 4, 5, 6, 8]


def test_partial_insertion_sort_sample():
    """Tests for partial_insertion_sort function."""
    assert partial_insertion_sort([4, 8, 6, 2, 5], 1) == [4, 8, 6, 2, 5]
    assert partial_insertion_sort([4, 8, 6, 2, 5], 2) == [4, 6, 8, 2, 5]
    assert partial_insertion_sort([4, 8, 6, 2, 5], 3) == [2, 4, 6, 8, 5]
    assert partial_insertion_sort([4, 8, 6, 2, 5], 4) == [2, 4, 5, 6, 8]


def test_partial_bubble_sort_sample():
    """Tests for partial_bubble_sort function."""
    assert partial_bubble_sort([4, 8, 6, 2, 5], 1) == [4, 6, 8, 2, 5]
    assert partial_bubble_sort([4, 8, 6, 2, 5], 2) == [4, 6, 2, 8, 5]
    assert partial_bubble_sort([4, 8, 6, 2, 5], 3) == [4, 6, 2, 5, 8]
    assert partial_bubble_sort([4, 8, 6, 2, 5], 4) == [4, 2, 6, 5, 8]
    assert partial_bubble_sort([4, 8, 6, 2, 5], 5) == [4, 2, 5, 6, 8]
    assert partial_bubble_sort([4, 8, 6, 2, 5], 6) == [2, 4, 5, 6, 8]
