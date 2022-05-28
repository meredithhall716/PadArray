#REMEMBER TO PSEUDOCODE
from unittest.util import _count_diff_hashable


def pad(array, min_size, value = None):
    count = len(array)
    pad_count = min_size - count
    while pad_count > 0:
        array.append(value)
        pad_count -= 1
        
    return array