from typing import List

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
    n = len(data)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


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
    for i in range(1, k + 1):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


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
    n = len(data)
    swap_count = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap_count += 1
                if swap_count == k:
                    return data
    return data
