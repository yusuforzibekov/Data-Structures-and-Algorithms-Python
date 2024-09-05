"""Sample tests for 'tasks.linked_list' module."""
from tasks.linked_list import merge_sorted_lists, ListNode


def test_merge_sorted_lists_sample():
    """Tests for merge_sorted_lists function."""
    # Example 1
    list_a = ListNode(5, ListNode(11, ListNode(30)))
    list_b = ListNode(1, ListNode(6))
    result = merge_sorted_lists(list_a, list_b)
    
    assert result.value == 1
    assert result.next.value == 5
    assert result.next.next.value == 6
    assert result.next.next.next.value == 11
    assert result.next.next.next.next.value == 30
    assert result.next.next.next.next.next is None

    # Example 2
    list_a = ListNode(5, ListNode(11, ListNode(30)))
    list_b = None
    result = merge_sorted_lists(list_a, list_b)
    
    assert result.value == 5
    assert result.next.value == 11
    assert result.next.next.value == 30
    assert result.next.next.next is None

    # Example 3
    list_a = ListNode(5, ListNode(11, ListNode(30)))
    list_b = ListNode(5, ListNode(11, ListNode(30)))
    result = merge_sorted_lists(list_a, list_b)
    
    assert result.value == 5
    assert result.next.value == 5
    assert result.next.next.value == 11
    assert result.next.next.next.value == 11
    assert result.next.next.next.next.value == 30
    assert result.next.next.next.next.next.value == 30
    assert result.next.next.next.next.next.next is None
    