"""Template for programming assignment: tree validity."""

from typing import List, Tuple
from .disjoint_sets import DisjointSets


def is_valid_tree(n: int, edges: List[Tuple[int, int]]) -> bool:
    """Checks whether a given graph is a valid tree.

    Args:
        n: int, number of vertexes in a given graph.
        edges: List[Tuple[int, int]], list of edges of a given graph.

    Returns:
        Whether a given graph is a valid tree.
    """
    if len(edges) != n - 1:
        return False

    ds = DisjointSets()

    for i in range(n):
        ds.make_set(i)

    for u, v in edges:
        if ds.find_set(u) == ds.find_set(v):
            return False
        ds.union_sets(u, v)

    return True
