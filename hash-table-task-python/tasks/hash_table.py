from typing import Any, List, Optional


class KeyValueData:
    """Data that will be stored in hash table.

    NOTE: no need to change this class.
    """

    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value


class Bucket:
    """Represents a set of (K,V) pairs that were assigned to the same bin/chain/bucket."""

    def __init__(self):
        self.elements: List[KeyValueData] = []

    def get(self, key: int) -> Optional[Any]:
        """Returns the value for a given key.

        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        for element in self.elements:
            if element.key == key:
                return element.value
        raise ValueError("Key not found")

    def put(self, key: int, value: Any):
        """Puts a given (K,V) pair into the bucket."""
        for element in self.elements:
            if element.key == key:
                element.value = value
                return
        self.elements.append(KeyValueData(key, value))

    def remove(self, key: int):
        """Removes the (K,V) pair for a given key.

        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        for i, element in enumerate(self.elements):
            if element.key == key:
                del self.elements[i]
                return
        raise ValueError("Key not found")


class HashTable:
    """Basic Hash Table interface."""

    def __init__(self, n_buckets: int = 100):
        self.n_buckets = n_buckets
        self.buckets = [Bucket() for _ in range(n_buckets)]

    def h(self, key: int) -> int:
        # Here we use the simplest type of hash function.
        return key % self.n_buckets

    def set(self, key: int, value: Any):
        """Inserts a given (K,V) pair.

        NOTE: If the key is already in the hash table, the value should be replaced.
        """
        bucket_index = self.h(key)
        self.buckets[bucket_index].put(key, value)

    def get(self, key: int) -> Optional[Any]:
        """Returns the value for a given key.

        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        bucket_index = self.h(key)
        return self.buckets[bucket_index].get(key)

    def remove(self, key: int):
        """Removes the (K,V) pair for a given key.

        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        bucket_index = self.h(key)
        self.buckets[bucket_index].remove(key)
