"""Sample tests for 'tasks.hash_table' module."""
import pytest

from tasks.hash_table import Bucket, HashTable, KeyValueData


def test_bucket_class():
    """Sample tests for Bucket class."""
    bucket = Bucket()
    bucket.put(0, 'hello')
    bucket.put(1, 3134)
    bucket.put(235134, ['foo', 'bar'])
    assert len(bucket.elements) == 3

    with pytest.raises(ValueError):
        _ = bucket.get(107)

    assert bucket.get(0) == 'hello'

    bucket.remove(0)
    with pytest.raises(ValueError):
        _ = bucket.get(0)   


def test_hash_table_class():
    """Sample tests for HashTable class."""
    hash_table = HashTable(n_buckets=3)
    hash_table.set(0, 'hello') # 0 bucket
    hash_table.set(1, 'world') # 1 bucket
    assert hash_table.get(0) == 'hello'

    hash_table.set(3, 'hello2') # 0 bucket again
    assert len(hash_table.buckets[0].elements) == 2

    hash_table.set(0, 'hello_new') # 0 bucket, replace
    assert len(hash_table.buckets[0].elements) == 2
    assert hash_table.get(0) == 'hello_new'
