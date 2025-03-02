"""Sample tests for 'tasks.priority_queue' module."""
from tasks.priority_queue import PriorityQueue


def test_priority_queue_sample():
    """Sample tests for PriorityQueue class."""
    # Example 1
    pq = PriorityQueue()
    assert pq.is_empty() # empty at first

    pq.insert(4) # {4}
    pq.insert(3) # {3, 4}
    pq.insert(2) # {2, 3, 4}
    assert pq.size() == 3

    assert pq.pop() == 2 # {3, 4}
    assert pq.get_minimum() == 3

    pq.insert(1) # {1, 3, 4}
    assert pq.get_minimum() == 1

    # Example 2
    pq = PriorityQueue()
    pq.insert(1) # {1}
    pq.insert(2) # {1, 2}
    pq.insert(3) # {1, 2, 3}
    pq.insert(4) # {1, 2, 3, 4}
    pq.insert(5) # {1, 2, 3, 4, 5}

    assert pq.pop() == 1 # {2, 3, 4, 5}
    assert pq.pop() == 2 # {3, 4, 5}
    assert pq.pop() == 3 # {4, 5}
    assert pq.pop() == 4 # {5}
    assert pq.pop() == 5 # {}

    assert pq.is_empty()
