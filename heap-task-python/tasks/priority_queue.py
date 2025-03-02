"""Template for programming assignment: Priority Queue."""

class PriorityQueue:
    """The basic interface for Priority Queue."""

    def __init__(self):
        self.heap = []

    def get_minimum(self) -> int:
        """Returns the minimum in the data structure.

        NOTE: the expected time complexity is O(1).
        """
        if not self.heap:
            raise IndexError("PriorityQueue is empty")
        return self.heap[0]
    
    def _bubble_up(self, index):
        """Helper function to maintain heap property after insertion."""
        parent = (index - 1) // 2
        
        if index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._bubble_up(parent)
    
    def _bubble_down(self, index):
        """Helper function to maintain heap property after removal."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)
    
    def pop(self) -> int:
        """Returns the minimum in the data structure and removes it.
        
        NOTE: the expected time complexity is O(log N), where N is the number of elements in the data structure.
        """
        if not self.heap:
            raise IndexError("PriorityQueue is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        
        return min_val
    
    def insert(self, value: int):
        """Inserts a given value into the data structure.

        NOTE: the expected time complexity is O(log N), where N is the number of elements in the data structure.
        """
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def is_empty(self) -> bool:
        """Returns True if there are no elements in the data structure.
        
        NOTE: the expected time complexity is O(1).
        """
        return len(self.heap) == 0
    
    def size(self) -> int:
        """Returns the number of elements in the data structure.
        
        NOTE: the expected time complexity is O(1).
        """
        return len(self.heap)
