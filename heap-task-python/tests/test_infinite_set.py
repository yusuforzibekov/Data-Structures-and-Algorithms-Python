"""Sample tests for 'tasks.infinite_set' module."""
from tasks.infinite_set import InfiniteSet


def test_infinite_set_sample():
    """Sample tests for InfiniteSet class."""
    # Example 1
    inf_set = InfiniteSet() # {1, 2, 3, 4, 5, ...}
    assert inf_set.pop_minimum() == 1 # {2, 3, 4, 5, 6, ...}
    assert inf_set.pop_minimum() == 2 # {3, 4, 5, 6, ...}
    assert inf_set.pop_minimum() == 3 # {4, 5, 6, ...}
    assert inf_set.pop_minimum() == 4 # {5, 6, 7, ...}
    assert inf_set.pop_minimum() == 5 # {6, 7, 8, ...}
    inf_set.insert(3) # {3, 6, ...}
    inf_set.insert(1) # {1, 3, 6, ...}
    assert inf_set.pop_minimum() == 1 # {3, 6, 7, ...}
    assert inf_set.pop_minimum() == 3 # {6, 7, 8, ...}
    assert inf_set.pop_minimum() == 6 # {7, 8, 9, ...}

    # Example 2
    inf_set = InfiniteSet() # {1, 2, 3, 4, 5, ...}

    for _ in range(100):
        assert inf_set.pop_minimum() == _ + 1
    # After 100 .pop_minimum() operations
    assert inf_set.pop_minimum() == 101 # {102, 103, 104, ...}
    inf_set.insert(35) # {35, 102, 103, ...}
    inf_set.insert(23) # {23, 35, 102, ...}
    assert inf_set.pop_minimum() == 23 # {35, 102, ...}
    assert inf_set.pop_minimum() == 35 # {102, 103, ...}
    assert inf_set.pop_minimum() == 102 # {103, 104, ...}
