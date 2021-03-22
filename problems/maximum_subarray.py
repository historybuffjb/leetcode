"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
largest sum and return its sum.
"""
from sys import maxsize

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Explanation
    We can iterate through the array keeping track of a local maximum that is defined as follows:
        * At each element we set local maximum to the maximum of the current value and current value + local maximum
        * If at any time we encounter a new maximum overall we save that value
        * At the end we return our largest maximum found
    """
    cur_max = 0
    result = -maxsize - 1
    for num in nums:
        cur_max = max(num, cur_max + num)
        result = max(result, cur_max)
    return result


"""
Run DETAILS
Runtime: 68 ms, faster than 54.97% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.9 MB, less than 60.75% of Python3 online submissions for Maximum Subarray.
"""