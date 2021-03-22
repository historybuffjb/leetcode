"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List


def contains_duplicates(nums: List[int]) -> bool:
    """
    Explanation
        * Just keep found digits in dict
            * If current digit in dict, return True
            * Else at end, return False
    """
    if len(nums) == 1:
        return False
    dict_holder = {}
    for val in nums:
        if val in dict_holder:
            return True
        dict_holder[val] = None
    return False


"""
Run DETAILS
Runtime: 108 ms, faster than 97.33% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21.4 MB, less than 19.02% of Python3 online submissions for Contains Duplicate.
"""