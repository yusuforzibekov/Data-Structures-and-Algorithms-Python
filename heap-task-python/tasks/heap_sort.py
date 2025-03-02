from typing import List

def min_heapify(data: List[int]) -> List[int]:
    """Returns the result of running the `heapify` (minimum) operation on a given array of numbers."""
    result = data.copy()
    n = len(result)
    
    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(result, i, n)
    
    return result

def _sift_down(arr: List[int], i: int, heap_size: int):
    """Helper function to maintain heap property."""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left
        
    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right
        
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        _sift_down(arr, smallest, heap_size)

def heap_sort(data: List[int]) -> List[int]:
    """Sorts a given array in ascending order using the heap sort algorithm."""
    # Make a copy to avoid modifying the input
    result = data.copy()
    n = len(result)
    
    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(result, i, n)
    
    # Extract elements one by one
    result_array = []
    for i in range(n):
        result_array.append(result[0])
        result[0] = result[n - i - 1]
        _sift_down(result, 0, n - i - 1)
        
    return result_array
