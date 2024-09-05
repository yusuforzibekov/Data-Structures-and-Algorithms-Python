"""Sample tests for 'tasks.disjoint_sets' module."""

from tasks.disjoint_sets import DisjointSets


def test_disjoint_sets_sample():
    """Sample tests for DisjointSets class."""
    ds = DisjointSets()
    # Let's create 5 sets
    for set_id in range(5):
        ds.make_set(set_id)
        assert ds.find_set(set_id) == set_id
    # Let's join some sets: {0; 1, 2}, {3, 4}
    ds.union_sets(0, 1)
    ds.union_sets(0, 2)
    ds.union_sets(3, 4)

    assert ds.find_set(0) == ds.find_set(1)
    assert ds.find_set(0) == ds.find_set(2)
    assert ds.find_set(3) == ds.find_set(4)

    assert ds.find_set(0) != ds.find_set(3)
