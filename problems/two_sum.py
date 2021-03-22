"""
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order.
"""
from typing import List, Dict


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Explanation:
        * Loop through nums and do the following:
            * Check if list element - target in dict:
                * If so return {dict[list element], current index}
            * Else:
                * Store results of list in a dictionary with list element as key and index as value
            *
        *
    """
    result_dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in result_dict:
            return [result_dict[temp], i]
        result_dict[nums[i]] = i


"""
RUN DETAILS
Runtime: 44 ms, faster than 85.74% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 46.77% of Python3 online submissions for Two Sum.
"""
