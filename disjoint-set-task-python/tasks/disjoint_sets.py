"""Template for programming assignment: disjoint sets data structure."""

from typing import Union

# For simplicity, assume that keys are either strings or integers.
KeyType = Union[str, int]


class DisjointSets:
    """Interface for supporting disjoint sets.

    NOTE: the expected implementation should contain:
    * 'path compression' heuristic
    * 'union by rank' heuristic (height)
    """

    def __init__(self):
        # Dictionary to store the parent of each node
        self.parent = {}
        # Dictionary to store the rank of each node
        self.rank = {}

    def make_set(self, key: KeyType):
        """Creates a new set that is associated with a given key."""
        self.parent[key] = key
        self.rank[key] = 0

    def find_set(self, key: KeyType) -> KeyType:
        """Returns a unique set identifier (key) of a given's key set.

        NOTE: 'path compression' heuristic should be used.
        """
        if self.parent[key] != key:
            self.parent[key] = self.find_set(self.parent[key])  # Path compression
        return self.parent[key]

    def union_sets(self, first_key: KeyType, second_key: KeyType):
        """Joins two given sets into a new one.

        NOTE: 'union by rank' heuristic should be used (the height one).
        NOTE: if the sets that correspond to the given keys are of the same rank,
        if is preferable to use the second set when deciding what set is to be used as a new 'root'.
        """
        root1 = self.find_set(first_key)
        root2 = self.find_set(second_key)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1