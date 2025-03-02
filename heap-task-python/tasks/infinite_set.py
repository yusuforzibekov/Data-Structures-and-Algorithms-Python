"""Template for programming assignment: Infinite Set."""

class InfiniteSet:
    """Emulates a set of all natural numbers."""

    def __init__(self):
        self.available_numbers = []
        self.next_number = 1
    
    def _bubble_up(self, index):
        """Helper function to maintain heap property after insertion."""
        parent = (index - 1) // 2
        
        if index > 0 and self.available_numbers[parent] > self.available_numbers[index]:
            self.available_numbers[parent], self.available_numbers[index] = self.available_numbers[index], self.available_numbers[parent]
            self._bubble_up(parent)
    
    def _bubble_down(self, index):
        """Helper function to maintain heap property after removal."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.available_numbers) and self.available_numbers[left] < self.available_numbers[smallest]:
            smallest = left
            
        if right < len(self.available_numbers) and self.available_numbers[right] < self.available_numbers[smallest]:
            smallest = right
            
        if smallest != index:
            self.available_numbers[index], self.available_numbers[smallest] = self.available_numbers[smallest], self.available_numbers[index]
            self._bubble_down(smallest)

    def pop_minimum(self) -> int:
        """Returns the minimum natural number available and removes it from the set."""
        if self.available_numbers:
            if len(self.available_numbers) == 1:
                return self.available_numbers.pop()
            
            min_val = self.available_numbers[0]
            self.available_numbers[0] = self.available_numbers.pop()
            self._bubble_down(0)
            return min_val
        else:
            num = self.next_number
            self.next_number += 1
            return num

    def insert(self, x: int):
        """Inserts a given number back into the set."""
        self.available_numbers.append(x)
        self._bubble_up(len(self.available_numbers) - 1)