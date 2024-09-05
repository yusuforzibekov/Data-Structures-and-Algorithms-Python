from typing import Optional


class ListNode:
    """Data class for representing singly-linked list's nodes."""

    def __init__(self, value: int = None, next: "ListNode" = None):
        self.value = value
        self.next = next


def merge_sorted_lists(list_a: Optional[ListNode], list_b: Optional[ListNode]) -> Optional[ListNode]:
    """Returns a merged (sorted) linked list head using two given (sorted) linked lists.

    NOTE: the expected time complexity is O(n+m), where n=|list_a| and m=|list_b|

    Args:
        list_a: ListNode, the head element of the first sorted linked list
        list_b: ListNode, the head element of the second sorted linked list
    Returns:
        ListNode, the result of merging two given lists
    """
    dummy = ListNode()
    tail = dummy
    
    while list_a and list_b:
        if list_a.value < list_b.value:
            tail.next = list_a
            list_a = list_a.next
        else:
            tail.next = list_b
            list_b = list_b.next
        tail = tail.next

    if list_a:
        tail.next = list_a
    if list_b:
        tail.next = list_b

    return dummy.next
