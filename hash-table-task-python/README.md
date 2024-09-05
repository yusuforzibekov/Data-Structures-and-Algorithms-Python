# Hash table

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:

* Hash table data structure and its API
* Resolving collisions using the chaining (bucketing) method

## Overview

The coding exercises cover the following practical problems:
* Implementing a hash table with chaining
* The 2-SUM problem
* Finding repeated patterns in a DNA sequence

## Coding exercises

### Exercise 1: Implement a hash table with chaining

Implement the HashTable interface **without using any hash table libraries**.

The following building blocks are provided for you:

* Assume that only integers will be used as keys. `KeyValueData` wraps a (key, value) pair.
```python
# tasks/hash_table.py

class KeyValueData:
    """Data that will be stored in hash table.
    
    NOTE: no need to change this class.
    """
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
```

* Each chain or bucket of `HashTable` will be be handled by the `Bucket` class, which has the following API:
```python
# tasks/hash_table.py

class Bucket:
    """Represents a set of (K,V) pairs that were assigned to the same bin/chain/bucket."""

    def __init__(self):
        self.elements: List[KeyValueData] = []

    def get(self, key: int) -> Optional[Any]:
        """Returns the value for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass

    def put(self, key: int, value: Any):
        """Puts a given (K,V) pair into the bucket."""
        pass

    def remove(self, key: int):
        """Removes the (K,V) pair for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass
```

* Main `HashTable` API:
```python
# tasks/hash_table.py

class HashTable:
    """Basic Hash Table interface."""

    def __init__(self, n_buckets: int = 100):
        self.n_buckets = n_buckets
        self.buckets = ... # Create #n_buckets Bucket objects.
    
    def h(self, key: int) -> int:
        # Here we use the simplest type of hash function.
        return key % self.n_buckets
    
    def set(self, key: int, value: Any):
        """Inserts a given (K,V) pair.
        
        NOTE: If the key is already in the hash table, the value should be replaced.
        """
        pass
    
    def get(self, key: int) -> Optional[Any]:
        """Returns the value for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass
    
    def remove(self, key: int):
        """Removes the (K,V) pair for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass
```

**Example:**

```python
hash_table = HashTable(n_buckets=3)
hash_table.set(0, 'hello') # 0 bucket
hash_table.set(1, 'world') # 1 bucket
assert hash_table.get(0) == 'hello'

hash_table.set(3, 'hello2') # 0 bucket again
assert len(hash_table.buckets[0].elements) == 2

hash_table.set(0, 'hello_new') # 0 bucket, replace
assert len(hash_table.buckets[0].elements) == 2
assert hash_table.get(0) == 'hello_new'
```

<br>

Please use the template `tasks/hash_table.py` for the implementation.

### Exercise 2: Find two numbers that add up to a given target

Given an array of integers `values` and an integer `target`, return *indices of the two numbers so that they add up to `target`*.

Assume that each input will have **exactly one solution** and you may not use the same element twice.

You can return the answer in any order.

**Constraints**
* 2 <= values.length <= 3*10^5
* -10^9 <= values[i] <= 10^9
* -10^9 <= target <= 10^9
* Only one valid answer exists.

Your task is to implement the following function for solving the problem above:

```python
def find_target_sum(values: List[int], target: int) -> Tuple[int, int]:
    """Returns a pair of indices so that the corresponding values add up to a given target.

    Args:
        values: List, available elements for look-up.
        target: int, target sum for look-up.

    Returns:
        Tuple[int, int], two indices of interest.
    """
    pass
```

**Example 1:**

Input: values = [1, 2, 3, 4, 5], target = 4

Output: [0, 2]

Explanation: values[0] + values[2] == 4


**Example 2:**

Input: values = [1, 2, 3, 4, 5], target = 8

Output: [2, 4]

Explanation: values[2] + values[4] == 8

<br>

Please use the template `tasks/two_sum.py:find_target_sum` for the implementation.

### Exercise 3: Repeated DNA Sequences

A **DNA sequence** is composed of a series of nucleotides abbreviated `'A'`, `'C'`, `'G'`, and `'T'`.

For example, `"ACGAATTCCG"` is a DNA sequence.
When studying **DNA**, it is useful to identify repeated sequences within the DNA.

Given a string `dna_sequence` that represents a **DNA sequence**, return all the `8`**-letter-long** sequences (substrings) that occur more than once in the DNA molecule. You may return the answer in **any order**.

**Constraints**
* 1 <= dna_sequence.length <= 10^5
* dna_sequence contains only 'A', 'C', 'G' and 'T' characters.

Your task is to implement the following function to solve the problem above:

```python
def find_repeated_dna_sequences(dna_sequence: str) -> List[str]:
    """Returns all 8-letter-long substrings that occur more than once.

    Args:
        dna_sequence: str, a given DNA sequence.

    Returns:
        List[str], list of all 8-letter-long substrings that occur more than once.
    """
    pass
```

**Example 1**

Input: dna_sequence='AAAATTTTAAAATTTT'

Output: ['AAAATTTT']


**Example 2**

Input: dna_sequence='ATATATATATA'

Output: ['ATATATAT', 'TATATATA']

<br>

Please use the template `tasks/dna.py:find_repeated_dna_sequences` for the implementation.
