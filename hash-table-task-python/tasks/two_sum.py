from typing import List, Tuple


def find_target_sum(values: List[int], target: int) -> Tuple[int, int]:
    """Returns a pair of indices so that the corresponding values add up to a given target.

    Args:
        values: List, available elements for look-up.
        target: int, target sum for look-up.

    Returns:
        Tuple[int, int], two indices of interest.
    """
    hash_table = {}
    for i, num in enumerate(values):
        complement = target - num
        if complement in hash_table:
            return (hash_table[complement], i)
        hash_table[num] = i
