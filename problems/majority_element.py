"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.
"""
from sys import maxsize
from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Explanation
    The idea here is to keep a hashmap where the key is a number in the array and the value is the number of occurrences
    we have found of that number. If we ever encounter a situation where we have found an element more than len(nums)/2
    times, then return num.
    """
    if len(nums) == 1:
        return nums[0]
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
        if nums_dict[num] > len(nums) / 2:
            return num
    return -1


"""
Runtime: 180 ms, faster than 31.39% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 52.09% of Python3 online submissions for Majority Element.
"""
